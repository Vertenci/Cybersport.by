import re

from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomAuthenticationForm, RegisterForm
from django.contrib.auth import login, logout
from django.views.decorators.csrf import csrf_exempt
from .models import EmailVerificationCode
from .tasks import send_verification_email


VALID_NAME_REGEX = re.compile(r'[\w\s()-]+$')


@login_required
def profile_home(request):
    user_profile = request.user
    user_groups = user_profile.groups.all()
    user_permissions = user_profile.get_all_permissions()
    registration_date = user_profile.date_joined.date()
    return render(request, 'userprofiles/profile.html', {
        'user_profile': user_profile,
        'user_groups': user_groups,
        'user_permissions': user_permissions,
        'registration_date': registration_date
    })


def pre_login(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('news_home')
        else:
            messages.error(request, "Неверные данные для входа.")
    else:
        form = CustomAuthenticationForm()
    return render(request, 'userprofiles/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('news_home')


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()

            code = get_random_string(length=6, allowed_chars='0123456789')
            EmailVerificationCode.objects.create(user=user, code=code)

            send_verification_email.delay(user.email, code)

            return redirect('verify_email')
    else:
        form = RegisterForm()
    return render(request, 'userprofiles/register.html', {'form': form})


@csrf_exempt
def update_profile(request):
    if request.method == 'POST':
        user = request.user

        first_name = request.POST.get('first_name', '').strip()
        last_name = request.POST.get('last_name', '').strip()
        # email = request.POST.get('email', '').strip()

        if first_name and len(first_name) < 100 and VALID_NAME_REGEX.match(first_name):
            user.first_name = first_name
        if last_name and len(last_name) < 100 and VALID_NAME_REGEX.match(last_name):
            user.last_name = last_name
        # if email is not None:
        #     user.email = email

        user.save()

        return JsonResponse({
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email
        })


def verify_email(request):
    if request.method == 'POST':
        code = request.POST.get('code')
        try:
            verification = EmailVerificationCode.objects.get(code=code)
            if verification.is_valid():
                user = verification.user
                user.is_active = True
                user.save()
                verification.delete()

                messages.success(request, "Email успешно подтвержден!")
                return redirect('login')
            else:
                messages.error(request, "Код истек. Пожалуйста, запросите новый.")
        except EmailVerificationCode.DoesNotExist:
            messages.error(request, "Неверный код.")
    return render(request, 'userprofiles/verify_email.html')


def resend_verification_code(request):
    if request.method == 'POST':
        email = request.POST.get('email')

        if email:
            try:
                user = EmailVerificationCode.objects.filter(user__email=email).first().user
                EmailVerificationCode.objects.filter(user=user).delete()

                code = get_random_string(length=6, allowed_chars='0123456789')
                EmailVerificationCode.objects.create(user=user, code=code)

                send_verification_email.delay(email, code)

                messages.success(request, "Код подтверждения отправлен снова!")
                return redirect('verify_email')
            except AttributeError:
                messages.error(request, "Пользователь с этой электронной почтой не найден.")
        else:
            messages.error(request, "Пожалуйста, введите вашу электронную почту.")

    return render(request, 'userprofiles/verify_email.html')

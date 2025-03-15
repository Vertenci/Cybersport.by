from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomAuthenticationForm, RegisterForm
from django.contrib.auth import login, logout
from django.views.decorators.csrf import csrf_exempt


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
        form = CustomAuthenticationForm()
    return render(request, 'userprofiles/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('news_home')


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'userprofiles/register.html', {'form': form})


@csrf_exempt
def update_profile(request):
    if request.method == 'POST':
        user = request.user

        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')

        if first_name is not None:
            user.first_name = first_name
        if last_name is not None:
            user.last_name = last_name
        if email is not None:
            user.email = email

        user.save()

        return JsonResponse({
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email
        })

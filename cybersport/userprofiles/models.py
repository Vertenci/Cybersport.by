from django.contrib.auth.models import User
from django.db import models
from django.utils.timezone import now
from datetime import timedelta


class EmailVerificationCode(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="email_verification_code")
    code = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)

    def is_valid(self):
        return now() < self.created_at + timedelta(minutes=10)

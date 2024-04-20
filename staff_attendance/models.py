from django.db import models
from django.utils import timezone

from django.contrib.auth.models import User

# class User(AbstractUser):
#     """admin"""
#     avatar = models.ImageField(blank=True, null=True, upload_to='avatar/')

#     class Meta(AbstractUser.Meta):
#         swappable = "AUTH_USER_MODEL"


class Staff(models.Model):
    """Xodim"""
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    choices = (
        ("ish_yurituvchi", "Ish yurituvchi"),
        ("ishchi", "Ishchi")
    )
    status = models.CharField(max_length=255, choices=choices, default="ishchi")
    avatar = models.ImageField(max_length=255, blank=True, null=True, upload_to='avatar/')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Attendance(models.Model):
    """Davomat"""
    body = models.ForeignKey(Staff, on_delete=models.CASCADE)
    arrival_time = models.DateTimeField(default=timezone.now)
    time_gone = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.body.first_name} - {self.arrival_time}"

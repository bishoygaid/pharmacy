from django.db import models
from django.contrib.auth.models import User


class Doctor(models.Model):
    user = models.OneToOneField(
        User, related_name='doctor', on_delete=models.CASCADE
    )
    phone = models.CharField(max_length=20, blank=True, null=True)


class Branch(models.Model):
    doctor = models.ForeignKey(
        Doctor, related_name='branches', on_delete=models.CASCADE
    )
    country = models.CharField(max_length=20, blank=True, null=True)
    city = models.CharField(max_length=20, blank=True, null=True)
    state = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)

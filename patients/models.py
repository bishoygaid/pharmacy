from django.db import models
from django.contrib.auth.models import User


class Patient(models.Model):
    full_name = models.CharField(max_length=250)
    phone = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.full_name

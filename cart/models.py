from django.db import models
from pharmacies.models import Medicine
from doctors.models import Doctor
from patients.models import Patient


class Cart(models.Model):
    doctor = models.ForeignKey(
        Doctor, related_name='doctors', on_delete=models.CASCADE
    )
    patient = models.ForeignKey(
        Patient, related_name='patients', on_delete=models.CASCADE
    )
    medecines = models.ManyToManyField(Medicine, blank=True)
    summry = models.TextField(blank=True, null=True)

from django.db import models


class Pharmacy(models.Model):
    name = models.CharField(max_length=250)


class Branch(models.Model):
    pharmacy = models.ForeignKey(
        Pharmacy, related_name='branches', on_delete=models.CASCADE
    )
    country = models.CharField(max_length=20, blank=True, null=True)
    city = models.CharField(max_length=20, blank=True, null=True)
    state = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)

class Phone(models.Model):
    pharmacy = models.ForeignKey(
        Pharmacy, related_name='phones', on_delete=models.CASCADE
    )
    phone = models.CharField(max_length=20, blank=True, null=True)


class Medicine(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    code = models.CharField(max_length=200, blank=True, null=True)
    price = models.FloatField(default=0)
    expire_date = models.DateTimeField(blank=True, null=True)

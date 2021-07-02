from django.contrib import admin

from .models import Pharmacy, Branch, Phone, Medicine


admin.site.register(Pharmacy)
admin.site.register(Phone)
admin.site.register(Branch)
admin.site.register(Medicine)

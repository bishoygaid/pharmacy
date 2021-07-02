from django import forms
from .models import Cart, Patient


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ["id", 'full_name', 'phone']

class CartForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CartForm, self).__init__(*args, **kwargs)
        self.fields.pop('doctor')
        self.fields.pop('patient')

    class Meta:
        model = Cart
        fields = ['doctor', 'patient', 'medecines', 'summry']

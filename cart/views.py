import logging
from django.db.models import Sum
from django.shortcuts import render, get_object_or_404, redirect
from .models import Cart
from .forms import CartForm, PatientForm

logger = logging.getLogger(__name__)

def create_cart(request):
    if request.method == "POST":
        form = CartForm(request.POST or None)
        patient_form = PatientForm(request.POST or None)
        if patient_form.is_valid():
            patient_id = patient_form.save()
            cart = form.save(commit=False)
            cart.patient = patient_id
            cart.doctor = request.user.doctor
            cart.save()
            form.save_m2m()
            return redirect("cart_detail", pk=cart.id)
    else:
        form = CartForm()
        patient_form = PatientForm()

    template = "create_cart.html"
    context = {"form": form, "patient_form": patient_form}
    return render(request, template, context)


def cart_detail(request, pk):
    cart = get_object_or_404(Cart, pk=pk)
    total_price = cart.medecines.aggregate(total=Sum("price")).get("total")
    return render(request, "cart_detail.html", context={"cart": cart, "total_price": total_price, "medecines": cart.medecines.all()})

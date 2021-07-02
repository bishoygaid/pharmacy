from django.shortcuts import render


def home_page(request):
    context = {}
    return render(request, "home.html", context)

def departments(request):
    context = {}
    return render(request, "departments.html", context)

def doctors(request):
    context = {}
    return render(request, "doctors.html", context)

def contact(request):
    context = {}
    return render(request, "contact.html", context)

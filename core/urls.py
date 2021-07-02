from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_page, name="home"),
    path('departments/', views.departments, name="departments"),
    path('doctors/', views.doctors, name="doctors"),
    path('contact/', views.contact, name="contact"),
]

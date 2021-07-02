from django.urls import path
from . import views


urlpatterns = [
    path('cart/', views.create_cart, name="create_cart"),
    path('cart/<int:pk>', views.cart_detail, name="cart_detail"),
]

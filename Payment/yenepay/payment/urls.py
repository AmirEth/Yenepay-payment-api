from django.urls import path
from .views import payment_with_cart, success, cancel

urlpatterns = [
    path('', payment_with_cart, name='cart-payment'),
    path('success/', success, name='success'),
    path('cancel/', cancel, name='cancel'),

]

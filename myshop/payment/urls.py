from django.urls import path
from . import views

app_name = 'payment'

urlpatterns = [
    path('process/',views.payment_process, name='payment_process'),
    path('completed/',views.payment_success, name='payment_success'),
    path('canceled/',views.payment_failure, name='payment_failure'),
]

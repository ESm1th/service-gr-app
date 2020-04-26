from django.urls import path

from . import views


app_name = 'web'

urlpatterns = [
    path('deliveries/', views.DeliveryList.as_view(), name='deliveries'),
]

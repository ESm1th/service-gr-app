from django.urls import path

from . import views


app_name = 'web'

urlpatterns = [
    path('deliveries/', views.DeliveryList.as_view(), name='deliveries'),
    path(
        'deliveries/<int:pk>/',
        views.DeliveryDetail.as_view(),
        name='delivery'
    ),
]

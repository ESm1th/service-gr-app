from django.views.generic import (
    ListView,
    DetailView
)
from django.views.generic.edit import ModelFormMixin

from . import models
from . import forms


class DeliveryList(ModelFormMixin, ListView):
    model = models.Delivery
    context_object_name = 'deliveries'
    form_class = forms.DeliveryForm
    object = None


class DeliveryDetail(DetailView):
    model = models.Delivery
    context_object_name = 'delivery'

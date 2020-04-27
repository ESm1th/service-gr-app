from django.views.generic import (
    ListView,
    DetailView
)
from django.views.generic.edit import ModelFormMixin, FormMixin

from . import models
from . import forms


class DeliveryList(ModelFormMixin, ListView):
    model = models.Delivery
    context_object_name = 'deliveries'
    form_class = forms.DeliveryForm
    object = None


class DeliveryDetail(FormMixin, DetailView):
    model = models.Delivery
    context_object_name = 'delivery'
    form_class = forms.HandlingUnitForm

    def get_form(self):
        form = super().get_form()
        instance = self.get_object()
        units = instance.handling_units.count()
        form.fields['number'].initial = units + 1
        return form

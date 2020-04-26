from django.views.generic import (
    ListView,
)
from django.views.generic.edit import ModelFormMixin
from django.core.paginator import Paginator

from . import models
from . import forms


class DeliveryList(ModelFormMixin, ListView):
    model = models.Delivery
    context_object_name = 'deliveries'
    form_class = forms.DeliveryForm
    per_row = 4
    object = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        paginator = Paginator(self.get_queryset(), self.per_row)
        pages = (paginator.page(num) for num in paginator.page_range)
        context.update({'rows': pages})
        return context

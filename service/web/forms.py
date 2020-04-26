from datetime import datetime

from django import forms
from django_select2 import forms as s2forms
from tempus_dominus.widgets import DatePicker, TimePicker

from . import models


class DeliveryForm(forms.ModelForm):
    date = forms.DateField(
        required=True,
        widget=DatePicker(),
        initial=datetime.now().date().strftime('%d-%m-%Y')
    )
    time = forms.TimeField(
        required=True,
        widget=TimePicker(),
        initial=datetime.now().time().strftime('%H:%M:%S')
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name in self.fields.keys():
            self.fields[name].widget.attrs.update(
                {'class': 'form-control shadow-sm'}
            )
            if name == 'client':
                self.fields[name].empty_label = '-'

    class Meta:
        model = models.Delivery
        fields = ('client', 'date', 'time')
        widgets = {'client': s2forms.Select2Widget, }

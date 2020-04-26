from django.db import models, transaction
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


class Base(models.Model):
    """Common fields for models."""
    title = models.CharField(_('title'), max_length=100)
    active = models.BooleanField(_('active'), default=True)
    creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created = models.DateTimeField(_('created'), auto_now_add=True)

    class Meta:
        abstract = True
        ordering = ['created']

    def __str__(self):
        return self.title


class Country(Base):
    """Represents country record in database."""
    class Meta:
        verbose_name = _('country')
        verbose_name_plural = _('countries')


class City(Base):
    """Represents city record in database."""
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = _('city')
        verbose_name_plural = _('cities')


class Client(Base):
    """Represents client record in database."""
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = _('client')
        verbose_name_plural = _('clients')


class Delivery(Base):
    """Represents client delivery record in database."""
    client = models.ForeignKey(
        Client, on_delete=models.CASCADE, related_name='deliveries'
    )
    date = models.DateField(_('date'))
    time = models.TimeField(_('time'))
    units = models.IntegerField(
        _('units quantity'), default=0,
        validators=[MaxValueValidator(50), MinValueValidator(1)]
    )
    title = None

    class Meta:
        verbose_name = _('delivery')
        verbose_name_plural = _('deliveries')

    def __str__(self):
        return f'{self.client} {self.date} / {self.id}'

    def save(self, *args, **kwargs):
        with transaction.atomic():
            super().save(*args, **kwargs)
            units = [
                HandlingUnit(number=num, delivery=self, creator=self.creator)
                for num in range(1, self.units + 1)
            ]
            HandlingUnit.objects.bulk_create(units)


class StorageUnitType(Base):
    """
    Represents storage unit type record in database.
    Something like code `BO2` - wooden boxes or `K32` - small plastic boxes.
    """
    description = models.CharField(
        _('description'), max_length=50, blank=True, null=True
    )

    class Meta:
        verbose_name = _('storage unit type')
        verbose_name_plural = _('storage unit types')

    def __str__(self):
        return self.title.upper()


class HandlingUnit(Base):
    """
    Represents particular storage unit with equipment that was received in
    service center. Handling unit can has many equipment items.
    """
    number = models.IntegerField(
        _('number'), validators=[MaxValueValidator(50), MinValueValidator(1)]
    )
    delivery = models.ForeignKey(
        Delivery, on_delete=models.CASCADE, related_name='handling_units'
    )
    type = models.ForeignKey(
        StorageUnitType, on_delete=models.SET_NULL, null=True
    )
    title = None

    class Meta:
        verbose_name = _('handling unit')
        verbose_name_plural = _('handling units')

    def __str__(self):
        return f'{self.delivery.client}/{self.delivery.id} #{self.number}'


class MaterialType(Base):
    """Represents material type record in database."""
    class Meta:
        verbose_name = _('material type')
        verbose_name_plural = _('material types')


class Material(Base):
    """Represents material record in database."""
    number = models.CharField(_('number'), max_length=50, unique=True)
    type = models.ForeignKey(
        MaterialType, on_delete=models.SET_NULL,
        related_name='materials', null=True
    )

    class Meta:
        verbose_name = _('material')
        verbose_name_plural = _('materials')

    def __str__(self):
        return self.number


class Equipment(Base):
    """
    Represents equipment record in database.
    Consist of material and serial number if it exists.
    """
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    serial_number = models.CharField(
        _('serial number'), max_length=50, blank=True, null=True
    )
    handling_unit = models.ForeignKey(
        HandlingUnit, on_delete=models.CASCADE, related_name='equipments'
    )
    title = None

    class Meta:
        verbose_name = _('equipment')
        verbose_name_plural = _('equipments')

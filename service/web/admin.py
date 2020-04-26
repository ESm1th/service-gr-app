from django.contrib import admin

from . import models


class BaseModelAdmin(admin.ModelAdmin):
    """Common interface, fields for all admin classes."""
    readonly_fields = ('id', 'creator', 'created', )
    list_display = ('title', 'creator', 'created', )

    def save_model(self, request, obj, form, change):
        obj.creator = request.user
        super().save_model(request, obj, form, change)


@admin.register(models.Country)
class CountryAdmin(BaseModelAdmin):
    pass


@admin.register(models.City)
class CityAdmin(BaseModelAdmin):
    list_display = ('title', 'country', 'creator', 'created', )


@admin.register(models.Client)
class ClientAdmin(BaseModelAdmin):
    list_display = ('title', 'city', 'creator', 'created', )


@admin.register(models.Delivery)
class ClientAdmin(BaseModelAdmin):
    list_display = ('client', 'date', 'time', 'creator', 'created', )


@admin.register(models.StorageUnitType)
class StorageUnitTypeAdmin(BaseModelAdmin):
    list_display = ('title', 'description', 'creator', 'created', )


@admin.register(models.HandlingUnit)
class HanlingUnitAdmin(BaseModelAdmin):
    list_display = ('delivery', 'type', 'creator', 'created', )


@admin.register(models.MaterialType)
class MaterialTypeAdmin(BaseModelAdmin):
    list_display = ('title', 'creator', 'created', )


@admin.register(models.Material)
class MaterialAdmin(BaseModelAdmin):
    list_display = ('number', 'title', 'type', 'creator', 'created', )


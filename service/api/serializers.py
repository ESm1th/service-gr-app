from rest_framework.serializers import ModelSerializer

from . import models


class CountrySerializer(ModelSerializer):
    class Meta:
        model = models.Country
        fields = ('id', 'title')


class CitySerializer(ModelSerializer):
    class Meta:
        model = models.City
        fields = ('id', 'title')


class ClientSerializer(ModelSerializer):
    class Meta:
        model = models.Client
        fields = ('id', 'title')


class DeliverySerializer(ModelSerializer):
    client = ClientSerializer()

    class Meta:
        model = models.Delivery
        fields = ('id', 'date', 'time', 'client')


class StorageUnitTypeSerializer(ModelSerializer):
    class Meta:
        model = models.StorageUnitType
        fields = ('id', 'title')


class HandlingUnitSerializer(ModelSerializer):
    delivery = DeliverySerializer()

    class Meta:
        model = models.HandlingUnit
        fields = ('id', 'type', 'delivery')


class MaterialTypeSerializer(ModelSerializer):
    class Meta:
        model = models.MaterialType
        fields = ('id', 'title')


class MaterialSerializer(ModelSerializer):
    type = MaterialTypeSerializer()

    class Meta:
        model = models.Material
        fields = ('id', 'number', 'type')


class EquipmentSerializer(ModelSerializer):
    material = MaterialSerializer()
    hanling_unit = HandlingUnitSerializer()

    class Meta:
        model = models.Equipment
        fiels = ('id', 'material', 'serial_number', 'handling_unit')

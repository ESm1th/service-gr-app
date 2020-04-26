from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView
)
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer

from web import models
from . import serializers


class CreatorMixin:
    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)


class CountryListCreate(CreatorMixin, ListCreateAPIView):
    queryset = models.Country.objects.all()
    serializer_class = serializers.CountrySerializer


class CountryRetriveUpdateDelete(RetrieveUpdateDestroyAPIView):
    queryset = models.Country.objects.all()
    serializer_class = serializers.CountrySerializer


class CityListCreate(CreatorMixin, ListCreateAPIView):
    queryset = models.Country.objects.all()
    serializer_class = serializers.CountrySerializer


class CityRetriveUpdateDelete(RetrieveUpdateDestroyAPIView):
    queryset = models.City.objects.all()
    serializer_class = serializers.CitySerializer


class ClientListCreate(CreatorMixin, ListCreateAPIView):
    queryset = models.Client.objects.all()
    serializer_class = serializers.CountrySerializer


class ClientRetriveUpdateDelete(RetrieveUpdateDestroyAPIView):
    queryset = models.Client.objects.all()
    serializer_class = serializers.ClientSerializer


class DeliveryListCreate(CreatorMixin, ListCreateAPIView):
    queryset = models.Delivery.objects.all()
    serializer_class = serializers.DeliverySerializer
    renderer_classes = [JSONRenderer, TemplateHTMLRenderer, ]

    def post(self, request, format=None, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        if request.accepted_renderer.format == 'html':
            delivery = self.get_queryset().get(id=response.data['id'])
            response.data = {'delivery': delivery, }
            response.template_name = 'web/includes/delivery_card_include.html'
        return response


class DeliveryRetriveUpdateDelete(RetrieveUpdateDestroyAPIView):
    queryset = models.Delivery.objects.all()
    serializer_class = serializers.DeliverySerializer


class StorageUnitTypeListCreate(CreatorMixin, ListCreateAPIView):
    queryset = models.StorageUnitType.objects.all()
    serializer_class = serializers.StorageUnitTypeSerializer


class StorageUnitTypeRetriveUpdateDelete(RetrieveUpdateDestroyAPIView):
    queryset = models.StorageUnitType.objects.all()
    serializer_class = serializers.StorageUnitTypeSerializer


class HandlingUnitListCreate(CreatorMixin, ListCreateAPIView):
    queryset = models.HandlingUnit.objects.all()
    serializer_class = serializers.HandlingUnitSerializer


class HandlingUnitRetriveUpdateDelete(RetrieveUpdateDestroyAPIView):
    queryset = models.HandlingUnit.objects.all()
    serializer_class = serializers.HandlingUnitSerializer


class MaterialTypeListCreate(CreatorMixin, ListCreateAPIView):
    queryset = models.MaterialType.objects.all()
    serializer_class = serializers.MaterialTypeSerializer


class MaterialTypeRetriveUpdateDelete(RetrieveUpdateDestroyAPIView):
    queryset = models.MaterialType.objects.all()
    serializer_class = serializers.MaterialTypeSerializer


class MaterialListCreate(CreatorMixin, ListCreateAPIView):
    queryset = models.Material.objects.all()
    serializer_class = serializers.MaterialSerializer


class MaterialRetriveUpdateDelete(RetrieveUpdateDestroyAPIView):
    queryset = models.Material.objects.all()
    serializer_class = serializers.MaterialSerializer


class EquipmentListCreate(CreatorMixin, ListCreateAPIView):
    queryset = models.Equipment.objects.all()
    serializer_class = serializers.EquipmentSerializer


class EquipmentRetriveUpdateDelete(RetrieveUpdateDestroyAPIView):
    queryset = models.Equipment.objects.all()
    serializer_class = serializers.EquipmentSerializer

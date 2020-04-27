from datetime import datetime
from uuid import uuid4

import pytest

from .. import models


pytestmark = pytest.mark.django_db


@pytest.fixture
def country():
    return models.Country.objects.create(title='Germany')


@pytest.fixture
def city(country):
    return models.City.objects.create(title='Munich', country=country)


@pytest.fixture
def client(city):
    return models.Client.objects.create(title='Siemens', city=city)


@pytest.fixture
def delivery(client):
    return models.Delivery.objects.create(
        client=client,
        date=datetime.now().date(),
        time=datetime.now().time()
    )


@pytest.fixture
def storage_unit_type():
    return models.StorageUnitType.objects.create(
        title='B01',
        description='Big wooden boxes'
    )


@pytest.fixture
def handling_unit(delivery, storage_unit_type):
    return models.HandlingUnit.objects.create(
        number=1,
        delivery=delivery,
        type=storage_unit_type
    )


@pytest.fixture
def material_type():
    return models.MaterialType.objects.create(title='Brake units')


@pytest.fixture
def material(material_type):
    return models.Material.objects.create(
        number=uuid4().hex,
        type=material_type
    )


@pytest.fixture
def equipment(handling_unit, material):
    return models.Equipment.objects.create(
        material=material,
        serial_number=uuid4().hex,
        handling_unit=handling_unit
    )


def test_handling_unit_in_delivery(delivery, storage_unit_type):
    handling_unit = models.HandlingUnit.objects.create(
        number=1,
        delivery=delivery,
        type=storage_unit_type
    )
    assert handling_unit in delivery.handling_units.all()
    assert delivery.handling_units.count() == 1


def test_material_in_delivery(
    delivery,
    material,
    handling_unit,
    equipment
):
    unit = delivery.handling_units.get(id=handling_unit.id)
    equipment = unit.equipment.first()
    assert equipment.material.number == material.number

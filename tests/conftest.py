# -*- coding: utf-8 -*-
import os
import sys

import pytest
from faker import Faker

local_path = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(local_path, '..'))
from src.vehicle import VehicleProvider  # noqa

@pytest.fixture(scope='module')
def fake():
    fixture = Faker()
    fixture.add_provider(VehicleProvider)
    return fixture

@pytest.fixture
def vehicles():
    from src.vehicle.vehicle_dict import vehicles as vd
    fixture = vd
    return fixture

@pytest.fixture
def years():
    from src.vehicle.vehicle_dict import vehicles as vd
    year_dict = []
    for veh in vd:
        year_dict.append(int(veh['Year']))
    year_dict = list(set(year_dict))
    fixture = year_dict
    return fixture

@pytest.fixture
def models():
    from src.vehicle.vehicle_dict import vehicles as vd
    model_dict = []
    for veh in vd:
        model_dict.append(veh['Model'])
    model_dict = list(set(model_dict))
    fixture = model_dict
    return fixture

@pytest.fixture
def categories():
    from src.vehicle.vehicle_dict import vehicles as vd
    cat_dict = []
    for veh in vd:
        cat_dict.append(veh['Category'])
    cat_dict = list(set(cat_dict))
    fixture = cat_dict
    return fixture

@pytest.fixture
def makes():
    from src.vehicle.vehicle_dict import vehicles as vd
    make_dict = []
    for veh in vd:
        make_dict.append(veh['Make'])
    make_dict = list(set(make_dict))
    fixture = make_dict
    return fixture
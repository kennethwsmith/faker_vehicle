# -*- coding: utf-8 -*-
import os
import pytest
import sys

from faker import Faker

local_path = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(local_path, '..'))
from src.vehicle import VehicleProvider  # noqa

@pytest.fixture(scope='module')
def fake():
    fixture = Faker()
    fixture.add_provider(VehicleProvider)
    return fixture
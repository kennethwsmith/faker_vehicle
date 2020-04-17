# -*- coding: utf-8 -*-
import re
import pytest
from faker import Faker
from faker_vehicle import VehicleProvider  # noqa
from src.vehicle.vehicle_dict import vehicles

fake = Faker()
fake.add_provider(VehicleProvider)

def test_make():
    make_list = []
    for vehicle in vehicles:
        make_list.append(vehicle['Make'])
    make_list = list(set(make_list))
    make = fake.vehicle_make()
    assert len(make) > 1
    assert make in make_list

def test_year():
    year_list = []
    for vehicle in vehicles:
        year_list.append(vehicle['Year'])
    year_list = list(set(year_list))
    year = fake.vehicle_year()
    assert len(year) > 1
    assert int(year) in year_list

def test_model():
    model_list = []
    for vehicle in vehicles:
        model_list.append(vehicle['Model'])
    model_list = list(set(model_list))
    model = fake.vehicle_model()
    assert len(model) > 1
    assert model in model_list

def test_category():
    category_list = []
    for vehicle in vehicles:
        category_list.append(vehicle['Category'])
    category_list = list(set(category_list))
    category = fake.vehicle_category()
    assert len(category) > 1
    assert category in category_list

def test_vehicle_make_model():
    ar_mm = fake.vehicle_make_model().split()
    assert len(ar_mm) >= 1 # check to see if there are 2 words

def test_vehicle_year_make_model():
    ar_ymm = fake.vehicle_year_make_model().split()
    assert len(ar_ymm) >= 2 # check to see if there are 3 words
    assert float(ar_ymm[0]).is_integer() # check to see if first word is a number (year)

def test_vehicle_year_make_model_cat():
    ar_ymmc = fake.vehicle_year_make_model_cat().split()
    assert len(ar_ymmc) >= 3 # check to see if there are 4 words
    assert float(ar_ymmc[0]).is_integer() # check to see if first word is a number (year)
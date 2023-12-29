# -*- coding: utf-8 -*-

def test_vehicles(fake, vehicles):
    assert len(vehicles) > 1
    v = vehicles[0]
    assert 'Make' in v.keys()
    assert 'Model' in v.keys()


def test_make(fake, makes):
    make = fake.vehicle_make()
    assert len(make) > 1
    assert make in makes


def test_year(fake, years):
    year = fake.vehicle_year()
    assert len(year) > 1
    assert int(year) in years


def test_model(fake, models):
    model = fake.vehicle_model()
    assert len(model) >= 1
    assert model in models


def test_category(fake, categories):
    category = fake.vehicle_category()
    assert len(category) > 1
    assert category in categories


def test_vehicle_make_model(fake):
    ar_mm = fake.vehicle_make_model().split()
    # check to see if there are 2 words
    assert len(ar_mm) >= 1

def test_vehicle_make_model_cat(fake):
    ar_ymmc = fake.vehicle_make_model_cat().split()
    # check to see if there are 3 words
    assert len(ar_ymmc) >= 2

def test_vehicle_year_make_model(fake):
    ar_ymm = fake.vehicle_year_make_model().split()
    # check to see if there are 3 words
    assert len(ar_ymm) >= 2
    # check to see if first word is a number (year)
    assert float(ar_ymm[0]).is_integer()


def test_vehicle_year_make_model_cat(fake):
    ar_ymmc = fake.vehicle_year_make_model_cat().split()
    # check to see if there are 4 words
    assert len(ar_ymmc) >= 3
    # check to see if first word is a number (year)
    assert float(ar_ymmc[0]).is_integer()

# -*- coding: utf-8 -*-

def test_machinery(fake, machinery):
    assert len(machinery) > 1
    v = machinery[0]
    assert 'Make' in v.keys()
    assert 'Model' in v.keys()


def test_seeded_machine_object():
    from faker import Faker
    from src.vehicle import VehicleProvider

    def get_seeded_machine_object(fake, seed=1):
        fake.seed_instance(seed)
        return fake.machine_object()

    fake = Faker()
    fake.add_provider(VehicleProvider)
    models = [get_seeded_machine_object(fake) for _ in range(2)]

    assert all(m == models[0] for m in models)


def test_make(fake, machine_makes):
    make = fake.machine_make()
    assert len(make) > 1
    assert make in machine_makes


def test_year(fake, machine_years):
    year = fake.machine_year()
    assert len(year) > 1
    assert int(year) in machine_years


def test_model(fake, machine_models):
    model = fake.machine_model()
    assert len(model) >= 1
    assert model in machine_models


def test_category(fake, machine_categories):
    category = fake.machine_category()
    assert len(category) > 1
    assert category in machine_categories


def test_machine_make_model(fake):
    ar_mm = fake.machine_make_model().split()
    # check to see if there are 2 words
    assert len(ar_mm) >= 1


def test_machine_make_model_cat(fake):
    ar_ymmc = fake.machine_make_model_cat().split()
    # check to see if there are 3 words
    assert len(ar_ymmc) >= 2


def test_machine_year_make_model(fake):
    ar_ymm = fake.machine_year_make_model().split()
    # check to see if there are 3 words
    assert len(ar_ymm) >= 2
    # check to see if first word is a number (year)
    assert float(ar_ymm[0]).is_integer()


def test_machine_year_make_model_cat(fake):
    ar_ymmc = fake.machine_year_make_model_cat().split()
    # check to see if there are 4 words
    assert len(ar_ymmc) >= 3
    # check to see if first word is a number (year)
    assert float(ar_ymmc[0]).is_integer()

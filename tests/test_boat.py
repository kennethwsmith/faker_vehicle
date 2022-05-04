# -*- coding: utf-8 -*-

def test_boat_format(fake):
    template = "banana {Year} apple ({Make})"
    formattedString = fake.boat_format(template)
    assert len(formattedString.split(" ")) >= 4
    for word in template.split(" "):
        if not word.find("{"):
            assert formattedString.find("word")

def test_boat_make(fake, boat_makes):
    make = fake.boat_make()
    assert len(make) > 1
    assert make in boat_makes

def test_boat_year(fake, boat_years):
    year = fake.boat_year()
    assert len(year) > 1
    assert int(year) in boat_years

def test_boat_model(fake, boat_models):
    model = fake.boat_model()
    assert len(model) >= 1
    assert model in boat_models

def test_boat_category(fake, boat_categories):
    category = fake.boat_category()
    assert len(category) > 1
    assert category in boat_categories

def test_boat_make_model(fake):
    ar_mm = fake.boat_make_model().split()
    # check to see if there are 2 words
    assert len(ar_mm) >= 1

def test_boat_year_make_model(fake):
    ar_ymm = fake.boat_year_make_model().split()
    # check to see if there are 3 words
    assert len(ar_ymm) >= 2
    # check to see if first word is a number (year)
    assert float(ar_ymm[0]).is_integer()

def test_boat_year_make_model_cat(fake):
    ar_ymmc = fake.boat_year_make_model_cat().split()
    # check to see if there are 4 words
    assert len(ar_ymmc) >= 3
    # check to see if first word is a number (year)
    assert float(ar_ymmc[0]).is_integer()

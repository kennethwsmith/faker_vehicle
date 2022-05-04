faker_vehicle
=============

 |pypi| |unix_build| |coverage| |license|

faker_vehicle is a provider for the `Faker`_ Python package.

It provides vehicle and machinery related fake data for testing purposes:

* Vehicle
    * Make
    * Model
    * Make / Model
    * Make / Model / Year
    * Make / Model / Category
    * Year
    * Formatter (pass in the format using string.format() syntax)
    * Object (just an object you can use)
* Machinery
    * Make
    * Model
    * Make / Model
    * Make / Model / Year
    * Make / Model / Category
    * Year
    * Formatter (pass in the format using string.format() syntax)
    * Object (just an object you can use)
* Boats
    * Make
    * Model
    * Make / Model
    * Make / Model / Year
    * Make / Model / Category
    * Year
    * Formatter (pass in the format using string.format() syntax)
    * Object (just an object you can use)

Usage
-----

Install with pip:

.. code:: bash

    pip install faker_vehicle

Or install with setup.py

.. code:: bash

    git clone https://github.com/kennethwsmith/faker_vehicle.git
    cd faker_vehicle && python setup.py install

Add the ``VehicleProvider`` to your ``Faker`` instance:

.. code:: python

    from faker import Faker
    from faker_vehicle import VehicleProvider

    fake = Faker()
    fake.add_provider(VehicleProvider)

    # VEHICLES

    print(fake.vehicle_format("My favorite {Category} is a {Model} by {Make} from {Year}"))
    # My favorite Truck is a F150 SuperCrew Cab by Ford from 2020
    print(fake.vehicle_year_make_model())
    # 2014 Volkswagen Golf
    print(fake.vehicle_year_make_model_cat())
    # 1996 Dodge Ram Wagon 1500 (Van/Minivan)
    print(fake.vehicle_make_model())
    # Volvo V40
    print(fake.vehicle_make())
    # BMW
    print(fake.vehicle_model())
    # SL
    print(fake.vehicle_year())
    # 2008
    print(fake.vehicle_category())
    # Wagon
    print(json.dumps(fake.vehicle_object()))
    # {"Year": 1996, "Make": "Chrysler", "Model": "New Yorker", "Category": "Sedan"}
    
    # MACHINERY

    print(fake.machine_format("My favorite {Category} is a {Model} by {Make} from {Year}"))
    # My favorite Wheel Loader is a 304H Waste Handler by John Deere from 2016
    print(fake.machine_year_make_model())
    # 2008 Caterpillar 5511C
    print(fake.machine_year_make_model_cat())
    # 2008 Caterpillar 5511C (Feller Buncher)
    print(fake.machine_make_model())
    # Caterpillar 5511C
    print(fake.machine_make())
    # Caterpillar
    print(fake.machine_model())
    # 5511C
    print(fake.machine_year())
    # 2008
    print(fake.machine_category())
    # Feller Buncher 
    print(json.dumps(fake.machine_object()))
    # {"Year": 2008, "Make": "Caterpillar", "Model": "5511C", "Category": "Feller Buncher"}

    # BOATS
    
    print(fake.boat_format("My favorite {Category} is a {Model} by {Make} from {Year}"))
    # My favorite Sailboat is a Jack Salmon 14 by Aeromarine from 1967 
    print(fake.boat_year_make_model())
    # 2003 Apex Inflatables Panga Sportfish
    print(fake.boat_year_make_model_cat())
    # 1979 Albin Marine Inc. Scampi 30 (Sailboat)
    print(fake.boat_make_model())
    # Caterpillar 5511C
    print(fake.boat_make())
    # Adventure
    print(fake.boat_model())
    # Success 200
    print(fake.boat_year())
    # 2008
    print(fake.boat_category())
    # Sailboat 
    print(json.dumps(fake.boat_object()))
    # {"Year": "2003", "Make": "Active Thunder Boats", "Model": "42 AVH", "Category": "Inboard"}

.. |pypi| image:: https://img.shields.io/pypi/v/faker_vehicle.svg?style=flat-square&label=version
    :target: https://pypi.python.org/pypi/faker_vehicle
    :alt: Latest version released on PyPi

.. |unix_build| image:: https://img.shields.io/travis/kennethwsmith/faker_vehicle/master.svg?style=flat-square&label=unix%20build
    :target: http://travis-ci.org/kennethwsmith/faker_vehicle
    :alt: Build status of the master branch on Mac/Linux

.. |coverage| image:: https://img.shields.io/coveralls/kennethwsmith/faker_vehicle/master.svg?style=flat-square
    :target: https://coveralls.io/r/kennethwsmith/faker_vehicle?branch=master
    :alt: Test coverage

.. |license| image:: https://img.shields.io/badge/license-apache-blue.svg?style=flat-square
    :target: https://github.com/kennethwsmith/faker_vehicle/blob/master/LICENSE
    :alt: Apache license version 2.0

.. _Faker: https://github.com/joke2k/faker

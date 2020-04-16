faker_vehicle
=============

 |pypi| |unix_build| |coverage| |license|

faker_vehicle is a provider for the `Faker`_ Python package.

It provides vehicle related fake data for testing purposes:

    * Vehicle Make
    * Vehicle Model
    * Vehicle Make / Model
    * Vehicle Make / Model / Year
    * Vehicle Make / Model / Category
    * Vehicle Year
    * Vehicle Object (you can format)

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

    fake.vehicle_year_make_model()
    # 2014 Volkswagen Golf
    fake.vehicle_year_make_model_cat()
    # 1996 Dodge Ram Wagon 1500 (Van/Minivan)
    fake.vehicle_make_model()
    # Volvo V40
    fake.vehicle_make()
    # BMW
    fake.vehicle_model()
    # SL
    fake.vehicle_year()
    # 2008
    fake.vehicle_category()
    # Wagon
    json.dumps(fake.vehicle_object())
    # {"Year": 1996, "Make": "Chrysler", "Model": "New Yorker", "Category": "Sedan"}
    
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

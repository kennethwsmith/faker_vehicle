faker_vehicle
=========

 |pypi| |unix_build| |coverage| |license|

faker_vehicle is a provider for the `Faker`_ Python package.

It provides web-related fake data for testing purposes:

   * Content-type http header.
   * Popular web server version tokens/signatures.


Usage
-----

Install with pip:

.. code:: bash

    pip install faker_vehicle

Or install with setup.py

.. code:: bash

    git clone https://github.com/kennethwsmith/faker_vehicle.git
    cd faker_vehicle && python setup.py install

Add the ``WebProvider`` to your ``Faker`` instance:

.. code:: python

    from faker import Faker
    from faker_vehicle import WebProvider

    fake = Faker()
    fake.add_provider(WebProvider)

    fake.content_type()
    # application/mxf
    fake.content_type_popular()
    # text/html
    fake.server_token()
    # Apache/2.0.51 (Ubuntu)


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

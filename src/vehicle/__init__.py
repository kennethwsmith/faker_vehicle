# -*- coding: utf-8 -*-

from random import choice
from random import randint
from faker.providers import BaseProvider
from .vehicle_dict import vehicles
from .machine_dict import machinery
from .boat_data import boats

class VehicleProvider(BaseProvider):
    """
    A Provider for vehicle related test data.

    >>> from faker import Faker
    >>> from faker_vehicle import VehicleProvider
    >>> fake = Faker()
    >>> fake.add_provider(VehicleProvider)
    """

    def vehicle_object(self):
        """
        Returns a random vehicle dict example:
        {"Year": 2008, "Make": "Jeep", "Model": "Wrangler", "Category": "SUV"}
        """
        veh = choice(vehicles)
        return veh

    def vehicle_format(self,formatString):
        vehicle = self.vehicle_object()
        vehicleString = formatString.format(Year=vehicle.get('Year'),Make=vehicle.get('Make'),Category=vehicle.get('Category'),Model=vehicle.get('Model'))
        return vehicleString

    def vehicle_year_make_model(self):
        """Returns Year Make Model example: 1997 Nissan 240SX"""
        veh = self.vehicle_object()
        year = veh.get('Year')
        make = veh.get('Make')
        model = veh.get('Model')
        return str(year) + ' ' + make + ' ' + model

    def vehicle_year_make_model_cat(self):
        """
        Returns Year Make Model Cat example:
        2017 GMC Sierra 1500 Double Cab (Pickup)
        """
        veh = self.vehicle_object()
        year = veh.get('Year')
        make = veh.get('Make')
        model = veh.get('Model')
        cat = veh.get('Category')
        return str(year) + ' ' + make + ' ' + model + ' (' + cat + ')'

    def vehicle_make_model(self):
        """Returns Make Model example: Audi Q7"""
        veh = self.vehicle_object()
        make = veh.get('Make')
        model = veh.get('Model')
        return make + ' ' + model

    def vehicle_make(self):
        """Returns Make example: Lincoln"""
        veh = self.vehicle_object()
        return veh.get('Make')

    def vehicle_year(self):
        """Returns Year example: 1999"""
        veh = self.vehicle_object()
        return str(veh.get('Year'))

    def vehicle_model(self):
        """Returns Model example: Frontier King Cab"""
        veh = self.vehicle_object()
        return veh.get('Model')

    def vehicle_category(self):
        """Returns Category example: SUV"""
        veh = self.vehicle_object()
        return veh.get('Category')

    def machine_object(self):
        """
        Returns a random machine dict example:
        {"Year": 2008, "Make": "Caterpillar", "Model": "5511C", "Category": "Feller Buncher"}
        """
        machine = choice(machinery)
        return machine

    def machine_format(self,formatString):
        machine = self.machine_object()
        machineString = formatString.format(Year=machine.get('Year'),Make=machine.get('Make'),Category=machine.get('Category'),Model=machine.get('Model'))
        return machineString

    def machine_year_make_model(self):
        """Returns Year Make Model example: 2008 Caterpillar 5511C"""
        machine = self.machine_object()
        year = machine.get('Year')
        make = machine.get('Make')
        model = machine.get('Model')
        return str(year) + ' ' + make + ' ' + model

    def machine_year_make_model_cat(self):
        """
        Returns Year Make Model Cat example:
        2008 Caterpillar 5511C (Feller Buncher)
        """
        machine = self.machine_object()
        year = machine.get('Year')
        make = machine.get('Make')
        model = machine.get('Model')
        cat = machine.get('Category')
        return str(year) + ' ' + make + ' ' + model + ' (' + cat + ')'

    def machine_make_model(self):
        """Returns Make Model example: Caterpillar 5511C"""
        machine = self.machine_object()
        make = machine.get('Make')
        model = machine.get('Model')
        return make + ' ' + model

    def machine_make(self):
        """Returns Make example: Caterpillar"""
        machine = self.machine_object()
        return machine.get('Make')

    def machine_year(self):
        """Returns Year example: 2008"""
        machine = self.machine_object()
        return str(machine.get('Year'))

    def machine_model(self):
        """Returns Model example: 5511C"""
        machine = self.machine_object()
        return machine.get('Model')

    def machine_category(self):
        """Returns Category example: Feller Buncher"""
        machine = self.machine_object()
        return machine.get('Category')

    def boat_object(self):
        """
        Returns a random boat example:
        {"Year": 2008, "Make": "AB Inflatables", "Model": "10 ALX", "Category": "Outboard"}
        """
        boatMakeIndex = randint(0,len(boats['makes'])-1)
        boatMake = boats['makes'][boatMakeIndex]['make']
        boatCatIndex = randint(0,len(boats['makes'][boatMakeIndex]['cats'])-1)
        boatCat = boats['makes'][boatMakeIndex]['cats'][boatCatIndex]['cat']
        boatYearIndex = randint(0,len(boats['makes'][boatMakeIndex]['cats'][boatCatIndex]['years'])-1)
        boatYear = boats['makes'][boatMakeIndex]['cats'][boatCatIndex]['years'][boatYearIndex]['year']
        boatModelIndex = randint(0,len(boats['makes'][boatMakeIndex]['cats'][boatCatIndex]['years'][boatYearIndex]['models'])-1)
        boatModel = boats['makes'][boatMakeIndex]['cats'][boatCatIndex]['years'][boatYearIndex]['models'][boatModelIndex]
        boat = {"Year": boatYear, "Make": boatMake, "Model": boatModel, "Category": boatCat}
        return boat

    def boat_format(self,formatString):
        boat = self.boat_object()
        boatString = formatString.format(Year=boat.get('Year'),Make=boat.get('Make'),Category=boat.get('Category'),Model=boat.get('Model'))
        return boatString

    def boat_model(self):
        """Returns Model example: 5511C"""
        boat = self.boat_object()
        return boat.get('Model')

    def boat_year_make_model(self):
        """Returns Year Make Model example: """
        boat = self.boat_object()
        year = boat.get('Year')
        make = boat.get('Make')
        model = boat.get('Model')
        return str(year) + ' ' + make + ' ' + model

    def boat_year_make_model_cat(self):
        """
        Returns Year Make Model Cat example:
        2008 Caterpillar 5511C (Feller Buncher)
        """
        boat = self.boat_object()
        year = boat.get('Year')
        make = boat.get('Make')
        model = boat.get('Model')
        cat = boat.get('Category')
        return str(year) + ' ' + make + ' ' + model + ' (' + cat + ')'

    def boat_make_model(self):
        """Returns Make Model example: Caterpillar 5511C"""
        boat = self.boat_object()
        make = boat.get('Make')
        model = boat.get('Model')
        return make + ' ' + model

    def boat_make(self):
        """Returns Make example: Caterpillar"""
        boat = self.boat_object()
        return boat.get('Make')

    def boat_year(self):
        """Returns Year example: 2008"""
        boat = self.boat_object()
        return str(boat.get('Year'))

    def boat_category(self):
        """Returns Category example: Feller Buncher"""
        boat = self.boat_object()
        return boat.get('Category')       
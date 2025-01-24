import random

from .BuildingBase import BuildingBase
from .BuildingFactory import BuildingFactory
from .BuildingParkingLot import BuildingParkingLot
from .ResourceCoal import ResourceCoal
from .ResourceIron import ResourceIron
from .ResourceSteelPlate import ResourceSteelPlate
from .VehicleTruck import VehicleTruck
from .VehicleFactory import VehicleFactory


class GameLogic:

    def __init__(self):
        self.buildings: list[BuildingBase] = []
        self.vehicles: list[VehicleTruck] = []

    def initialize_game_field(self):
        factory_types = [ResourceCoal, ResourceCoal, ResourceIron, ResourceSteelPlate]
        for i, factory_type in enumerate(factory_types):
            current_factory = BuildingFactory(factory_type)
            current_factory.set_position((i + 1) * 100, ((i + 1) % 3) * 100)
            self.buildings.append(current_factory)

        new_parking_lot = BuildingParkingLot()
        self.buildings.append(new_parking_lot)

        self.vehicles += VehicleFactory().create_vehicles(
            new_parking_lot.position_x,
            new_parking_lot.position_y,
            self.buildings,
            3
        )

        '''
        for i in range(3):
            new_vehicle_truck = VehicleTruck()
            new_vehicle_truck.set_position(new_parking_lot.position_x, new_parking_lot.position_y)
            new_vehicle_truck.set_destination(random.choice(self.buildings))
            self.vehicles.append(new_vehicle_truck)
        '''

    def game_tick(self):
        self.process_buildings()
        self.move_vehicles()
        self.galaxy_express()

    def process_buildings(self):
        for building in self.buildings:
            building.process()

    def move_vehicles(self):
        for vehicle in self.vehicles:
            vehicle.move()

    def galaxy_express(self):
        for vehicle in self.vehicles:
            if not vehicle.has_destination():
                vehicle.set_destination(random.choice(self.buildings))


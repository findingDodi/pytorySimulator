import random

from .BuildingBase import BuildingBase
from .BuildingFactory import BuildingFactory
from .BuildingParkingLot import BuildingParkingLot
from .VehicleTruck import VehicleTruck


class GameLogic:

    def __init__(self):
        self.buildings: list[BuildingBase] = []
        self.vehicles: list[VehicleTruck] = []

    def initialize_game_field(self):
        for i in range(5):
            current_factory = BuildingFactory()
            current_factory.set_position((i + 1) * 100, (i + 1) * 100)
            self.buildings.append(current_factory)

        new_parking_lot = BuildingParkingLot()
        new_vehicle_truck = VehicleTruck()
        new_vehicle_truck.set_position(new_parking_lot.position_x, new_parking_lot.position_y)
        new_vehicle_truck.set_destination(random.choice(self.buildings))

        self.buildings.append(new_parking_lot)
        self.vehicles.append(new_vehicle_truck)

    def game_tick(self):
        self.move_vehicles()
        self.galaxy_express()

    def move_vehicles(self):
        for vehicle in self.vehicles:
            vehicle.move()

    def galaxy_express(self):
        for vehicle in self.vehicles:
            if not vehicle.has_destination():
                vehicle.set_destination(random.choice(self.buildings))


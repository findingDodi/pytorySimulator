from .VehicleTruck import VehicleTruck
import random


class VehicleFactory:

    @staticmethod
    def create_vehicle(position_x, position_y, building):
        new_vehicle_truck = VehicleTruck()
        new_vehicle_truck.set_position(position_x, position_y)
        new_vehicle_truck.set_destination(building)
        return new_vehicle_truck

    @staticmethod
    def create_vehicles(position_x, position_y, buildings, amount):
        vehicles = []
        for i in range(amount):
            vehicles.append(VehicleFactory.create_vehicle(
                position_x,
                position_y,
                random.choice(buildings)
            ))

        return vehicles

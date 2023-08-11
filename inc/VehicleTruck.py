from __future__ import annotations
import math

from .BuildingBase import BuildingBase


class VehicleTruck:

    global_vehicle_id = 0

    @staticmethod
    def get_next_vehicle_id():
        VehicleTruck.global_vehicle_id += 1
        return VehicleTruck.global_vehicle_id

    def __init__(self):
        self.id = VehicleTruck.get_next_vehicle_id()
        self.width = 10
        self.height = 10
        self.position_x = 0
        self.position_y = 0
        self.color = (50, 100, 220)
        self.item_slots = []
        self.items_max = 10
        self.speed = 5
        self.destination: BuildingBase | None = None

    def add_item(self, item):
        if len(self.item_slots) >= self.items_max:
            return False

        self.item_slots.append(item)
        return True

    def get_item(self):
        if not self.item_slots:
            return None

        return self.item_slots.pop()

    def get_payload_type(self):
        if not self.item_slots:
            return None

        return type(self.item_slots[0])

    def set_position(self, x, y):
        self.position_x = x
        self.position_y = y

    def set_destination(self, destination, enforce=False):
        if self.destination is None or enforce:
            self.destination = destination
            return True

        return False

    def get_rect(self):
        return (self.position_x, self.position_y, self.width, self.height)

    def has_destination(self):
        return self.destination is not None

    def move(self):
        if not self.destination:
            return

        if (self.position_x, self.position_y) == (self.destination.position_x, self.destination.position_y):
            # print("You arrived at your destination!", self.id)
            self.destination = None
            return

        move_x = 0
        move_y = 0

        if self.position_x < self.destination.position_x:
            move_x += 1
        elif self.position_x > self.destination.position_x:
            move_x -= 1

        if self.position_y < self.destination.position_y:
            move_y += 1
        elif self.position_y > self.destination.position_y:
            move_y -= 1

        vector_length = math.sqrt(move_x ** 2 + move_y ** 2)
        move_x *= self.speed / vector_length
        move_y *= self.speed / vector_length

        target_position_x = self.position_x + move_x
        target_position_y = self.position_y + move_y

        if self.position_x < self.destination.position_x:
            target_position_x = min(target_position_x, self.destination.position_x)
        elif self.position_x > self.destination.position_x:
            target_position_x = max(target_position_x, self.destination.position_x)

        if self.position_y < self.destination.position_y:
            target_position_y = min(target_position_y, self.destination.position_y)
        elif self.position_y > self.destination.position_y:
            target_position_y = max(target_position_y, self.destination.position_y)

        self.set_position(target_position_x, target_position_y)

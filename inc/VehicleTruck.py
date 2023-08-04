from __future__ import annotations

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
        self.speed = 1
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
            move_x += self.speed
        elif self.position_x > self.destination.position_x:
            move_x -= self.speed

        if self.position_y < self.destination.position_y:
            move_y += self.speed
        elif self.position_y > self.destination.position_y:
            move_y -= self.speed

        self.set_position(self.position_x + move_x, self.position_y + move_y)

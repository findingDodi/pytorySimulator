from typing import Type

from .BuildingBase import BuildingBase
from .ResourceBase import ResourceBase


class BuildingFactory(BuildingBase):

    def __init__(self, production_task):
        super().__init__()

        self.width = 50
        self.height = 50
        self.color = (200, 150, 100)

        self.item_slots: list[ResourceBase] = []
        self.items_max = 10

        self.production_task: Type[ResourceBase] = production_task
        self.input_resources = {}
        for resource_name in self.production_task.RESOURCES_NEEDED.keys():
            self.input_resources[resource_name] = []

        self._to_produce = 0

    def __str__(self):
        return self.production_task.NAME + ": " + str(len(self.item_slots))

    def __repr__(self):
        return self.__str__()

    def process(self):
        if self.production_task.needs_resources():
            if not self.can_produce():
                return

            for resource_name, amount in self.production_task.RESOURCES_NEEDED.items():
                self.remove_from_input_resources(resource_name, amount)

        self._to_produce += 1.0 / self.production_task.CRAFTING_TIME
        left_over = self._to_produce % 1
        total_production = int(self._to_produce - left_over)
        self.__add_to_stack(total_production)
        self._to_produce = left_over

    def is_full(self):
        return len(self.item_slots) >= self.items_max

    def can_produce(self):
        for resource_name in self.production_task.RESOURCES_NEEDED.keys():
            available = self.get_total_amount_input_resource(resource_name)
            if available < self.production_task.RESOURCES_NEEDED[resource_name]:
                return False

        return True

    def get_total_amount_input_resource(self, resource_name):
        total_amount = 0
        for resource in self.input_resources[resource_name]:
            total_amount += resource.stack_amount

        return total_amount

    def add_to_input_resources(self, resource: ResourceBase):
        self.input_resources[resource.NAME].append(resource)
        # TODO: obey limits

    def remove_from_input_resources(self, resource_name, amount):
        to_remove = amount
        for i in range(len(self.input_resources[resource_name])):
            item_stack: ResourceBase = self.input_resources[resource_name][i]

            if to_remove <= 0:
                break

            if not item_stack.is_empty():
                to_remove = item_stack.remove_from_stack(to_remove)

        for i in range(len(self.input_resources[resource_name]), 0, -1):
            item_stack: ResourceBase = self.input_resources[resource_name][i]
            if item_stack.is_empty():
                self.input_resources[resource_name].pop(i)

    def get_needed_resources(self) -> list:
        needed_resources = []
        for resource_name in self.production_task.RESOURCES_NEEDED.keys():
            order_minimum = 1 + self.production_task.RESOURCES_NEEDED[resource_name]
            if len(self.input_resources[resource_name]) <= order_minimum:
                needed_resources.append(resource_name)

        return needed_resources

    def __add_to_stack(self, amount):
        to_distribute = amount
        for i in range(len(self.item_slots)):
            item_stack = self.item_slots[i]

            if to_distribute <= 0:
                break

            if item_stack.is_full():
                to_distribute = item_stack.add_to_stack(to_distribute)

        if to_distribute <= 0:
            return

        if not self.is_full():
            # TODO: fix to_distribute > stack_size_max bug
            self.item_slots.append(
                self.production_task(to_distribute)
            )

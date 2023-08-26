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
        self._to_produce = 0

    def __str__(self):
        return self.production_task.NAME + ": " + str(len(self.item_slots))

    def __repr__(self):
        return self.__str__()

    def process(self):
        self._to_produce += 1.0 / self.production_task.CRAFTING_TIME
        left_over = self._to_produce % 1
        self.__add_to_stack(int(self._to_produce - left_over))
        self._to_produce = left_over

    def __add_to_stack(self, amount):
        to_distribute = amount  # 2
        for i in range(len(self.item_slots)):
            item_stack = self.item_slots[i]

            if to_distribute <= 0:
                break

            if item_stack.stacked_amount < item_stack.stack_size_max:
                stack_space = item_stack.stack_size_max - item_stack.stacked_amount
                stack_difference = min(stack_space, to_distribute)
                item_stack.stacked_amount += stack_difference
                to_distribute -= stack_difference
                to_distribute = max(to_distribute, 0)

        if to_distribute <= 0:
            return

        if len(self.item_slots) < self.items_max:
            # TODO: fix to_distribute > stack_size_max bug
            self.item_slots.append(
                self.production_task(to_distribute)
            )

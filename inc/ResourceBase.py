

class ResourceBase:

    NAME = "None"
    CRAFTING_TIME = 1
    RESOURCES_NEEDED = {}

    @classmethod
    def needs_resources(cls):
        return len(cls.RESOURCES_NEEDED) > 0

    def __init__(self, stacked_amount=1):
        self.stacked_amount = stacked_amount
        self.stack_size_max = 20

    def is_full(self):
        return self.stacked_amount < self.stack_size_max

    def is_empty(self):
        return self.stacked_amount == 0

    def add_to_stack(self, amount: int) -> int:
        to_distribute = amount
        stack_space = self.stack_size_max - self.stacked_amount
        stack_difference = min(stack_space, to_distribute)
        self.stacked_amount += stack_difference
        to_distribute -= stack_difference
        to_distribute = max(to_distribute, 0)

        return to_distribute

    def remove_from_stack(self, amount: int) -> int:
        to_remove = amount
        if to_remove <= self.stacked_amount:
            self.stacked_amount -= to_remove
            return 0

        rest = to_remove - self.stacked_amount
        self.stacked_amount = 0
        return rest


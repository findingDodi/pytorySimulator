

class ResourceBase:

    NAME = "None"
    CRAFTING_TIME = 1

    def __init__(self, stacked_amount=1):
        self.stacked_amount = stacked_amount
        self.stack_size_max = 20
        self.resources_needed = {}

    def is_full(self):
        return self.stacked_amount < self.stack_size_max

    def add_to_stack(self, amount: int) -> int:
        to_distribute = amount
        stack_space = self.stack_size_max - self.stacked_amount
        stack_difference = min(stack_space, to_distribute)
        self.stacked_amount += stack_difference
        to_distribute -= stack_difference
        to_distribute = max(to_distribute, 0)

        return to_distribute


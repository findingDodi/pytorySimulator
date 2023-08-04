

class ResourceBase:

    NAME = "None"

    def __init__(self, stacked_amount=1):
        self.stacked_amount = stacked_amount
        self.stack_size_max = 20
        self.resources_needed = {}
        self.crafting_time = 1

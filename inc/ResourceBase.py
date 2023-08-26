

class ResourceBase:

    NAME = "None"
    CRAFTING_TIME = 1

    def __init__(self, stacked_amount=1):
        self.stacked_amount = stacked_amount
        self.stack_size_max = 20
        self.resources_needed = {}

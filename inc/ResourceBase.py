

class ResourceBase:

    NAME = "None"

    def __init__(self, stack_size=1):
        self.stack_size = stack_size
        self.stack_size_max = 20
        self.resources_needed = {}
        self.crafting_time = 1

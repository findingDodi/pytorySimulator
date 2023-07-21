from .ResourceBase import ResourceBase
from .ResourceIron import ResourceIron
from .ResourceCoal import ResourceCoal


class ResourceSteelPlate(ResourceBase):

    NAME = "Steel Plate"

    def __init__(self, stack_size=1):
        super().__init__(stack_size)

        self.stack_size_max = 10
        self.resources_needed = {
            ResourceIron.NAME: 1,
            ResourceCoal.NAME: 1
        }
        self.crafting_time = 2

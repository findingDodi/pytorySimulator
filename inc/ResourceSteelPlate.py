from .ResourceBase import ResourceBase
from .ResourceIron import ResourceIron
from .ResourceCoal import ResourceCoal


class ResourceSteelPlate(ResourceBase):

    NAME = "Steel Plate"
    CRAFTING_TIME = 2
    RESOURCES_NEEDED = {
        ResourceIron.NAME: 1,
        ResourceCoal.NAME: 1
    }

    def __init__(self, stacked_amount=1):
        super().__init__(stacked_amount)

        self.stack_size_max = 10

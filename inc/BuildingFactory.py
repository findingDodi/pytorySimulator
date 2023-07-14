from .BuildingBase import BuildingBase


class BuildingFactory(BuildingBase):

    def __init__(self):
        super().__init__()

        self.width = 50
        self.height = 50
        self.color = (200, 150, 100)

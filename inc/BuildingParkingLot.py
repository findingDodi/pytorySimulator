from .BuildingBase import BuildingBase


class BuildingParkingLot(BuildingBase):

    def __init__(self):
        super().__init__()

        self.width = 100
        self.height = 50
        self.color = (220, 220, 220)

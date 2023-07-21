from .BuildingBase import BuildingBase


class BuildingFactory(BuildingBase):

    def __init__(self, production_task):
        super().__init__()

        self.width = 50
        self.height = 50
        self.color = (200, 150, 100)

        self.production_task = production_task

    def __str__(self):
        return self.production_task.NAME

    def __repr__(self):
        return self.production_task.NAME

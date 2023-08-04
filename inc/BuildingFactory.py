from .BuildingBase import BuildingBase


class BuildingFactory(BuildingBase):

    def __init__(self, production_task):
        super().__init__()

        self.width = 50
        self.height = 50
        self.color = (200, 150, 100)

        self.item_slots = []
        self.items_max = 10

        self.production_task = production_task

    def __str__(self):
        return self.production_task.NAME + ": " + str(len(self.item_slots))

    def __repr__(self):
        return self.__str__()

    def process(self):
        if len(self.item_slots) < self.items_max:
            self.item_slots.append(
                self.production_task(20)
            )

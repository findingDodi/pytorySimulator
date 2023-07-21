

class BuildingBase:

    global_building_id = 0

    @staticmethod
    def get_next_building_id():
        BuildingBase.global_building_id += 1
        return BuildingBase.global_building_id

    def __init__(self):
        self.id = BuildingBase.get_next_building_id()
        self.width = 0
        self.height = 0
        self.position_x = 0
        self.position_y = 0
        self.color = None

    def set_position(self, x, y):
        self.position_x = x
        self.position_y = y

    def get_position(self):
        return (self.position_x, self.position_y)

    def get_rect(self):
        return (self.position_x, self.position_y, self.width, self.height)

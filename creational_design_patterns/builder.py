class House:
    walls = None
    doors = None
    windows = None
    roof = None
    garage = None


class Wall:
    pass


class Door:
    pass


class Window:
    pass


class Roof:
    pass


class Garage:
    pass


class HouseBuilder:
    house = None

    def init_house(self):
        self.house = House()

    def build_walls(self, number):
        raise NotImplementedError

    def build_doors(self, number):
        raise NotImplementedError

    def build_windows(self, number):
        raise NotImplementedError

    def build_roof(self):
        raise NotImplementedError

    def build_garage(self):
        raise NotImplementedError

    def get_house(self):
        return self.house


class WoodWall(Wall):
    pass


class WoodDoor(Door):
    pass


class WoodWindow(Window):
    pass


class WoodRoof(Roof):
    pass


class WoodGarage(Garage):
    pass


class CarbinBuilder(HouseBuilder):
    def build_walls(self, number):
        self.house.walls = [WoodWall() for i in range(number)]

    def build_doors(self, number):
        self.house.doors = [WoodDoor() for i in range(number)]

    def build_windows(self, number):
        self.house.windows = [WoodWindow() for i in range(number)]

    def build_roof(self):
        self.house.roof = WoodRoof()

    def build_garage(self):
        self.house.garage = WoodGarage()


class GoldWall(Wall):
    pass


class GoldDoor(Door):
    pass


class GoldWindow(Window):
    pass


class GoldRoof(Roof):
    pass


class GoldGarage(Garage):
    pass


class PalaceBuilder(HouseBuilder):
    def build_walls(self, number):
        self.house.walls = [GoldWall() for i in range(number)]

    def build_doors(self, number):
        self.house.doors = [GoldDoor() for i in range(number)]

    def build_windows(self, number):
        self.house.windows = [GoldWindow() for i in range(number)]

    def build_roof(self):
        self.house.roof = GoldRoof()

    def build_garage(self):
        self.house.garage = GoldGarage()


class SimpleHouseBuildingDirector:
    builder = None

    def __init__(self, builder):
        self.builder = builder

    def change_builder(self, builder):
        self.builder = builder

    def build_house(self):
        self.builder.init_house()
        self.builder.build_walls(4)
        self.builder.build_doors(1)
        self.builder.build_windows(2)
        self.builder.build_roof()
        hosue = self.builder.get_house()

        return hosue


class GarageHouseBuildingDirector:
    builder = None

    def __init__(self, builder):
        self.builder = builder

    def change_builder(self, builder):
        self.builder = builder

    def build_house(self):
        self.builder.init_house()
        self.builder.build_walls(4)
        self.builder.build_doors(1)
        self.builder.build_windows(2)
        self.builder.build_roof()
        self.builder.build_garage()
        hosue = self.builder.get_house()

        return hosue

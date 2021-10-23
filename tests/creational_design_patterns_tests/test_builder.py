import unittest
from .builder import *


class TestDirector(unittest.TestCase):
    def test_simple_house_director_with_carbin_builder(self):
        builder = CarbinBuilder()
        director = SimpleHouseBuildingDirector(builder)
        house = director.build_house()

        self.assertEqual(len(house.walls), 4)
        self.assertEqual(type(house.walls[0]), WoodWall)
        self.assertEqual(len(house.doors), 1)
        self.assertEqual(type(house.doors[0]), WoodDoor)
        self.assertEqual(len(house.windows), 2)
        self.assertEqual(type(house.windows[0]), WoodWindow)
        self.assertEqual(type(house.roof), WoodRoof)
        self.assertEqual(house.garage, None)

    def test_simple_house_director_with_palace_builder(self):
        builder = PalaceBuilder()
        director = SimpleHouseBuildingDirector(builder)
        house = director.build_house()

        self.assertEqual(len(house.walls), 4)
        self.assertEqual(type(house.walls[0]), GoldWall)
        self.assertEqual(len(house.doors), 1)
        self.assertEqual(type(house.doors[0]), GoldDoor)
        self.assertEqual(len(house.windows), 2)
        self.assertEqual(type(house.windows[0]), GoldWindow)
        self.assertEqual(type(house.roof), GoldRoof)
        self.assertEqual(house.garage, None)

    def test_garage_house_director_with_carbin_builder(self):
        builder = CarbinBuilder()
        director = GarageHouseBuildingDirector(builder)
        house = director.build_house()

        self.assertEqual(len(house.walls), 4)
        self.assertEqual(type(house.walls[0]), WoodWall)
        self.assertEqual(len(house.doors), 1)
        self.assertEqual(type(house.doors[0]), WoodDoor)
        self.assertEqual(len(house.windows), 2)
        self.assertEqual(type(house.windows[0]), WoodWindow)
        self.assertEqual(type(house.roof), WoodRoof)
        self.assertEqual(type(house.garage), WoodGarage)

    def test_garage_house_director_with_palace_builder(self):
        builder = PalaceBuilder()
        director = GarageHouseBuildingDirector(builder)
        house = director.build_house()

        self.assertEqual(len(house.walls), 4)
        self.assertEqual(type(house.walls[0]), GoldWall)
        self.assertEqual(len(house.doors), 1)
        self.assertEqual(type(house.doors[0]), GoldDoor)
        self.assertEqual(len(house.windows), 2)
        self.assertEqual(type(house.windows[0]), GoldWindow)
        self.assertEqual(type(house.roof), GoldRoof)
        self.assertEqual(type(house.garage), GoldGarage)

    def test_build_twice(self):
        builder = CarbinBuilder()
        director = SimpleHouseBuildingDirector(builder)
        house1 = director.build_house()
        house2 = director.build_house()

        self.assertIsNot(house1, house2)

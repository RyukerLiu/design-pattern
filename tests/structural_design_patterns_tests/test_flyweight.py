import unittest
from structural_design_patterns.flyweight import Canvas, Forest, TreeFactory


class TestFlyweight(unittest.TestCase):
    def test(self):
        canvas = Canvas()
        forest = Forest()
        forest.plant_tree(1, 2, 'tree', 'red', 'xxx')
        forest.plant_tree(1, 3, 'tree', 'red', 'xxx')
        forest.plant_tree(2, 3, 'tree', 'red', 'zzz')
        forest.draw(canvas)

        expect = 'at 1 2 have very big tree data tree red xxx.'
        expect += 'at 1 3 have very big tree data tree red xxx.'
        expect += 'at 2 3 have very big tree data tree red zzz.'
        self.assertEqual(canvas.content, expect)

        self.assertEqual(len(TreeFactory.tree_types), 2)

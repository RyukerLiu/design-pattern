class TreeType:
    '''
    The flyweight
    intrinsic data keep it here
    '''

    def __init__(self, name, color, texture):
        self.name = name
        self.color = color
        self.texture = texture

    def draw(self, canvas, x, y):
        canvas.content += f'at {x} {y} have very big tree data {self.name} {self.color} {self.texture}.'


class TreeFactory:
    '''
    Flyweight Factory
    '''
    tree_types = {}

    @staticmethod
    def get_tree_type(name, color, texture):
        key = f'{name}-{color}-{texture}'
        type = TreeFactory.tree_types.get(key)
        if type is None:
            type = TreeType(name, color, texture)
            TreeFactory.tree_types[key] = type
        return type


class Tree:
    def __init__(self, x, y, type):
        self.x = x
        self.y = y
        self.type = type

    def draw(self, canvas):
        self.type.draw(canvas, self.x, self.y)


class Forest:
    def __init__(self):
        self.trees = []

    def plant_tree(self, x, y, name, color, texture):
        type = TreeFactory.get_tree_type(name, color, texture)
        tree = Tree(x, y, type)
        self.trees.append(tree)

    def draw(self, canvas):
        for tree in self.trees:
            tree.draw(canvas)


class Canvas:
    def __init__(self):
        self.content = ''

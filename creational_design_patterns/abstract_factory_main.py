from .abstract_factory import VictorianFurnitureFactory, ModernFurnitureFactory


def get_furniture(variant):
    if variant == 'Victorian':
        furniture_factory = VictorianFurnitureFactory()
    elif variant == 'Modern':
        furniture_factory = ModernFurnitureFactory()
    else:
        raise Exception(f'variant: {variant} not support.')

    chair = furniture_factory.create_chair()
    coffee_table = furniture_factory.create_coffee_table()
    sofa = furniture_factory.create_sofa()

    return chair, coffee_table, sofa

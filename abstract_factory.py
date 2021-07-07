class Chair:
    def __str__(self):
        raise NotImplementedError('.__str__() should be overriden.')


class CoffeTable:
    def __str__(self):
        raise NotImplementedError('.__str__() should be overriden.')


class Sofa:
    def __str__(self):
        raise NotImplementedError('.__str__() should be overriden.')


class FurnitureFactory:
    def create_chair(self) -> Chair:
        raise NotImplementedError('.create_chair() should be overriden.')

    def create_coffee_table(self) -> CoffeTable:
        raise NotImplementedError(
            '.create_coffee_table() should be overriden.')

    def create_sofa(self) -> Sofa:
        raise NotImplementedError('.create_sofa() should be overriden.')


class VictorianChair(Chair):
    def __str__(self):
        return type(self).__name__


class VictorianCoffeTable(CoffeTable):
    def __str__(self):
        return type(self).__name__


class VictorianSofa(Sofa):
    def __str__(self):
        return type(self).__name__


class VictorianFurnitureFactory:
    def create_chair(self) -> Chair:
        return VictorianChair()

    def create_coffee_table(self) -> CoffeTable:
        return VictorianCoffeTable()

    def create_sofa(self) -> Sofa:
        return VictorianSofa()


class ModernChair(Chair):
    def __str__(self):
        return type(self).__name__


class ModernCoffeTable(CoffeTable):
    def __str__(self):
        return type(self).__name__


class ModernSofa(Sofa):
    def __str__(self):
        return type(self).__name__


class ModernFurnitureFactory:
    def create_chair(self) -> Chair:
        return ModernChair()

    def create_coffee_table(self) -> CoffeTable:
        return ModernCoffeTable()

    def create_sofa(self) -> Sofa:
        return ModernSofa()

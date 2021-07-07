class Chair:
    pass


class CoffeTable:
    pass


class Sofa:
    pass


class FurnitureFactory:
    def create_chair(self) -> Chair:
        raise NotImplementedError('.create_chair() should be overriden.')

    def create_coffee_table(self) -> CoffeTable:
        raise NotImplementedError(
            '.create_coffee_table() should be overriden.')

    def create_sofa(self) -> Sofa:
        raise NotImplementedError('.create_sofa() should be overriden.')


class VictorianChair(Chair):
    pass


class VictorianCoffeTable(CoffeTable):
    pass


class VictorianSofa(Sofa):
    pass


class VictorianFurnitureFactory:
    def create_chair(self) -> Chair:
        return VictorianChair()

    def create_coffee_table(self) -> CoffeTable:
        return VictorianCoffeTable()

    def create_sofa(self) -> Sofa:
        return VictorianSofa()


class VictorianChair(Chair):
    pass


class VictorianCoffeTable(CoffeTable):
    pass


class VictorianSofa(Sofa):
    pass


class VictorianFurnitureFactory:
    def create_chair(self) -> Chair:
        return VictorianChair()

    def create_coffee_table(self) -> CoffeTable:
        return VictorianCoffeTable()

    def create_sofa(self) -> Sofa:
        return VictorianSofa()


class ModernChair(Chair):
    pass


class ModernCoffeTable(CoffeTable):
    pass


class ModernSofa(Sofa):
    pass


class ModernFurnitureFactory:
    def create_chair(self) -> Chair:
        return ModernChair()

    def create_coffee_table(self) -> CoffeTable:
        return ModernCoffeTable()

    def create_sofa(self) -> Sofa:
        return ModernSofa()

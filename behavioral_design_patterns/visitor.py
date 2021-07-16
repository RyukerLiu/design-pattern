class Element:
    def accept(self, visitor):
        return visitor.visit(type(self))


class ElementA(Element):
    pass


class ElementB(Element):
    pass


class Visitor:
    def visit(self, element_type):
        if element_type is Element:
            return self.visit_element()
        elif element_type is ElementA:
            return self.visit_element_a()
        elif element_type is ElementB:
            return self.visit_element_b()

    def visit_element(self):
        return ''

    def visit_element_a(self):
        return 'A'

    def visit_element_b(self):
        return 'B'

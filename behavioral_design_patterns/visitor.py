class Element:
    def accept(self, visitor):
        return visitor.visit_element()


class ElementA(Element):
    def accept(self, visitor):
        return visitor.visit_element_a()


class ElementB(Element):
    def accept(self, visitor):
        return visitor.visit_element_b()


class Visitor:
    def visit_element(self):
        return ''

    def visit_element_a(self):
        return 'A'

    def visit_element_b(self):
        return 'B'

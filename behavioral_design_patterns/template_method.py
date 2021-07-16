class StringGenerator:
    def get_string(self):
        '''
        template method, should not be override by subclass
        '''

        return self.first_str() + self.second_str() + self.third_str()

    def first_str(self):
        return 'first'

    def second_str(self):
        return 'second'

    def third_str(self):
        return 'third'


class HolyStringGenerator(StringGenerator):
    def second_str(self):
        return 'holy'


class DarkStringGenerator(StringGenerator):
    def second_str(self):
        return 'dark'

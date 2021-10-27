class Iterator:
    def get_next(self):
        raise NotImplementedError

    def has_more(self) -> bool:
        raise NotImplementedError


class ListForwardIterator(Iterator):
    def __init__(self, collection):
        self.collection = collection
        self.index = 0

    def get_next(self):
        element = self.collection[self.index]
        self.index += 1
        return element

    def has_more(self) -> bool:
        return self.index < len(self.collection)


class ListBackwardIterator(Iterator):
    def __init__(self, collection):
        self.collection = collection
        self.index = len(self.collection) - 1

    def get_next(self):
        element = self.collection[self.index]
        self.index -= 1
        return element

    def has_more(self) -> bool:
        return self.index >= 0


class PythonicIterator(Iterator):
    def __init__(self, collection):
        self.collection = collection
        self.index = 0

    def __next__(self):
        try:
            value = self.collection[self.index]
            self.index += 1
        except IndexError:
            raise StopIteration()
            
        return value

class Collection:
    def create_iterator(self):
        raise NotImplementedError


class List(Collection):
    def __init__(self, list):
        self.list = list

    def __len__(self) -> int:
        return len(self.list)

    def __getitem__(self, key):
        return self.list[key]

    def get_forward_iterator(self):
        return ListForwardIterator(self)

    def get_backward_iterator(self):
        return ListBackwardIterator(self)

    def __iter__(self):
        return PythonicIterator(self)


class Iterator:
    def get_next(self):
        raise NotImplementedError

    def has_more(self) -> bool:
        raise NotImplementedError


class ForwardIterator(Iterator):
    def __init__(self, collection):
        self.collection = collection
        self.index = 0

    def get_next(self):
        if self.has_more():
            element = self.collection[self.index]
            self.index += 1
            return element

    def has_more(self) -> bool:
        return self.index < len(self.collection)


class Collection:
    def create_iterator(self) -> Iterator:
        raise NotImplementedError


class BackwardIterator(Iterator):
    def __init__(self, collection):
        self.collection = collection
        self.index = len(self.collection) - 1

    def get_next(self):
        if self.has_more():
            element = self.collection[self.index]
            self.index -= 1
            return element

    def has_more(self) -> bool:
        return self.index >= 0


class List(Collection):
    def __init__(self, list):
        self.list = list

    def __len__(self) -> int:
        return len(self.list)

    def __getitem__(self, key):
        return self.list[key]

    def get_forward_iterator(self):
        return ForwardIterator(self)

    def get_backward_iterator(self):
        return BackwardIterator(self)

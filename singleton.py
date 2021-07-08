class Singleton:
    __instance = None
    __key = 'create_singleton'

    def __init__(self, *args, create_key=None, **kwargs):
        if create_key != self.__key:
            raise Exception('Singleton should be construct by .get_instance')

    @classmethod
    def __construct(cls, *args, create_key=None, **kwargs):
        if create_key != Singleton.__key:
            raise Exception('Singleton should be construct by .get_instance')

        return cls(*args, **kwargs, create_key=create_key)

    @classmethod
    def get_instance(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = cls.__construct(
                *args, **kwargs, create_key=cls.__key)

        return cls.__instance


class FileSingleton(Singleton):
    def __init__(self, file, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.file = file

    def get_file(self):
        return self.file


class SingletonMeta(type):
    __instance = None

    def __call__(cls, *args, **kwargs):
        """
        Possible changes to the value of the `__init__` argument do not affect
        the returned instance.
        """
        if cls.__instance is None:
            instance = super().__call__(*args, **kwargs)
            cls.__instance = instance
        return cls.__instance


class SingletonV2(metaclass=SingletonMeta):
    pass


class FileSingletonV2(SingletonV2):
    def __init__(self, file):
        self.file = file

    def get_file(self):
        return self.file

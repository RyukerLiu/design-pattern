from threading import Lock

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


class Singleton(metaclass=SingletonMeta):
    pass


class FileSingleton(Singleton):
    def __init__(self, file):
        self.file = file

    def get_file(self):
        return self.file


class ThreadSafeSingletonMeta(type):
    __instance = None
    _lock: Lock = Lock()

    def __call__(cls, *args, **kwargs):
        """
        Possible changes to the value of the `__init__` argument do not affect
        the returned instance.
        """
        with cls._lock:
            if cls.__instance is None:
                instance = super().__call__(*args, **kwargs)
                cls.__instance = instance
        
        return cls.__instance


class ThreadSafeSingleton(metaclass=SingletonMeta):
    pass


class ThreadSafeFileSingleton(ThreadSafeSingleton):
    def __init__(self, file):
        self.file = file

    def get_file(self):
        return self.file


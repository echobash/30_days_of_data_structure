class Singleton_Logger:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Singleton_Logger, cls).__new__(cls)
            return cls._instance
        else:
            return cls._instance


logger1 = Singleton_Logger()
logger2 = Singleton_Logger()
print(f"Singleton - {id(logger1) = } {id(logger2) =}")


class Dirty_Logger:
    pass


logger1 = Dirty_Logger()
logger2 = Dirty_Logger()
print(f"Dirty - {id(logger1) = } {id(logger2) =}")

import threading
class SingleTon(type):

    __instances = dict()
    __locks = dict()


    def __call__(cls, *args, **kwargs):
        if cls not in cls.__locks:
            lock = threading.Lock()
            cls.__locks[cls] = lock
        if cls not in cls.__instances:
            with cls.__locks[cls]:
                if cls not in cls.__instances:
                    instance = super().__call__(*args, **kwargs)
                    cls.__instances[cls] = instance
        return cls.__instances[cls]



class ConnMgr(metaclass= SingleTon):

    def __init__(self, dbName: str):
        self.dbName = dbName
    


if __name__ == "__main__":
    conn1 = ConnMgr("PostGress")
    conn2 = ConnMgr("Oracle")

    print(conn1)
    print(conn2)

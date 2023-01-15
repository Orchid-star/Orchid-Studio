class CA:
    def __init__(self):
        print("CA 构造")
        self.name = "CA"
        self._name = "_CA"
        self.__name = "__CA"


class CB(CA):
    def __init__(self):
        super(CB, self).__init__()
        print("CB 构造")
        print(self.name)
        print(self._name)
        print(self.__name)


def test1():
    a = CA()
    print(a.name)
    print(a._name)


def test2():
    b = CB()
    print(b.name)
    print(b._name)


class CBase:
    def __init__(self, name, parent=None):
        self._name = name


class CChild(CBase):
    def __init__(self, attr1, name, parent=None):
        super().__init__(name, parent)
        self._channel = attr1

    def channel(self):
        return self._channel


def test3():
    a = CChild('123', 'Orchid', 'parent')
    print(a.channel())


if __name__ == "__main__":
    test3()
    # print(a.__name)

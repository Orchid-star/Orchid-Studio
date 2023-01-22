from abc import ABC, abstractmethod


class CBase(ABC):
    def __init__(self):
        pass

    def func1(self):
        print("base func1")

    @abstractmethod
    def func2(self):
        pass


class CChild(CBase):
    def __init__(self):
        super().__init__()

    def func1(self):
        print("child func1")

    def func2(self):
        print("child func2")


def show_info(obj):
    obj.func1()


if __name__ == "__main__":
    ch = CChild()
    # ch.func1()
    # ch.func2()
    show_info(ch)


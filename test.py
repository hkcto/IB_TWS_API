class A:
    def __init__(self) -> None:
        self.n = 2

    def add(self, m):
        print(f"self is {self} @A.add")
        self.n += m


a = A()
a.add(1)
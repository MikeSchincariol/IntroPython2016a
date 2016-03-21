class my_base(object):
    def __init__(self):
        print("Init called in: my_base")
        super().__init__()

class a(my_base):
    def __init__(self):
        print("Init called in: a")
        super().__init__()

class b(my_base):
    def __init__(self):
        print("Init called in: b")
        super().__init__()

class c(a, b):
    def __init__(self):
        print("Init called in: c")
        super().__init__()


if __name__ == "__main__":
    inst = c()

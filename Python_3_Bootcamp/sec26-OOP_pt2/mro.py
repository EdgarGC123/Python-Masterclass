# class A:
#     def do_something(self):
#         print("Method Defined In: A")


# class B(A):
#     def do_something(self):
#         print("Method Defined In: B")


# class C:
#     def do_something(self):
#         print("Method Defined In: C")


# class D(B, C):
#     def do_something(self):
#         print("Method Defined In: D")


# thing = D()
# thing.do_something()


class Mother:
    def __init__(self, eye_color="brown", hair_color="dark brown", hair_type="curly"):
        self.eye_color = eye_color
        self.hair_color = hair_color
        self.hair_type = hair_type


class Father:
    def __init__(self, eye_color="blue", hair_color="blond", hair_type="straight"):
        self.eye_color = eye_color
        self.hair_color = hair_color
        self.hair_type = hair_type


class Child(Mother, Father):
    pass


newkid = Child()
# print(newkid.mro())
# print(newkid.__mro__)
help(newkid)

# class Human:
#     def __init__(self, first, last, age):
#         self.first = first
#         self.last = last
#         if age >= 0:
#             self._age = age
#         else:
#             self._age = 0

#     def get_age(self):
#         return self._age

#     def set_age(self, new_age):
#         if new_age >= 0:
#             self._age = new_age
#         else:
#             self._age = 0

#     @property  # getter
#     def age(self):
#         return self._age

#     @age.setter  # setter
#     def age(self, nval):
#         if nval >= 0:
#             self._age = nval
#         else:
#             raise ValueError("Age can't be negative!")

#     @property
#     def full_name(self):
#         return f"{self.first} {self.last}"

#     @full_name.setter
#     def full_name(self, name):
#         self.first, self.last = name.split(" ")


# jane = Human("Jane", "Goodall", 34)
# # print(jane.get_age())
# # jane.set_age(45)
# # print(jane.get_age())
# print(jane.age)
# jane.age = 20
# print(jane.age)
# print(jane.first)

from copy import copy


class Human:
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age

    def __repr__(self):
        return f"Human named {self.first} {self.last}"

    def __len__(self):
        return self.age

    def __add__(self, other):
        if isinstance(other, Human):
            return Human(first="Newborn", last=self.last, age=0)
        return "You can't add that!"

    def __mul__(self, other):
        if isinstance(other, int):
            return [copy(self) for i in range(other)]
            s = "s" if other > 1 else ""
            return f"You are creating {other} clone{s} of a Human"
        return "You can't multiply that!"


j = Human("Jenny", "Larsen", 47)
k = Human("Kevin", "Jones", 49)
print(j)
print(len(j))
print(j + k)
triplets = j * 3
triplets[0].first = "Jason"
print(triplets)

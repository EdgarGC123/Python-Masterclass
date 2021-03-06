
#Section 8: Object Oriented Programming
###################################################
# class Teddy:
#     quantity = 200
#
#     def __init__(self, name, color):
#         self.name = name
#         self.color = color
#     def change_color(self,color):
#         print("This is a method")
#         self.color = color
#     def change_name(self, name):
#         self.name = name
#
# teddy1 = Teddy("Ted", "Red")
# print(teddy1.name)
# print(teddy1.color)
#
# teddy2 = Teddy("Rob","Brown")
# print(teddy2.name)
# print(teddy2.color)
#
#
# teddy1.change_color("Orange")
# print(teddy1.color)
# teddy1.change_name("Mr. PoopyButthole")
# print(teddy1.name)





# def abc():
#     name = input("Enter name")
#     age = input("Enter Age")
#     print(name)
#     print(age)
#
# class Student:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#
#     def get_data(self):
#         self.name = input("Enter the name ")
#         self.age = input("Enter age ")
#     def put_data(self):
#         print(self.name)
#         print(self.age)
#
# # student1 = Student("", "")
# # student1.get_data()
# # student1.put_data()
#
#
# class ScienceStudent(Student):
#     def science(self):
#         print("This is a science method")
#
# a = ScienceStudent("","")
# a.get_data()
#
# print(a.name, a.age)




# class A:
#     def a_method(self):
#         print("This is a method from A")
#
# class B:
#     def b_method(self):
#         print("This is a method from B")
#
# class C(A,B):
#     def c_method(self):
#         print("This is a method from C")
#
# c_object = C()
# c_object.a_method()
# c_object.b_method()
# c_object.c_method()









# class A:
#     def a_method(self):
#         print("This is a method from A")
#
# class B(A):
#     def b_method(self):
#         print("This is a method from B")
#
# class C(B):
#     def c_method(self):
#         print("This is a method from C")
#
# c_object = C()
# c_object.a_method()
# c_object.b_method()
# c_object.c_method()




# def factorial(x):
#     if x==1:
#         return x
#     return x*factorial(x-1)
# print(factorial(5))




# numbers={1,2,3,4,5,6}
# print(numbers)
# numbers.add(9)
# print(numbers)
# numbers.remove(4)
# print(numbers)

# seta = {1,2,3,4,5}
# setb = {4,5,6,7,8}
# print(seta | setb)
# print(seta & setb)
# print(seta - setb)
# print(setb - seta)





# from itertools import count

# for i in count(3):#count will start from parameter and count upwards forever. second parameter is how much to increment by
#     print(i)
#     if i>=20:
#         break



# from itertools import accumulate,takewhile
# numbers = list(accumulate(range(8)))
# print(numbers)
# print(list(takewhile(lambda x: x <= 6, numbers)))





#operator overloading

# class Point:
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y
#     def __add__(self, other):
#         x = self.x + other.x
#         y = self.y + other.y
#         return Point(x,y)
#     def __str__(self):
#         return "({0},{1})".format(self.x, self.y)
#
# point1 = Point(1,4)
# point2 = Point(2,8)
#
# print(point1 + point2)




# class Myclass:
#     __hidenvariable = 0
#     def add(self,increment):
#         self.__hidenvariable+= increment
#         print(self.__hidenvariable)
#     def __str__(self):
#         return "{0} is a hidden value".format(self.__hidenvariable)
#     def myprint(self):
#         print(self.__hidenvariable)
#     def myprint2(self):
#         print(self)
#
# objectone = Myclass()
# objectone.add(5)
# objectone.myprint()
# objectone.myprint2()
# print(objectone)


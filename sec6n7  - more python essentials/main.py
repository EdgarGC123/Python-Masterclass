
#section 6: More types in python
######################################################
# peopleDict = {"John": 32, "Rob": 23}
# print()

# numbers = {
#     1: "one",
#     2: "two",
#     3: "three"
# }
# print(numbers.get(5,"Key not found"))




# fruits = ("Apple", "Mango", "Peach")#this is a tuple, not a list. Tuple's are immutable
# print(fruits[0])


# numbers=[0,100,200,300,400,500,600]
# print(numbers[3:5])
# print(numbers[3:])
# print(numbers[:3])
# print(numbers[1:6:2])



# list = [x**2 for x in range(10) if x**2%2 ==0]
# print(list)


# numbers = ["my first val","my second val","my third val"]
#
# myString = "Numbers: {0} {1} {2}"
# myFormat = myString.format(numbers[0],numbers[1],numbers[2])
# print(myFormat)


# print(",".join(["Apple","Banana","Mango"]))
#
# print("Hello There".replace("There","World"))

# newstring = "Hello There"
# newstring = newstring.replace("There", "World")
# print(newstring)

# newstring = "this is a string"
# newstring = newstring.replace("ring","ing")
# print(newstring)
# print(newstring.startswith("this")) #returns either true or false. .endswith() is another.

# print(min(1,2,3,4,5))
# print(max(1,2,3,4,5))
# print(abs(-203))


# products = {"shampoo": 23, "soap": 5, "conditioner": 10}
#
# key = raw_input('what product are you interested in ')
# key = key.lower()
# if(key in products):
#     returnString = "You requested {0} and it costs ${1}"
#     myRet = returnString.format(key, products[key])
#     print(myRet)
# else:
#     print("Product not found")

#Coding Challenge
# list = [x**2 for x in range(10) if x**2%2 ==0]

# myArr = [x for x in range(1,101) if x%2 ==1]
# print(myArr)


#Section 7: Functional Programming
###################################################
# def add_ten(x):
#     return x+10
#
# def twice(func,arg):
#     first = func(arg)
#     second = func(first)
#     return second
#
# print(twice(add_ten, 10))



# result = (lambda x: x**2)(30)
# print(result)

# test = (lambda x: x**2)
# result = test(30)
# print(result)




# def add(x):
#     return x+2
# newlist = [10,20,30,40,50]
# result = list(map(add,newlist))
# result2 = map(add, newlist)
# print(result2)
# print(result)


# newlist = [10,20,30,40,50]
# result = list(map(lambda x: x+2,newlist))
# print(result)



# newlist =[1,2,3,4,5,7,2,9,11,13]
#
# result = filter(lambda x: x%2==0, newlist)
# print(result)




# def function():
#     counter = 0
#     while counter < 5:
#         yield counter
#         counter +=1
#
# for x in function():
#     print(x)



#
# def even_numbers(x):
#     for i in range(x):
#         if i%2 ==0:
#             yield i
#
#
# print(list(even_numbers(21)))



#Coding Challenge
# products=[10,15,20,30,15]
#
# def sDiscount(x):
#     return x*0.90
# def discount(x):
#     return x*.95
# studentDiscount = list(map(sDiscount, products))
# genDiscount = list(map(discount, studentDiscount))
# print(genDiscount)

#Coding Challenge
# print((lambda x: x*(x+5)**2)(5))

#Coding Challenge
# products=[10,15,20,30,15]
# def discount(x):
#     return x*0.90
# discountedProducts = list(map(discount, products))
# print(discountedProducts)




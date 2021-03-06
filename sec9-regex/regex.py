import re

# pattern = r"eggs" #r stands for string, check for a pattern in string that has eggs

# #match - must be 1 to 1 from the beginning - boolean return
# if re.match(pattern, "baconeggseggsbacon"):
#     print("we have a match")
# else:
#     print("we DON'T have a match")
# if re.match(pattern, "eggseggsbacon"):
#     print("we have a match")
# else:
#     print("we DON'T have a match")


# #search - pattern simply has to exist anywhere in the string
# if re.search(pattern, "baconeggseggsbacon"):
#     print("we have a match")
# else:
#     print("we DON'T have a match")
# if re.search(pattern, "eggseggsbacon"):
#     print("we have a match")
# else:
#     print("we DON'T have a match")


# #findall - same like search but returns an array of all the repeating patterns it found
# if re.findall(pattern, "baconeggseggsbacon"):
#     print("we have a match")
# else:
#     print("we DON'T have a match")
# if re.findall(pattern, "eggseggsbacon"):
#     print("we have a match")
# else:
#     print("we DON'T have a match")




# string = "My name is John, Hi I'm John"
# pattern = r"John"

# #sub - acts as a replacement for all instances of the pattern
# newstring = re.sub(pattern, "Rob", string)# (pattern searching, replacement string, string to change/update )
# print(newstring)





# pattern = re"gr.y"

# if re.match(pattern, "gray"):
#     print("Match Found")
# else:
#     print("Match Not Found")





# pattern = r"^gr.y$" #explicit for the start of the string to be the beginning ^ and end of the string should be 

# if re.match(pattern, "grey"):
#     print("Match 1")
# else:
#     print("Mat")




# pattern = r"[A-Z][A-Z][0-9]"

# if re.search(pattern, "AA1"):
#     print("Match found")




# pattern = r"eggs(bacon)*"

# if re.match(pattern, "eggsbaconbacon"):
#     print("Match found")



string = "a a a b b b wont //wont //won't won't"
newstr = string.split(" ")
pattern = r"[A-Za-z]+('[A-Za-z])?"

for x in newstr:
    # print(x)
    ret = re.match(pattern, x)
    if ret != None:
        print(ret[0])
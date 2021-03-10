#pip install bcrypt

import bcrypt

password = b"thisismypassword" #type casing maybe?

hashed = bcrypt.hashpw(password, bcrypt.gensalt())#bycrypt, run hash pw on ( string, bycrypt.gensalt )

print(hashed) #funky string

entered_password = input('Enter password to login') #for user input

# entered_password = bytes(entered_password, encoding='utf-8') #converting to bytes and back to a string (unicode-objects)

if bcrypt.checkpw(entered_password, hashed): #check pw to compare entered_password to hashed
    print('login successful')
else:
    print('invalid password')

from tkinter import *

import bcrypt

def validate(pw):
    hash = b'$2b$12$Esdli3IvvyO9X3SIvx8SOuZtAnEqUp00I6.SmBtxZ90udK.EzMySG'

    pw = bytes(pw, encoding='utf-8')

    if bcrypt.checkpw(pw, hash):
        print('login successful')
    else:
        print('invalid password')

root = Tk()
root.geometry("300x300")

pw_entry = Entry(root)
pw_entry.pack()

button = Button(text="validate", command = lambda: validate(pw_entry.get()))
button.pack()

root.mainloop()
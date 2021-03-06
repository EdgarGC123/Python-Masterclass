from tkinter import *

# root = Tk() #Tk is a class in tkinter
# label1 = Label(root, text="Hello World")
# label1.pack()
# root.mainloop()





# root = Tk()
# newframe = Frame(root)
# newframe.pack()
#
# otherframe = Frame(root)
# otherframe.pack(side=BOTTOM)
#
# button1 = Button(newframe,text="Click Here", fg="Red")
# button2 = Button(otherframe,text="Click Here", fg="Blue")
#
# button1.pack()
# button2.pack()
#
# root.mainloop()



#
# root = Tk()
#
# label1 = Label(root, text="Firstname")
# label2 = Label(root, text="Lastname")
#
# entry1 = Entry(root)
# entry2 = Entry(root)
#
# label1.grid(row=0, column=0)
# label2.grid(row=1,column=0)
#
# entry1.grid(row=0,column=1)
# entry2.grid(row=1,column=1)
#
# root.mainloop()





###self adjustable widgets
# root = Tk()
#
# label1 = Label (root, text="First", bg="Red", fg="White")
# label1.pack(fill=X)
#
# label2 = Label (root, text="Second", bg="Blue", fg="Green")
# label2.pack(side=LEFT, fill=Y)
#
# root.mainloop()








# root = Tk()
#
# def dosomething():
#     print("You clicked the button")
#
#
# button1 = Button(root, command=dosomething, text="Click Here")
# button1.pack()
#
# root.mainloop()







# class MyButtons:
#     def __init__(self, rootone):
#         frame = Frame(rootone)
#         frame.pack()
#
#         self.printbutton = Button(frame, text="Click Here", command=self.printmessage)
#         self.printbutton.pack()
#         self.quitbutton = Button(frame, text="Exit", command=frame.quit)
#         self.quitbutton.pack(side=LEFT)
#
#     def printmessage(self):
#         print("Button Clicked")
#
# root = Tk(className="Edgar's Mini App")
# b = MyButtons(root)
#
# root.mainloop()






# def function1():
#     print("Menu item clicked")
#
#
# root = Tk()
# mymenu = Menu(root)
# root.config(menu=mymenu)
#
# submenu = Menu(mymenu, bg="Red")
# mymenu.add_cascade(label="File", menu=submenu)
# submenu.add_command(label="Project", command=function1)
# submenu.add_command(label="Save", command=function1)
# submenu.add_separator()
# submenu.add_command(label="Exit", command=function1)
#
# newmenu = Menu(mymenu)
# mymenu.add_cascade(label="Edit", menu=newmenu)
# newmenu.add_command(label="Undo", command=function1)
#
# toolbar = Frame(root, bg="pink")
# toolbar.pack(side=TOP, fill=X)
#
# insertbutton = Button(toolbar, text="Insert Files", command=function1())
# insertbutton.pack(side=LEFT, padx=2, pady=3)
#
# printbutton = Button(toolbar, text="print", command=function1())
# printbutton.pack(side=LEFT, padx=2, pady=3)
#
#
# status = Label(root, text="This is the status", bd=1, relief=SUNKEN, anchor=W)
# status.pack(side=BOTTOM, fill=X)
#
# root.mainloop()




# import tkinter.messagebox
#
# root = Tk()
# tkinter.messagebox.showinfo("Title", "This is awesome")
#
# response = tkinter.messagebox.askquestion("Question 1", "Do you like coffee") #very specific method with yes or no buttons
#
# if response=="yes":
#     print("Here is a coffee for you")
#
# root.mainloop()




root = Tk()

canvas = Canvas(root, width=200, height=100)
canvas.pack()

newline = canvas.create_line(0,0, 50, 100)
otherline = canvas.create_line(10,10,100,100, fill="green")

root.mainloop()
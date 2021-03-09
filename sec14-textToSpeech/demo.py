from gtts import gTTS
import os

# text = "I like where this is going"
# output = gTTS(text = text, lang="en", slow = False)
# output.save('output2.mp3')

# #os.system("start output.mp3") # for Windows pc
# os.system("afplay output2.mp3") # for Mac pc

# text = open('demo.txt','r').read()

# language = 'ru'
# output = gTTS(text = text, lang= language, slow=False)
# output.save('fileoutput.mp3')

# os.system("afplay fileoutput.mp3")






from tkinter import *

root = Tk()

canvas = Canvas (root,width=400,height=300)
canvas.pack()

def textToSpeech():
    text = entry.get()
    language = 'ru'
    fil = gTTS(text=text, lang=language, slow=False)
    fil.save('output.mp3')
    os.system("afplay output.mp3")


entry = Entry(root)
canvas.create_window(200, 180, window=entry)


button = Button(text = "start", command=textToSpeech)
canvas.create_window(200, 230, window=button)

root.mainloop()
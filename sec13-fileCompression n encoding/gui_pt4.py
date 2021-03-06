import tkinter as tk 
from compressmodule_pt2 import compress, decompress
from tkinter import filedialog

def open_file():
    filename = filedialog.askopenfilename(initialdir='/', title="Select a file to compress")
    print(filename)
    return filename

def compression(i,o):
    compress(i,o)

def decompression(i,o):
    decompress(i,o)

window = tk.Tk()
window.title("Compression engine")
window.geometry("600x400")

compress_button = tk.Button(window,text="Compress",command=lambda: compression(open_file(), "compressedoutput1.txt"))
compress_button.grid(row=2,column=1)


# decompress_button = tk.Button(window,text="Decompress",command=lambda: decompression(input_entry2.get(), output_entry2.get()))
# decompress_button.grid(row=5,column=1)

window.mainloop()
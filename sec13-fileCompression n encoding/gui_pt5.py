import tkinter as tk 
from compressmodule_pt2 import compress, decompress
from tkinter import filedialog, simpledialog

#IMPORTANT NOTE:
#In pt4, we did not like how he was hardcoding the output file as 'compressedoutput1.txt'
#after doing research we found out about simpledialog

def open_file():
    filename = filedialog.askopenfilename(title="Select a file to compress")

    print(filename)
    if len(filename)>0:
        filename_output = "compressed_" + filename.split('/')[-1]
        # filename_output = simpledialog.askstring("Enter String", prompt="Enter new filename")
        print(filename_output)
        compress(filename,filename_output)

def compression(i,o):
    compress(i,o)

def decompression(i,o):
    decompress(i,o)

window = tk.Tk()
window.title("Compression engine")
window.geometry("600x400")

compress_button = tk.Button(window,text="Compress",command=lambda: open_file())
compress_button.grid(row=2,column=1)


# decompress_button = tk.Button(window,text="Decompress",command=lambda: decompression(input_entry2.get(), output_entry2.get()))
# decompress_button.grid(row=5,column=1)

window.mainloop()
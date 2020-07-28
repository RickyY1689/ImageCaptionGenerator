import tkinter as tk 
import requests
from io import BytesIO
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from PIL import Image, ImageTk
from ImgAnalysis import ImgAnalysis

# List of widgets can be found here https://www.tutorialspoint.com/python/python_gui_programming.htm with documentation 
# on how to add arguments and control both positioning and control 

# Define general variables 
height = 400
width = 600
imgAnalyzer = ImgAnalysis()

# Allows the selected background image to change with the shape of the window
def resize_image(event):
    new_width = event.width
    new_height = event.height
    image = copy_of_image.resize((new_width, new_height))
    photo = ImageTk.PhotoImage(image)
    backgroundLabel.config(image = photo)
    backgroundLabel.image = photo #avoid garbage collection

def clearFrame():
    for widget in imgFrame.winfo_children():
        widget.destroy()
    for widget in captionFrame.winfo_children():
        widget.destroy()
    
def sendInput(imgUrl):
    clearFrame()
    caption = imgAnalyzer.remoteImg(imgUrl)

    response = requests.get(imgUrl)
    img_data = response.content
    img = ImageTk.PhotoImage(Image.open(BytesIO(img_data)))
    imgBlock = tk.Label(imgFrame, image=img)
    imgBlock.pack(side="bottom", fill="both", expand="yes")
    imgBlock.image = img

    imgCaption=tk.Label(captionFrame, text=caption, fg="black")
    imgCaption.pack(side = "bottom", expand = YES)

def getImgPath():
    clearFrame()
    
    filename = filedialog.askopenfilename(initialdir="/", title="Select File", 
                                        filetypes=(("Jpegs", "*.jpg"), ("all files", "*.*")))
    
    pathlabel=tk.Label(midFrame, text=filename, bg="white", fg="black")
    pathlabel.place(relx=0.01, rely=0.5, relheight=0.7, anchor='w')
    # pathlabel.pack(side = "bottom", expand = YES)

    caption = imgAnalyzer.localImg(filename)

    img = ImageTk.PhotoImage(Image.open(filename))
    panel = Label(imgFrame, image = img)
    panel.pack(side = "bottom", fill = "both", expand = "yes")
    panel.image = img

    imgCaption=tk.Label(captionFrame, text=caption, fg="black")
    imgCaption.pack(side = "bottom", expand = YES)



root = tk.Tk()
root.title("Title")
root.geometry('600x400')

image = Image.open('compvis.png')
copy_of_image = image.copy()
photo = ImageTk.PhotoImage(image)
backgroundLabel = tk.Label(root, image = photo)
backgroundLabel.bind('<Configure>', resize_image)
backgroundLabel.pack(fill=BOTH, expand = YES)

canvas = tk.Canvas(root, height=height, width=width)
canvas.pack() 

# There are three ways to position things in Tkinter: place, pack, and grid 
upperFrame = tk.Frame(root, bg='#80c1ff')
upperFrame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n') 

entry = tk.Entry(upperFrame, bg='white', font=("Calibri 12"))
entry.place(relx=0.01, rely=0.5, relwidth=0.65, relheight=0.7, anchor='w')

#Labda functions are known as inline functions which will rerun everytime it is called allowing us to get the updated input 
button = tk.Button(upperFrame, text="Test button", bg='gray', command=lambda: sendInput(entry.get()))
button.place(relx=0.98, rely=0.5, relwidth=0.3, relheight=0.7, anchor='e') 

midFrame = tk.Frame(root, bg='#80c1ff')
midFrame.place(relx=0.5, rely=0.2, relwidth=0.75, relheight=0.1, anchor='n') 

pathlabel = tk.Label(midFrame, text="", bg='white')
pathlabel.place(relx=0.01, rely=0.5, relwidth=0.65, relheight=0.7, anchor='w') 

button = tk.Button(midFrame, text="Test button", bg='gray', command=getImgPath)
button.place(relx=0.98, rely=0.5, relwidth=0.3, relheight=0.7, anchor='e') 

imgFrame = tk.Frame(root, bg="#80c1ff", bd=10)
imgFrame.place(relx=0.5, rely=0.35, relwidth=0.75, relheight=0.5, anchor='n')
captionFrame = tk.Frame(root, bg="#80c1ff", bd=10)
captionFrame.place(relx=0.5, rely=0.85, relwidth=0.75, relheight=0.1, anchor='n')
# imgFrame = tk.Frame(lowerFrame, bg='white')
# imgFrame.place(relx=0.5, rely=0.35, relwidth=0.75, relheight=0.6, anchor='n')

root.mainloop()
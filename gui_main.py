import tkinter as tk
#from tkinter import ttk, LEFT, END
from PIL import Image, ImageTk



##############################################+=============================================================
root = tk.Tk()
root.configure(background="light gray")
# root.geometry("1300x700")


w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.title("Home Page")




label_l2 = tk.Label(root, text="Multi Purpose Security Application",font=("times", 30, 'bold'),
background="#8B0A50", fg="white", width=70, height=2)
label_l2.place(x=0, y=0)


logo_label=tk.Label()
logo_label.place(x=0,y=95)

x = 1



# calling the function

frame_alpr = tk.LabelFrame(root, text=" --Let's Start-- ", width=1800, height=200, bd=5, font=('times', 14, ' bold '),bg="light gray",fg="white")
frame_alpr.grid(row=0, column=0, sticky='nw')
frame_alpr.place(x=0, y=350)



################################$%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

def mode1():
    from subprocess import call
    call(["python","mode1.py"])
    #root.destroy()
    
def mode2():
    from subprocess import call
    call(["python","mode2.py"])
    #root.destroy()

def mode3():
    from subprocess import call
    call(["python","mode3.py"])
    #root.destroy()
    

def mode4():
    from subprocess import call
    call(["python","mode4.py"])
    #root.destroy()


def mode5():
    from subprocess import call
    call(["python","mode5.py"])
    #root.destroy()


def window():
  root.destroy()
  
  

#####################################################################################################################

button1 = tk.Button(frame_alpr, text="Mode 1", command=mode1, width=15, height=1,font=('times', 15, ' bold '), bg="white", fg="black")
button1.place(x=200, y=20)

button2 = tk.Button(frame_alpr, text="Mode 2",command=mode2,width=15, height=1,font=('times', 15, ' bold '), bg="white", fg="black")
button2.place(x=600, y=20)

button3 = tk.Button(frame_alpr, text="Mode 3",command=mode3,width=14, height=1,font=('times', 15, ' bold '), bg="white", fg="black")
button3.place(x=1100, y=20)

button4 = tk.Button(frame_alpr, text="Mode 4", command=mode4, width=15, height=1,font=('times', 15, ' bold '), bg="white", fg="black")
button4.place(x=200, y=100)

button5 = tk.Button(frame_alpr, text="Mode 5", command=mode5, width=15, height=1,font=('times', 15, ' bold '), bg="white", fg="black")
button5.place(x=600, y=100)


root.mainloop()

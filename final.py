import tkinter as tk
new=tk.Tk()
new.geometry("1920x1080")
new.title("Attendance Tracker")
new.configure(bg='#34cfeb')
new1=tk.Tk()
new1.title("attendance data")
new1.geometry("1920x1080")
new1.config(bg="#34cfeb")


def two():
    new.destroy()
    
    def display():
      a=int(e1.get())
      needed=25-a
      if a>25:
           tk.Label(new1,text="invalid number").grid(row=4,column=0)
      else:
           
           tk.Label(new1,text="This subject has 30 classes in total",font=("Helvetica",25),background='#34cfeb').grid(row=4,column=0)
           tk.Label(new1,text="you need to attend 25 classes to get 85 percent attendance",font=("Helvetica",25),background='#34cfeb').grid(row=5,column=0)
           tk.Label(new1,text="you need to attend these many classes to make up for attendance:",font=("Helvetica",25),background='#34cfeb').grid(row=6,column=0)
           tk.Label(new1,text=str(needed),font=("Helvetica",25),background='#34cfeb').grid(row=6,column=1)    
    
    
    global e1
    
    e1 = tk.Entry(new1)
    tk.Label(new1, text="enter no. of classes attended",font=("Helvetica",25),bg="#34cfeb").grid(row=2, column=0)
    e1.grid(row=2, column=1)
    button1 = tk.Button(new1, text="submit", bg="red", command=display,width=5,height=2)
    button1.grid(row=3, column=1 )
    

    new1.mainloop()
import tkinter as tk

def four():
    new.destroy()
    
    def display():
        attended_classes = int(e1.get())
        needed = 56 - attended_classes

        if attended_classes >66:
            tk.Label(new1, text="Invalid number").grid(row=4, column=0)
        else:
            tk.Label(new1, text="This subject has 66 classes in total", font=("Helvetica", 25)).grid(row=4, column=0)
            tk.Label(new1, text="You need to attend 56 classes to get 85 percent attendance", font=("Helvetica", 25)).grid(row=5, column=0)
            tk.Label(new1, text="You need to attend these many classes to make up for attendance:", font=("Helvetica", 25)).grid(row=6, column=0)
            tk.Label(new1, text=str(needed)).grid(row=6, column=1)

    global e1

    e1 = tk.Entry(new1)
    tk.Label(new1, text="Enter no. of classes attended", font=("Helvetica", 25),bg="#34cfeb").grid(row=2, column=0)
    e1.grid(row=2, column=1)
    button1 = tk.Button(new1, text="Submit", bg="green", command=display)
    button1.grid(row=3, column=1)

    new1.mainloop()
def one():
    new.destroy()
    

    def display():
        attended_classes = int(e1.get())
        needed = 12 - attended_classes

        if attended_classes > 15:
            tk.Label(new1, text="Invalid number").grid(row=4, column=0)
        else:
            tk.Label(new1, text="This subject has 15 classes in total", font=("Helvetica", 25)).grid(row=4, column=0)
            tk.Label(new1, text="You need to attend 12 classes to get 85 percent attendance", font=("Helvetica", 25)).grid(row=5, column=0)
            tk.Label(new1, text="You need to attend these many classes to make up for attendance:", font=("Helvetica", 25)).grid(row=6, column=0)
            tk.Label(new1, text=str(needed)).grid(row=6, column=1)

    global e1

    e1 = tk.Entry(new1)
    tk.Label(new1, text="Enter no. of classes attended", font=("Helvetica", 25),bg="#34cfeb").grid(row=2, column=0)
    e1.grid(row=2, column=1)
    button1 = tk.Button(new1, text="Submit", bg="green", command=display)
    button1.grid(row=3, column=1)

    new1.mainloop()
tk.Label(new,text="Welcome to attendance tracker , please select a subject to begin with",font=("Helvetica",36),background='#7181a4',padx=30).grid(row=0,column=0)
eng=tk.Button(new,text='english',command=two,font=("Helvetica",36),background='#7181a4',padx="50").grid(row=1, column=0)
math=tk.Button(new,text='maths',command=four,font=("Helvetica",36),background='#7181a4',padx="50    ").grid(row=2, column=0)
chem=tk.Button(new,text='chemistry',command=four,font=("Helvetica",36),background='#7181a4',padx="50").grid(row=3, column=0)
caed=tk.Button(new,text='CAED',command=four,font=("Helvetica",36),background='#7181a4',padx="50").grid(row=4, column=0)
cons=tk.Button(new,text='ICO',command=one,font=("Helvetica",36),background='#7181a4',padx="50").grid(row=5, column=0)
health=tk.Button(new,text='SFH',command=one,font=("Helvetica",36),background='#7181a4',padx="50").grid(row=6, column=0)
elective=tk.Button(new,text='ESC',command=two,font=("Helvetica",36),background='#7181a4',padx="50").grid(row=7, column=0)
    
new.mainloop()


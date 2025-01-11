#imports the tkinter library
from tkinter import *
from tkinter import messagebox

#these will pop up when an error occurs
'''
def errorMessage1():
   messagebox.showerror("PYTHON ERROR", "Only numbers please!")
def errorMessage2():
   messagebox.showerror("PYTHON ERROR", "Enter something for both textfields")
'''
'''
#function to calculate sum when button is pressed
def sum():
    try:
        a=str(t1.get())
        b=int(t2.get())
        c= print(f"Hello {a}, you are {b} years old")
        #sets the answer in textfield 3
        t3.insert(0,c)
    except:
        if t1.get() == "" or t2.get() == "":
            errorMessage2()
        else:
            errorMessage1()
'''
#function to clear textfields when button is pressed
def clear():
    t1.delete(0,END)
    t2.delete(0,END)
    t3.delete(0,END)

#this is used to create the window, title & dimensions            
window = Tk()
window.title("Dice roll")
window.geometry("250x200")

#this just puts a space between the top & the first entry
l0=Label(window,text="")
l0.grid(row = 1,column = 0)

#this is the label & textfield for the first number
l1=Label(window,text="First Number", font=('Arial', 9))
l1.grid(row = 2,column = 0)
t1=Entry(window)
t1.grid(row = 2,column = 1)

#this is the label & textfield for the second number
l2=Label(window,text="Second Number", font=('Arial', 9))
l2.grid(row = 3,column = 0)
t2=Entry(window)
t2.grid(row = 3,column = 1)

#this is the label & textfield for the result of sum of the numbers
l3=Label(window,text="Result", font=('Arial', 9))
l3.grid(row = 4,column = 0)
t3=Entry(window)
t3.grid(row = 4,column = 1)

#this just puts a space between the buttons and the textfields
l4=Label(window,text="")
l4.grid(row = 5,column = 0)

#button for sum
b1=Button(window,text="Sum", command = sum)
b1.grid(row = 6,column = 1)

#button for clear
b2=Button(window,text="Clear", command = clear)
b2.grid(row = 7,column = 1)

#button for exit
b3=Button(window,text="Exit", command = window.destroy)
b3.grid(row = 8,column = 1)

#opens the window and keeps it open
window.mainloop()

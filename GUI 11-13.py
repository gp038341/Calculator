import tkinter as tk
from tkinter.simpledialog import askinteger
from tkinter import *
from tkinter import messagebox

top = Tk()


top.geometry("500x750") #size of window
answer = Text(width=35, height=2)
answer.place(x=100, y=100)

pressedEqual = False

def show(x):
    global pressedEqual
    try:
        if x == "=":
            final_answer = eval(answer.get(1.0, "end-1c"))
            answer.insert(tk.INSERT, x)
            answer.insert(tk.INSERT, final_answer)
            pressedEqual = True
        elif x == "AC":
            answer.delete(1.0, END)
        elif x == "TYPE":
            num = askinteger(title="Input", prompt="Input an Integer")
            print(num)
            answer.insert(tk.INSERT, num)
        else:
            if pressedEqual == True:
                answer.delete(1.0, END)
                pressedEqual = False
            answer.insert(tk.INSERT, x)

    except:
        answer.delete(1.0, END)

B1 = Button(top, text="1", width=10, height=5, command=lambda: show("1"))  #calls function show and passes value "1"
B1.place(x=100, y=150) #Y = rows, x = columns

B2 = Button(top, text="2", width=10, height=5, command=lambda: show("2"))  #calls function show and passes value "1"
B2.place(x=200, y=150) #Y = rows, x = columns

B3 = Button(top, text="3", width=10, height=5, command=lambda: show("3"))  #calls function show and passes value "1"
B3.place(x=300, y=150) #Y = rows, x = columns

B4 = Button(top, text="4", width=10, height=5, command=lambda: show("4"))  #calls function show and passes value "1"
B4.place(x=100, y=250) #Y = rows, x = columns

B5 = Button(top, text="5", width=10, height=5, command=lambda: show("5"))  #calls function show and passes value "1"
B5.place(x=200, y=250) #Y = rows, x = columns

B6 = Button(top, text="6", width=10, height=5, command=lambda: show("6"))  #calls function show and passes value "1"
B6.place(x=300, y=250) #Y = rows, x = columns

B7 = Button(top, text="7", width=10, height=5, command=lambda: show("7"))  #calls function show and passes value "1"
B7.place(x=100, y=350) #Y = rows, x = columns

B8 = Button(top, text="8", width=10, height=5, command=lambda: show("8"))  #calls function show and passes value "1"
B8.place(x=200, y=350) #Y = rows, x = columns

B9 = Button(top, text="9", width=10, height=5, command=lambda: show("9"))  #calls function show and passes value "1"
B9.place(x=300, y=350) #Y = rows, x = columns

B10 = Button(top, text="+", width=10, height=5, command=lambda: show("+"))  #calls function show and passes value "1"
B10.place(x=100, y=450) #Y = rows, x = columns

B11 = Button(top, text="-", width=10, height=5, command=lambda: show("-"))  #calls function show and passes value "1"
B11.place(x=200, y=450) #Y = rows, x = columns

B12 = Button(top, text="0", width=10, height=5, command=lambda: show("0"))  #calls function show and passes value "1"
B12.place(x=300, y=450) #Y = rows, x = columns

B13 = Button(top, text="=", width=10, height=5, command=lambda: show("="))  #calls function show and passes value "1"
B13.place(x=400, y=550) #Y = rows, x = columns

B14 = Button(top, text="*", width=10, height=5, command=lambda: show("*"))  #calls function show and passes value "1"
B14.place(x=200, y=550) #Y = rows, x = columns

B15 = Button(top, text="/", width=10, height=5, command=lambda: show("/"))  #calls function show and passes value "1"
B15.place(x=100, y=550) #Y = rows, x = columns

B16 = Button(top, text="AC", width=39, height=5, command=lambda: show("AC"))  #calls function show and passes value "1"
B16.place(x=99, y=650) #Y = rows, x = columns)

B17 = Button(top, text="TYPE", width=10, height=5, command=lambda: show("TYPE"))  #calls function show and passes value "1"
B17.place(x=400, y=450) #Y = rows, x = columns

B13 = Button(top, text="^", width=10, height=5, command=lambda: show("**"))  #calls function show and passes value "1"
B13.place(x=300, y=550) #Y = rows, x = columns

top.mainloop() #calls output window and keeps it running until you close the window. This is needed for every GUI
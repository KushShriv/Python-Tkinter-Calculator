from tkinter import *

me = Tk()
me.geometry("400x500")
me.title("CALCULATOR")
melabel = Label(me, text="CALCULATOR")
melabel.pack(side=TOP)

textin = StringVar()
operator = ""

def clickButton(number):
    global operator
    operator = operator + str(number)
    textin.set(operator)

def equalButton():
    global operator
    result = str(eval(operator))
    textin.set(result)
    operator = result

def clearButton():
    global operator
    operator = ""
    textin.set('')

metext = Entry(me, textvar=textin)
metext.pack()

button1 = Button(me, text="1", command=lambda: clickButton(1))
button1.place(x=10, y=100)

button2 = Button(me, text="2", command=lambda: clickButton(2))
button2.place(x=10, y=170)

button3 = Button(me, text="3", command=lambda: clickButton(3))
button3.place(x=10, y=240)

button4 = Button(me, text="4", command=lambda: clickButton(4))
button4.place(x=75, y=100)

button5 = Button(me, text="5", command=lambda: clickButton(5))
button5.place(x=75, y=170)

button6 = Button(me, text="6", command=lambda: clickButton(6))
button6.place(x=75, y=240)

button7 = Button(me, text="7", command=lambda: clickButton(7))
button7.place(x=140, y=100)

button8 = Button(me, text="8", command=lambda: clickButton(8))
button8.place(x=140, y=170)

button9 = Button(me, text="9", command=lambda: clickButton(9))
button9.place(x=140, y=240)

button0 = Button(me, text="0", command=lambda: clickButton(0))
button0.place(x=10, y=310)

buttonDot = Button(me, text=".", command=lambda: clickButton("."))
buttonDot.place(x=75, y=310)

buttonPlus = Button(me, text="+", command=lambda: clickButton("+"))
buttonPlus.place(x=205, y=100)

buttonSubstract = Button(me, text="-", command=lambda: clickButton("-"))
buttonSubstract.place(x=205, y=170)

buttonMultiply = Button(me, text="*", command=lambda: clickButton("*"))
buttonMultiply.place(x=205, y=240)

buttonDivide = Button(me, text="/", command=lambda: clickButton("/"))
buttonDivide.place(x=205, y=310)

buttonClear = Button(me, text="CE", command=clearButton)
buttonClear.place(x=270, y=100)

buttonEqual = Button(me, command=equalButton, text="=")
buttonEqual.place(x=10, y=380)

me.mainloop()

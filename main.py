from tkinter import *

me = Tk()
me.geometry("354x460")
me.title("CALCULATOR")
melabel = Label(me, text="CALCULATOR", bg='White', font=("Times", 30, 'bold'))
melabel.pack(side=TOP)
me.config(background='White')

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

metext = Entry(me, font=("Courier New", 12, 'bold'), textvar=textin, width=25, bd=5, bg='powder blue')
metext.pack()

button1 = Button(me, padx=14, pady=14, bd=4, bg='white', command=lambda: clickButton(1), text="1", font=("Courier New", 16, 'bold'))
button1.place(x=10, y=100)

button2 = Button(me, padx=14, pady=14, bd=4, bg='white', command=lambda: clickButton(2), text="2", font=("Courier New", 16, 'bold'))
button2.place(x=10, y=170)

button3 = Button(me, padx=14, pady=14, bd=4, bg='white', command=lambda: clickButton(3), text="3", font=("Courier New", 16, 'bold'))
button3.place(x=10, y=240)

button4 = Button(me, padx=14, pady=14, bd=4, bg='white', command=lambda: clickButton(4), text="4", font=("Courier New", 16, 'bold'))
button4.place(x=75, y=100)

button5 = Button(me, padx=14, pady=14, bd=4, bg='white', command=lambda: clickButton(5), text="5", font=("Courier New", 16, 'bold'))
button5.place(x=75, y=170)

button6 = Button(me, padx=14, pady=14, bd=4, bg='white', command=lambda: clickButton(6), text="6", font=("Courier New", 16, 'bold'))
button6.place(x=75, y=240)

button7 = Button(me, padx=14, pady=14, bd=4, bg='white', command=lambda: clickButton(7), text="7", font=("Courier New", 16, 'bold'))
button7.place(x=140, y=100)

button8 = Button(me, padx=14, pady=14, bd=4, bg='white', command=lambda: clickButton(8), text="8", font=("Courier New", 16, 'bold'))
button8.place(x=140, y=170)

button9 = Button(me, padx=14, pady=14, bd=4, bg='white', command=lambda: clickButton(9), text="9", font=("Courier New", 16, 'bold'))
button9.place(x=140, y=240)

button0 = Button(me, padx=14, pady=14, bd=4, bg='white', command=lambda: clickButton(0), text="0", font=("Courier New", 16, 'bold'))
button0.place(x=10, y=310)

buttonDot = Button(me, padx=47, pady=14, bd=4, bg='white', command=lambda: clickButton("."), text=".", font=("Courier New", 16, 'bold'))
buttonDot.place(x=75, y=310)

buttonPlus = Button(me, padx=14, pady=14, bd=4, bg='white', text="+", command=lambda: clickButton("+"), font=("Courier New", 16, 'bold'))
buttonPlus.place(x=205, y=100)

buttonSubstract = Button(me, padx=14, pady=14, bd=4, bg='white', text="-", command=lambda: clickButton("-"), font=("Courier New", 16, 'bold'))
buttonSubstract.place(x=205, y=170)

buttonMultiply = Button(me, padx=14, pady=14, bd=4, bg='white', text="*", command=lambda: clickButton("*"), font=("Courier New", 16, 'bold'))
buttonMultiply.place(x=205, y=240)

buttonDivide = Button(me, padx=14, pady=14, bd=4, bg='white', text="/", command=lambda: clickButton("/"), font=("Courier New", 16, 'bold'))
buttonDivide.place(x=205, y=310)

buttonClear = Button(me, padx=14, pady=119, bd=4, bg='white', text="CE", command=clearButton, font=("Courier New", 16, 'bold'))
buttonClear.place(x=270, y=100)

buttonEqual = Button(me, padx=151, pady=14, bd=4, bg='white', command=equalButton, text="=", font=("Courier New", 16, 'bold'))
buttonEqual.place(x=10, y=380)

me.mainloop()

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

def keyPress(event):
    key = event.char
    if key in '0123456789+-*/.':
        clickButton(key)
    elif key == '\r':  # Enter key
        equalButton()
    elif key == '\x08':  # Backspace key
        clearButton()

Keys = {
    'buttonText': ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.', '+', '-', '*', '/', 'CE', '='],
    'buttonNames': ['button1', 'button2', 'button3', 'button4', 'button5', 'button6', 'button7', 'button8', 'button9', 'button0', 'buttonDot', 'buttonPlus', 'buttonSubstract', 'buttonMultiply', 'buttonDivide', 'buttonClear', 'buttonEqual'],
    'buttonX': [10, 10, 10, 75, 75, 75, 140, 140, 140, 10, 75, 205, 205, 205, 205, 270, 10],
    'buttonY': [100, 170, 240, 100, 170, 240, 100, 170, 240, 310, 310, 100, 170, 240, 310, 100, 380],
    'buttonPaddingx': [14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 47, 14, 14, 14, 14, 14, 151],
    'buttonPaddingy': [14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 47, 14, 14, 14, 14, 119, 14],
    'buttonBg': 'white',
    'buttonFont': ("Courier New", 16, 'bold'),
    'buttonCommand': [lambda: clickButton(1), lambda: clickButton(2), lambda: clickButton(3), lambda: clickButton(4), lambda: clickButton(5), lambda: clickButton(6), lambda: clickButton(7), lambda: clickButton(8), lambda: clickButton(9), lambda: clickButton(0), lambda: clickButton("."), lambda: clickButton("+"), lambda: clickButton("-"), lambda: clickButton("*"), lambda: clickButton("/"), clearButton, equalButton],
    'buttonbd': 4
    }

metext = Entry(me, font=("Courier New", 12, 'bold'), textvar=textin, width=25, bd=5, bg='powder blue')
metext.pack()
for i in range(len(Keys['buttonText'])):
    button = Button(me, padx=Keys['buttonPaddingx'][i], pady=Keys['buttonPaddingy'][i], bd=Keys['buttonbd'], bg=Keys['buttonBg'], command=Keys['buttonCommand'][i], text=Keys['buttonText'][i], font=Keys['buttonFont'])
    button.place(x=Keys['buttonX'][i], y=Keys['buttonY'][i])

me.bind('<Key>', keyPress)
me.mainloop()
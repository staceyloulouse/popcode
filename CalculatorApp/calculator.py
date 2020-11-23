from tkinter import *

#setup the frame of the interface and give it a title
root = Tk()
root.title("Algebra Calculator")
#setup calculator environment
e = Entry(root, width = 70, borderwidth = 5)
e.grid(row = 0, column = 0, columnspan = 5, padx=10,pady=10)
expression = myClick(e.get())

#reaction to clicking the button
def myClick(item):
    
    current = e.get()
    e.insert(0, item)
    e.delete(0,END)
    myLabel = Label(root, text=item)
    myLabel.grid(row=9, column=0, columnspan=3, padx=10,pady=10)
    if item == '1':
        one()
    return current
def one():
    expression = 1
    myLabel = Label(root, text=expression)
    myLabel.grid(row=9, column=0, columnspan=3, padx=10,pady=10)
    return expression

def action(item):
    entry = item
    if entry == "LCM":
        myLabel = Label(root, text=entry)
        myLabel.grid(row=9, column=0, columnspan=3, padx=10,pady=10)


#define buttons
button1 = Button(root, text = "1", padx=40,pady=20,command = myClick('1'))
button2 = Button(root, text = "2", padx=40,pady=20,command = myClick('2'))
button3 = Button(root, text = "3", padx=40,pady=20,command = myClick('3'))
button4 = Button(root, text = "4", padx=40,pady=20,command = myClick('4'))
button5 = Button(root, text = "5", padx=40,pady=20,command = myClick('5'))
button6 = Button(root, text = "6", padx=40,pady=20,command = myClick('6'))
button7 = Button(root, text = "7", padx=40,pady=20,command = myClick('7'))
button8 = Button(root, text = "8", padx=40,pady=20,command = myClick('8'))
button9 = Button(root, text = "9", padx=40,pady=20,command = myClick('9'))
button0 = Button(root, text = "0", padx=40,pady=20,command = myClick('0'))
buttonLcm = Button(root, text = "LCM", padx=35,pady=20,command = action('LCM'))
buttonGcf = Button(root, text = "GCF", padx=35,pady=20,command = myClick('GCF'))
buttonAvg = Button(root, text = "AVG", padx=35,pady=20,command = myClick('AVG'))
buttonNpR = Button(root, text = "nPr", padx=37,pady=20,command = myClick('nPr'))
buttonNcR = Button(root, text = "nCr", padx=37,pady=20,command = myClick('nCr'))
buttonDivide = Button(root, text = "/", padx=40,pady=20,command = myClick('divide'))
buttonMultiply = Button(root, text = "*", padx=40,pady=20,command = myClick('multiply'))
buttonSubtract = Button(root, text = "-", padx=40,pady=20,command = myClick('subtract'))
buttonAdd = Button(root, text = "+", padx=40,pady=20,command = myClick('plus'))
buttonPercent = Button(root, text = "%", padx=40,pady=20,command = myClick('percent'))
buttonFactorial = Button(root, text = "!", padx=40,pady=20,command = myClick('factorial'))
buttonNegate = Button(root, text = "(-)", padx=40,pady=20,command = myClick('negate'))
buttonX = Button(root, text = " x", padx=40,pady=20,command = myClick('x'))
buttonY = Button(root, text = "y", padx=40,pady=20,command = myClick('x'))
buttonX2 = Button(root, text = "x^2", padx=40,pady=20,command = myClick('x^2'))
buttonXy = Button(root, text = "x^y", padx=25,pady=20,command = myClick('x^y'))
buttonClear = Button(root, text = "Clear", padx=30,pady=20,command = myClick("Clear"))
fieldPreview= Entry(root, width = 50, borderwidth = 5)
#buttonStatus = Button(root, text = "Status Message", padx=40,pady=20,command = myClick)
buttonEqual = Button(root, text = "=", padx=40,pady=20,command = myClick('equal'))
buttonSimplify = Button(root, text = "Simplify", padx=40,pady=20,command = myClick('simplify'))
buttonSolve = Button(root, text = "Solve", padx=40,pady=20,command = myClick('solve'))
buttonDecimal = Button(root, text = ".", padx=40,pady=20,command = myClick('point'))
buttonComma = Button(root, text = ",", padx=40, pady = 20,command = myClick('comma'))

#grid placement for the buttons
button7.grid(row=2, column=1)
button8.grid(row=2, column=2)
button9.grid(row=2, column=3)
buttonDivide.grid(row=2, column=4)
buttonLcm.grid(row=2, column=5)
button4.grid(row=3, column=1)
button5.grid(row=3, column=2)
button6.grid(row=3, column=3)
buttonMultiply.grid(row=3, column=4)
buttonGcf.grid(row=3,column=5)
button1.grid(row=4, column=1)
button2.grid(row=4, column=2)
button3.grid(row=4, column=3)
buttonSubtract.grid(row=4, column=4)
buttonAvg.grid(row=4, column=5)
buttonNegate.grid(row=5, column=1)
button0.grid(row=5, column=2)
buttonDecimal.grid(row=5, column=3)
buttonAdd.grid(row=5, column=4)
buttonNcR.grid(row=5, column=5)
buttonX.grid(row=6, column=1)
buttonY.grid(row=6, column=2)
buttonComma.grid(row=6, column=3)
buttonPercent.grid(row=6, column=4)
buttonNpR.grid(row=6, column=5)
buttonX2.grid(row=7, column=1)
buttonXy.grid(row=7, column=2)
buttonClear.grid(row=7, column=5)
buttonFactorial.grid(row=7, column=3)
buttonEqual.grid(row=7, column=4)
fieldPreview.grid(row=8, column=1, columnspan=3, padx=10,pady=10)
buttonSimplify.grid(row=8, column=4, columnspan=2)
buttonSolve.grid(row=9, column=4, columnspan=2)



    








root.mainloop()


from tkinter import *

#setup the frame of the interface and give it a title
root = Tk()
root.title("Algebra Calculator")
#setup calculator environment
e = Entry(root, width = 30, borderwidth = 5)
e.grid(row = 0, column = 0, columnspan = 6, rowspan = 13, padx=10,pady=10)


#reaction to clicking the button
def myClick():
    hello = "Hello " + e.get()
    myLabel = Label(root, text = hello)
#define buttons
button1 = Button(root, text = "1", padx=40,pady=20,command = myClick)
button2 = Button(root, text = "2", padx=40,pady=20,command = myClick)
button3 = Button(root, text = "3", padx=40,pady=20,command = myClick)
button4 = Button(root, text = "4", padx=40,pady=20,command = myClick)
button5 = Button(root, text = "5", padx=40,pady=20,command = myClick)
button6 = Button(root, text = "6", padx=40,pady=20,command = myClick)
button7 = Button(root, text = "7", padx=40,pady=20,command = myClick)
button8 = Button(root, text = "8", padx=40,pady=20,command = myClick)
button9 = Button(root, text = "9", padx=40,pady=20,command = myClick)
button0 = Button(root, text = "0", padx=40,pady=20,command = myClick)
buttonLcm = Button(root, text = "LCM", padx=40,pady=20,command = myClick)
buttonGcf = Button(root, text = "GCF", padx=40,pady=20,command = myClick)
buttonAvg = Button(root, text = "AVG", padx=40,pady=20,command = myClick)
buttonNpR = Button(root, text = "nPr", padx=40,pady=20,command = myClick)
buttonNcR = Button(root, text = "nCr", padx=40,pady=20,command = myClick)
buttonDivide = Button(root, text = "/", padx=40,pady=20,command = myClick)
buttonMultiply = Button(root, text = "*", padx=40,pady=20,command = myClick)
buttonSubtract = Button(root, text = "-", padx=40,pady=20,command = myClick)
buttonAdd = Button(root, text = "+", padx=40,pady=20,command = myClick)
buttonPercent = Button(root, text = "%", padx=40,pady=20,command = myClick)
buttonFactorial = Button(root, text = "!", padx=40,pady=20,command = myClick)
buttonNegate = Button(root, text = "+/-", padx=40,pady=20,command = myClick)
buttonX = Button(root, text = "x", padx=40,pady=20,command = myClick)
buttonY = Button(root, text = "y", padx=40,pady=20,command = myClick)
buttonX2 = Button(root, text = "x^2", padx=40,pady=20,command = myClick)
buttonXy = Button(root, text = "x^y", padx=25,pady=20,command = myClick)
buttonOpenP = Button(root, text = "(", padx=40,pady=20,command = myClick)
buttonCloseP = Button(root, text = ")", padx=40,pady=20,command = myClick)
buttonPreview = Button(root, text = "", padx=40,pady=20,command = myClick)
buttonStatus = Button(root, text = "Status Message", padx=40,pady=20,command = myClick)
buttonEqual = Button(root, text = "=", padx=40,pady=20,command = myClick)
buttonSimplify = Button(root, text = "Simplify", padx=40,pady=20,command = myClick)
buttonSolve = Button(root, text = "Solve", padx=40,pady=20,command = myClick)
buttonAnswer = Button(root, text = "", padx=40,pady=20,command = myClick)
buttonDecimal = Button(root, text = ".", padx=40,pady=20,command = myClick)
buttonComma = Button(root, text = ",", padx=40, pady = 20,command = myClick)

#grid placement for the buttons
buttonAnswer.grid(row=0, column=0, columnspan = 5)
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
buttonOpenP.grid(row=7, column=3)
buttonCloseP.grid(row=7, column=3)
buttonFactorial.grid(row=7, column=4)
buttonEqual.grid(row=7, column=5)
buttonPreview.grid(row=8, column=1, columnspan=3)
buttonSimplify.grid(row=8, column=4, columnspan=2)
buttonStatus.grid(row=9, column=0, columnspan=3)
buttonSolve.grid(row=9, column=4, columnspan=2)











root.mainloop()


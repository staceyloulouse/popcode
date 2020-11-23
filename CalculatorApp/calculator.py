from tkinter import *

#setup the frame of the interface and give it a title
root = Tk()
root.title("Algebra Calculator")
#operator string
operator = ''
textInput = StringVar()
statusText = StringVar()
previewText = StringVar()


#setup calculator environment
e = Entry(root, fg = 'green', textvariable= textInput,justify='right',width = 70, borderwidth = 5)
e.grid(row = 0, column = 0, columnspan = 5, padx=10,pady=10)



#reaction to clicking the numbers and operator buttons
def numClick(number):
    global operator
    global previewText
    operator= operator + str(number)
    textInput.set(operator)
    
#preview area function
def updatePreview():
    global operator
    global previewText
    previewText = previewText + operator
    previewText.set(previewText)

#clear button function
def actionClear():
    global operator
    global statusText
    statusText.set(operator + ' cleared')
    operator = ''
    textInput.set('')

#equal button function
def actionEqual():
    global operator
    global statusText
    try:
        answer = str(eval(operator))
        textInput.set(answer)
        statusText.set(operator + '= '+ answer)
    except SyntaxError as y:
        statusText.set('Error')
    
    
#negate button function
def actionNegate():
    global operator
    operator = '-('+operator+')'
    textInput.set(operator)

#define buttons in top row (7,8,9,/,LCM)=================================================
button7 = Button(root, text = "7", command=lambda: numClick(7),padx=40,pady=20)
button7.grid(row=2, column=0)

button8 = Button(root, text = "8", command=lambda: numClick(8),padx=40,pady=20)
button8.grid(row=2, column=1)

button9 = Button(root, text = "9", command=lambda: numClick(9),padx=40,pady=20)
button9.grid(row=2, column=2)

buttonDivide = Button(root, text = "/", command = lambda: numClick("/"), padx=40,pady=20)
buttonDivide.grid(row=2, column=3)

buttonLcm = Button(root, text = "LCM", padx=35,pady=20)
buttonLcm.grid(row=2, column=4)

#Second row of buttons (4, 5,6,*,GCF)===================================================
button4 = Button(root, text = "4", command=lambda: numClick(4),padx=40,pady=20)
button4.grid(row=3, column=0)

button5 = Button(root, text = "5", command=lambda: numClick(5),padx=40,pady=20)
button5.grid(row=3,column=1)

button6 = Button(root, text = "6", command=lambda: numClick(6),padx=40,pady=20)
button6.grid(row=3, column=2)

buttonMultiply = Button(root, text = "*", command=lambda: numClick('*'),padx=40,pady=20)
buttonMultiply.grid(row=3, column=3)

buttonGcf = Button(root, text = "GCF", padx=35,pady=20)
buttonGcf.grid(row=3,column=4)

#Third row of buttons (1,2,3,-,AVG)=======================================================

button1 = Button(root, text = "1", command=lambda: numClick(1),padx=40,pady=20)
button1.grid(row=4, column=0)

button2 = Button(root, text = "2", command=lambda: numClick(2),padx=40,pady=20)
button2.grid(row=4, column=1)

button3 = Button(root, text = "3", command=lambda: numClick(3),padx=40,pady=20)
button3.grid(row=4, column=2)

buttonSubtract = Button(root, text = "-", command=lambda: numClick('-'),padx=40,pady=20)
buttonSubtract.grid(row=4, column=3)

buttonAvg = Button(root, text = "AVG", padx=35,pady=20)
buttonAvg.grid(row=4, column=4)

#Fourth row of buttons ((-),0,+,nCr)=======================================================
buttonNegate = Button(root, text = "(-)", command = lambda: actionNegate(), padx=40,pady=20)
buttonNegate.grid(row=5, column=0)

button0 = Button(root, text = "0", command=lambda: numClick(0),padx=40,pady=20)
button0.grid(row=5, column=1)

buttonDecimal = Button(root, text = ".", command=lambda: numClick('.'),padx=40,pady=20)
buttonDecimal.grid(row=5, column=2)


buttonAdd = Button(root, text = "+", command=lambda: numClick('+'),padx=40,pady=20)
buttonAdd.grid(row=5, column=3)


buttonNcR = Button(root, text = "nCr", padx=37,pady=20)
buttonNcR.grid(row=5, column=4)

#Fifth row of buttons (x,y,,,%,nPr)==========================================================

buttonX = Button(root, text = " x", padx=40,pady=20)
buttonX.grid(row=6, column=0)

buttonY = Button(root, text = "y", padx=40,pady=20)
buttonY.grid(row=6, column=1)


buttonComma = Button(root, text = ",", padx=40, pady = 20)
buttonComma.grid(row=6, column=2)

buttonPercent = Button(root, text = "%", padx=40,pady=20)
buttonPercent.grid(row=6,column=3)

buttonNpR = Button(root, text = "nPr", padx=37,pady=20)
buttonNpR.grid(row=6, column=4)


#Sixth row of buttons(x^2,x^y,!,=,Clear)========================================================

buttonX2 = Button(root, text = "x^2", padx=40,pady=20)
buttonX2.grid(row=7, column=0)

buttonXy = Button(root, text = "x^y", padx=25,pady=20)
buttonXy.grid(row=7, column=1)

buttonFactorial = Button(root, text = "!", padx=40,pady=20)
buttonFactorial.grid(row=7, column=2)

buttonEqual = Button(root, text = "=", command = lambda: actionEqual(), padx=40,pady=20)
buttonEqual.grid(row=7, column=3)

buttonClear = Button(root, text = "Clear", command = lambda: actionClear(),padx=30,pady=20)
buttonClear.grid(row=7, column=4)

#Preview Area======================================================================================
fieldPreview= Label(root, width = 50, borderwidth = 5,bg='powder blue',textvariable = previewText,padx=20,pady=10)
fieldPreview.grid(row=8, column=0, columnspan=3, padx=20)

#button to request simplified expression
buttonSimplify = Button(root, text = "Simplify", padx=20,pady=20)
buttonSimplify.grid(row=8,column=3, columnspan=3)

#button to solve equation
buttonSolve = Button(root, text = "Solve", padx=30,pady=20)
buttonSolve.grid(row=9, column=3, columnspan=3)

#status message area
statusMessage = Label(root, fg = 'red', textvariable= statusText)
statusMessage.grid(row=9,column=0,columnspan=3)

# repeat root display until window closes
root.mainloop()


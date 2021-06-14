import sqlite3
import tkinter 
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from PIL import ImageTk, Image
from tkinter import Scale

#set up screen
main_screen = tkinter.Tk()
main_screen.title('Widgets Tutorial')
main_screen.iconbitmap('C:\\Users\\stace\\OneDrive\\Documents\\python\\2quizBit\\iconImage.ico')
main_screen.configure(background = 'grey')

#define some global variables
student_options = []

# setting up the database
sql_db = sqlite3.connect('users.db')
control = sql_db.cursor()

#create a table within the database using the control cursor
control.execute('SELECT oid,* FROM students')
entries = control.fetchall()
for entry in entries:
    student_options.append(entry)
    
sql_db.commit()
sql_db.close()

#define string variable and other variables
student_clicked = StringVar(main_screen, student_options[0])
submissions = []
lunch = ['No cheese', 'No peppers', 'No mushrooms', 'and No tomatoes.']
rate_num = StringVar()
year_num = StringVar()
has_cheese = IntVar()
has_peppers = IntVar()
has_mushrooms = IntVar()
has_tomatoes = IntVar()
toppings = StringVar()
entree_clicked = StringVar(main_screen, 'Pizza')
photo = ImageTk.PhotoImage(Image.open('C:\\Users\\stace\\OneDrive\\Documents\\python\\pylogo.png'))
toggle = True

#define a function for the click of the button
def clickAction():
    global toggle
    global start_button

    if toggle:
        start_button.config(bg = 'black', fg = 'white', text = 'Thank you!')
        toggle = False
    else:
        start_button.config(bg = 'white', fg = 'black')
        toggle = True

    sql_db = sqlite3.connect('users.db')
    control = sql_db.cursor()

    control.execute('SELECT oid,* FROM students')
    #use fetchall, fetchmany(#howmany), or fetchone
    entries = control.fetchall()
    entry_string = ''
    for entry in entries:
        entry_string+=str(entry)+'\n'
    Label(main_screen, text = entry_string).grid(row = 14, column = 1)

    #update the database and close it
    sql_db.commit()
    sql_db.close()

def show_entries():
    #connect to database
    sql_db = sqlite3.connect('users.db')
    control = sql_db.cursor()

    control.execute('SELECT oid,* FROM students')
    #use fetchall, fetchmany(#howmany), or fetchone
    entries = control.fetchall()
    entry_string = ''
    for entry in entries:
        entry_string+=str(entry)+'\n'
    Label(main_screen, text = entry_string).grid(row = 14, column = 1)

    #update the database and close it
    sql_db.commit()
    sql_db.close()


def delete_entry():
    #connect to database
    sql_db = sqlite3.connect('users.db')
    control = sql_db.cursor()
    id_num = student_clicked.get().split(',')
    id_num = id_num[0][1:]

    control.execute('DELETE FROM students WHERE oid = ' + id_num)
  
    #update the database and close it
    sql_db.commit()
    sql_db.close()

# update an email entry for a student
def update_entry():
    # setting up a new screen
    update_screen = tkinter.Tk()
    update_screen.title('Update Student Email')
    update_screen.configure(background = 'purple')
    update_screen.geometry('200x200')

    
    # entry label and field for email input
    user_label = Label(update_screen, text = 'New Email').pack()
    new_email = Entry(update_screen, borderwidth = 5 )
    new_email.pack()
    

    def update_email():
        global user_label
        sql_db = sqlite3.connect('users.db')
        control = sql_db.cursor()
        id_num = student_clicked.get().split(',')
        id_num = id_num[0][1:]

        control.execute('''
        'UPDATE students SET 
        email = :email
        WHERE oid = ''' + id_num,
        {
            
            'email': new_email.get(),
            
        })

        #update the database and close it
        sql_db.commit()
        sql_db.close()
    
        update_screen.destroy()

    save_button = Button(update_screen, text = 'Save', command = update_email)
    save_button.pack()
    
def submit_action():
    #connect to database
    sql_db = sqlite3.connect('users.db')
    control = sql_db.cursor()

    control.execute('INSERT INTO students VALUES (:name, :email)',
            {
                'name':user_entry.get(),
                'email':email_entry.get()
            })
    #update the database and close it
    sql_db.commit()
    sql_db.close()

    submit_button.config(text = 'Success!', bg = 'light blue', fg = 'white')
    
    submissions.append({user_entry.get(): email_entry.get()})
    submit_text = 'Hi, ' + user_entry.get()+' '+email_entry.get()
    Label(main_screen, text = submit_text, font = ('Arial black', 22)).grid(row = 3, column = 1, pady = 10)
    
    user_entry.delete(0,END)
    email_entry.delete(0,END)

#show result of checking radio button with messagebox
#other messagebox methods --> showwarning, showerror, askquestion, askokcancel, askyesno
def check(value):
    if value == 'quotes':
        messagebox.showinfo('Result', 'That\'s, correct!')
    else:
        messagebox.showinfo('Result', 'That\'s, not right!')

#use a dialog box to get the file name of the photo to use
def open_image_file():
    global picture
    
    open_frame_icon = filedialog.askopenfilename(initialdir = '/', title = 'Choose a photo')
    open_label = Label(open_frame, text = open_frame_icon)
    open_label.pack()
    picture = ImageTk.PhotoImage(Image.open(open_frame_icon))
    open_icon = Label(open_frame, image = picture, width = 200, height = 200)
    open_icon.pack_forget()
    open_icon.pack()

# function to assign a value to rate_num based on the slider
def get_rating():
    global rate_num
    rate_num.set(wide.get())

def get_year():
    global year_num
    year_num.set(tall.get())

def get_lunch():
    global lunch
    order = 'Your lunch comes with: Sauce, '
    if has_cheese.get()==1:
        order += 'Cheese, '
    else:
        order += lunch[0] + ', '
    if has_peppers.get()==1:
        order += 'Peppers, '
    else:
        order += lunch[1] + ', '
    if has_mushrooms.get()==1:
        order += 'Mushrooms, '
    else:
        order += lunch[2] + ', '
    if has_tomatoes.get()==1:
        order += 'and Tomatoes. '
    else:
        order += lunch[3]
    
    lunch_label = Label(main_screen, textvariable = toppings)
    lunch_label.grid(row = 12, column = 0)
    toppings.set(order)

#label widgets
icon_label = Label(image = photo)
icon_label.grid(row = 13, column = 0)

welcome_label = Label(main_screen, text = 'Welcome to Widgets!', bg = 'grey',font = ('Arial black', 22) )
welcome_label.grid(row = 0, column = 1, columnspan = 2)

name_label = Label(main_screen, text = 'Enter your name:', bg = 'grey', font = ('Arial black', 22))
name_label.grid(row = 1, column = 0)

email_label = Label(main_screen, text = 'Enter your email:', bg = 'grey', font = ('Arial black', 22))
email_label.grid(row = 1, column = 2)



#define frames
open_frame = LabelFrame(main_screen, text = 'Select an image', padx=20, pady=20)
open_frame.grid(row = 4,column = 0)

option_frame = LabelFrame(main_screen, text = 'What symbol is used to define strings?', padx=50, pady = 50)
option_frame.grid(row = 4, column = 1)


#button widgets
start_button = Button(main_screen,text = 'Finish', bg = 'yellow', command = clickAction,font = ('Arial black', 22), fg = 'light blue')
start_button.grid(row = 4, column = 4)

submit_button = Button(main_screen, text = 'Submit', bg = 'yellow', command = submit_action,font = ('Arial black', 22), fg = 'light blue')
submit_button.grid(row = 1, column = 4, columnspan = 4, pady = 5, padx = 10)

exit_button = Button(main_screen, text = 'Exit', bg = 'yellow', command = main_screen.quit, font = ('Arial black', 22), fg = 'light blue')
exit_button.grid(row = 13, column = 4)

open_button = Button(open_frame, text = 'Choose photo', bg = 'red', command = open_image_file)
open_button.pack()

delete_button = Button(main_screen, text = 'Delete Student', bg = 'yellow', command = delete_entry, font = ('Arial black', 22), fg = 'light blue')
delete_button.grid(row = 7, column = 4)

update_button = Button(main_screen, text = 'Update Student', bg = 'yellow', command = update_entry, font = ('Arial black', 22), fg = 'light blue')
update_button.grid(row = 8, column = 4)

# Entry widget for input
user_entry = Entry(main_screen, borderwidth = 5)
user_entry.grid(row = 1, column = 1)

email_entry = Entry(main_screen, borderwidth = 5)
email_entry.grid(row = 1, column = 3)

#set up an radiobutton question
selection = StringVar()
Radiobutton(option_frame, text = 'quotes', variable = selection, value = 'quotes' ).pack(anchor = W)
Radiobutton(option_frame, text = 'comma', variable = selection, value = 'comma').pack(anchor = W)
Radiobutton(option_frame, text = 'colon', variable = selection, value = 'colon').pack(anchor = W)
Radiobutton(option_frame, text = 'asterisk', variable = selection, value = 'asterisk').pack(anchor = W)
radio_button = Button(option_frame, text = 'Check answer', bg = 'red', command = lambda:check(selection.get()))
radio_button.pack(anchor = W)

#slider widget is called Scale
#define vertical slider for year entry, orientation is vertical
#by default
tall = Scale(main_screen, from_ = 2000, to = 2030)
tall.grid(row = 4, column = 3)

year_label = Label(main_screen, textvariable = year_num)
year_label.grid(row = 6, column = 3)
year_button = Button (main_screen, text = 'Submit Year', bg = 'red', command = get_year)
year_button.grid(row = 5, column = 3)

#create a drop down menu for lunch extras
#choose from pizza, hambuger, or salad
lunch_options = OptionMenu(main_screen, entree_clicked, 'Pizza', 'Hamburger', 'Salad')
lunch_options.grid(row = 7, column = 0)

#create drop down menu for students entered
student_menu = OptionMenu(main_screen, student_clicked, *student_options)
student_menu.grid(row = 7, column = 3, pady= 5)

#scale widget for ratings entry
wide = Scale(main_screen, from_ = 0, to = 100, orient = HORIZONTAL)
wide.grid(row = 4, column = 2)

rate_label = Label(main_screen, textvariable = rate_num)
rate_label.grid(row = 6, column = 2)
rating = Button(main_screen, text = "Submit Rating", bg = 'red', command = get_rating)
rating.grid(row = 5, column = 2)

#create check boxes for a pizza order
#default variable is 1 or 0, set variariable with attributes onvalue or offvalue
check_box1 = Checkbutton(main_screen, text = 'Cheese', variable = has_cheese)
check_box1.grid(row = 7, column = 1)

check_box2 = Checkbutton(main_screen, text = 'Peppers', variable = has_peppers)
check_box2.grid(row = 8, column = 1)

check_box3 = Checkbutton(main_screen, text = 'Mushrooms', variable = has_mushrooms)
check_box3.grid(row = 9, column = 1)

check_box4 = Checkbutton(main_screen, text = 'Tomatoes', variable = has_tomatoes)
check_box4.grid(row = 10, column = 1)

lunch_order = Button(main_screen, text = 'Order Lunch', command = get_lunch, pady = 5, bg = 'red')
lunch_order.grid(row = 11, column = 1, pady = 10)

query_students = Button(main_screen, text = 'Show entries', command = show_entries)
query_students.grid(row = 14, column = 0)

main_screen.mainloop()
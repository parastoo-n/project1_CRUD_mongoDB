from tkinter import *
from pymongo import MongoClient
from tkinter import ttk 
from tkinter import messagebox 
Client = MongoClient('localhost',27017)
db=Client['CRUD']
persons=db['persons1']

win=Tk()
# win.geometry("850x600")
win.attributes('-fullscreen',True)
win.title('CRUD')
win.iconbitmap('icons/python_18894.ico')
win.configure(background='#914d4d')


#def

def changeButtonStyleWithHoverRegister(e):
    btnRegister.configure(fg='#a18282',background='white')
    
def changeButtonStyleWithHoverToSelfRegister(e):
     btnRegister.configure(fg='white',background='#a18282')

def ActiveBtn(e):
    if txtName.get()!= '' and txtFamily.get() != '' and comboBoxField.get() != '' and txtAge.get() != '':
        btnRegister.configure(state=NORMAL)
    else: 
        btnRegister.configure(state=DISABLED)  

#TXTbox
txtName=Entry(win,width=15,bd=5,font=('arial',15,'bold'),bg='#a18282',fg='white',textvariable=Name,justify='center')
txtName.bind('<KeyRelease>',ActiveBtn)
txtName.place(x=100,y=100)

txtFamily=Entry(win,width=15,bd=5,font=('arial',15,'bold'),bg='#a18282',fg='white',textvariable=Family,justify='center')
txtFamily.bind('<KeyRelease>',ActiveBtn)
txtFamily.place(x=100,y=160)

txtField=Entry(win,width=15,bd=5,font=('arial',15,'bold'),bg='#a18282',fg='white',textvariable=Field,justify='center')
txtField.bind('<KeyRelease>',ActiveBtn)
txtField.place(x=100,y=220)


txtAge=Entry(win,width=15,bd=5,font=('arial',15,'bold'),bg='#a18282',fg='white',textvariable=Age,justify='center')
txtAge.bind('<KeyRelease>',ActiveBtn)
txtAge.place(x=100,y=280)

#LBL
lblName=Label(win,text='Name',font=('arial',12,'bold'),bg='#a18282',fg='white')
lblName.place(x=20,y=100)

lblFamily=Label(win,text='Family',font=('arial',12,'bold'),bg='#a18282',fg='white')
lblFamily.place(x=20,y=160)

lblField=Label(win,text='Filed',font=('arial',12,'bold'),bg='#a18282',fg='white')
lblField.place(x=20,y=220)

lblAge=Label(win,text='Age',font=('arial',12,'bold'),bg='#a18282',fg='white')
lblAge.place(x=20,y=280)

#BTN

btnRegister=Button(win,text='register',width=10,font=('arial',12,'bold'),bg='#a18282',fg='white')
btnRegister.configure(state=DISABLED)
btnRegister.bind('<Enter>',changeButtonStyleWithHoverRegister)
btnRegister.bind('<Leave>',changeButtonStyleWithHoverToSelfRegister)
btnRegister.bind('<Button-1>',OnClickRegister)
btnRegister.place(x=125,y=350)



win.mainloop()
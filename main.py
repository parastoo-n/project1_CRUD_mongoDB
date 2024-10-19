from tkinter import *
from pymongo import MongoClient
from tkinter import ttk 
from tkinter import messagebox 
Client = MongoClient('localhost',27017)
db=Client['project1_CRUD_mongoDB']
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

def OnClickRegister(e):
    if btnRegister.cget('state')==NORMAL:
       try: 

            person={'name':txtName.get(),'family':txtFamily.get(),'field':comboBoxField.get(),'age':int(txtAge.get())}
            if Exist(person)==False:
               Register(person)
            #    allData=ReadData()
               CleanTable()
            #    for data in allData:
            #        InsertDataToTable(data)
               Load()
               CleanTextBoxAfterUseCrud()
               messagebox.showinfo("success","your registration is complete")
            else:
                messagebox.showerror("error","you have already registered")
       except:
            messagebox.showerror("error","you must enter a number in the age field")

    def Register(person):
    if person['age']>=18:
       persons.insert_one(person)
   
def ReadData():
    AllData=persons.find()
    return AllData 
# ReadData() 
def InsertDataToTable(person):
    table.insert('','end',values=[person['name'],person['family'],person['field'],person['age']])

def CleanTable():
    for item in table.get_children():
        table.delete(item)

def CleanTextBoxAfterUseCrud():
        Name.set('')
        Family.set('')
        # Field.set('')
        Age.set('')
        txtName.focus_set()             

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

btnSearch=Button(win,text='search',width=10,font=('arial',12,'bold'),bg='#a18282',fg='white')
btnSearch.bind('<Enter>',changeButtonStyleWithHoverSearch)
btnSearch.bind('<Leave>',changeButtonStyleWithHoverToSelfSearch)
btnSearch.bind('<Button-1>',OnClickSearch)
btnSearch.place(x=400,y=50)


win.mainloop()
from tkinter import *
from pymongo import MongoClient
from tkinter import ttk 
from tkinter import messagebox 
Client = MongoClient('localhost',27017)
db=Client['CRUD']
persons=db['persons1']

win=Tk()
win.geometry("850x600")
# win.attributes('-fullscreen',True)
win.title('CRUD')
win.iconbitmap('icons/python_18894.ico')
win.configure(background='#914d4d')

win.mainloop()
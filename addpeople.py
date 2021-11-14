from tkinter import *
from tkinter import Toplevel
import sqlite3
from tkinter import font

con = sqlite3.connect('database.db')
cur = con.cursor()

class AddPeople(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry("650x750")
        self.title("Add People")
        self.resizable(False,False)

        #frames.......
        self.top=Frame(self,height=150,bg='white')
        self.top.pack(fill=X)

        self.bottom=Frame(self,height=500,bg='#fcc324')
        self.bottom.pack(fill=X)

        #Heading........
        self.top_Image=PhotoImage(file='icons/addperson.png')
        self.top_Image_Label = Label(self.top,image=self.top_Image,bg='white')
        self.top_Image_Label.place(x=120,y=10)
        self.heading = Label(self.top,text="Add Persons",font='arial 15 bold',fg='#003f8a',bg='white')
        self.heading.place(x=260,y=60)
        
        #Scrollbar....
        self.sb = Scrollbar(self.bottom,orient=VERTICAL)


        #Name
        self.lbl_name = Label(self.bottom, text= "Name", font='arial 15 bold' , fg='white', bg='#fcc324')
        self.lbl_name.place(x=40,y=40)
        self.ent_name = Entry(self.bottom, width=30, bd=4)
        self.ent_name.insert(0,'Please enter a name')
        self.ent_name.place(x=150,y=45)

        #Surname
        self.lbl_surname = Label(self.bottom, text= "Surname", font='arial 15 bold' , fg='white', bg='#fcc324')
        self.lbl_surname.place(x=40,y=80)
        self.ent_surname = Entry(self.bottom, width=30, bd=4)
        self.ent_surname.insert(0,'Please enter a surname')
        self.ent_surname.place(x=150,y=85)

        #Email
        self.lbl_email = Label(self.bottom, text= "Email", font='arial 15 bold' , fg='white', bg='#fcc324')
        self.lbl_email.place(x=40,y=120)
        self.ent_email = Entry(self.bottom, width=30, bd=4)
        self.ent_email.insert(0,'Please enter a Email')
        self.ent_email.place(x=150,y=125)

        #Phone
        self.lbl_Phone = Label(self.bottom, text= "Phone", font='arial 15 bold' , fg='white', bg='#fcc324')
        self.lbl_Phone.place(x=40,y=160)
        self.ent_phone = Entry(self.bottom, width=30, bd=4)
        self.ent_phone.insert(0,'Please enter a phone number')
        self.ent_phone.place(x=150,y=165)

        #Address
        self.lbl_address = Label(self.bottom, text= "Address", font='arial 15 bold' , fg='white', bg='#fcc324')
        self.lbl_address.place(x=40,y=300)
        self.ent_address = Text(self.bottom, width=23, height=15, wrap=WORD)
        self.ent_address.place(x=150,y=200)

        button = Button(self.bottom, text='Add Person')
        button.place(x=270,y=460)

from tkinter import *
from tkinter import Toplevel
import sqlite3
from tkinter import font
import addpeople
con = sqlite3.connect('database.db')
cur = con.cursor()

class MyPeople(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry("650x650")
        self.title("My People")
        self.resizable(False,False)

#frames.......
        self.top=Frame(self,height=150,bg='white')
        self.top.pack(fill=X)

        self.bottom=Frame(self,height=500,bg='#fcc324')
        self.bottom.pack(fill=X)

        #Heading........
        self.top_Image=PhotoImage(file='icons/person_icon.png')
        self.top_Image_Label = Label(self.top,image=self.top_Image,bg='white')
        self.top_Image_Label.place(x=120,y=10)
        self.heading = Label(self.top,text="My Persons",font='arial 15 bold',fg='#003f8a',bg='white')
        self.heading.place(x=260,y=60)
        
        #Scrollbar....
        self.sb = Scrollbar(self.bottom,orient=VERTICAL)

        #ListBox.......
        self.listbox= Listbox(self.bottom,width=60,height=31, font="Sans 10")
        self.listbox.grid(row=0,column=0,padx=(40,0))
        self.sb.config(command= self.listbox.yview)
        self.listbox.config(yscrollcommand=self.sb.set)
        self.sb.grid(row=0,column=1,sticky=N+S)

        persons=cur.execute("select * from persons").fetchall()
        print(persons)
        count = 0
        for person in persons:
            
            self.listbox.insert(count,str(person[0])+"-"+person[1]+" "+person[2])
            count +=1



        #Buttons......
        btnAdd = Button(self.bottom,text="Add",width=12,font='Sans 12 bold', command=self.funcaddPeople)
        btnAdd.grid(row=0,column=2,sticky=N,padx=10,pady=10)

        btnUpdate = Button(self.bottom,text="Update",width=12,font='Sans 12 bold')
        btnUpdate.grid(row=0,column=2,sticky=N,padx=10,pady=50)

        btnDisplay = Button(self.bottom,text="Display",width=12,font='Sans 12 bold')
        btnDisplay.grid(row=0,column=2,sticky=N,padx=10,pady=90)

        btnDelete = Button(self.bottom,text="Delete",width=12,font='Sans 12 bold')
        btnDelete.grid(row=0,column=2,sticky=N,padx=10,pady=130)

        
    def funcaddPeople(self):
        self.destroy()
        add_page = addpeople.AddPeople()
        
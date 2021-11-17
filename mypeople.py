from tkinter import *
from tkinter import Toplevel
import sqlite3
from tkinter import messagebox
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
        
        count = 0
        for person in persons:
            
            self.listbox.insert(count,str(person[0])+"-"+person[1]+" "+person[2])
            count +=1



        #Buttons......
        btnAdd = Button(self.bottom,text="Add",width=12,font='Sans 12 bold', command=self.funcaddPeople)
        btnAdd.grid(row=0,column=2,sticky=N,padx=10,pady=10)

        btnUpdate = Button(self.bottom,text="Update",width=12,font='Sans 12 bold', command=self.funcUpdate)
        btnUpdate.grid(row=0,column=2,sticky=N,padx=10,pady=50)

        btnDisplay = Button(self.bottom,text="Display",width=12,font='Sans 12 bold', command=self.funcDisplay)
        btnDisplay.grid(row=0,column=2,sticky=N,padx=10,pady=90)

        btnDelete = Button(self.bottom,text="Delete",width=12,font='Sans 12 bold', command=self.funcDelete)
        btnDelete.grid(row=0,column=2,sticky=N,padx=10,pady=130)

        
    def funcaddPeople(self):
        self.destroy()
        add_page = addpeople.AddPeople()
        
    def funcUpdate(self):
        global person_id
        selected = self.listbox.curselection()
        person = self.listbox.get(selected)
        person_id = person.split("-")[0]
        
        updatepage = Update()
        

    def funcDisplay(self):
        global person_id
        selected = self.listbox.curselection()
        person = self.listbox.get(selected)
        person_id = person.split("-")[0]
        
        displaypage = Display()
        self.destroy()

    def funcDelete(self):
        global person_id
        selected = self.listbox.curselection()
        person = self.listbox.get(selected)
        person_id = person.split("-")[0]

        mbox = messagebox.askquestion("warning","Are you sur to delete ?",icon='warning')
        if mbox == 'yes':
            try :
                query = "delete from persons where person_id=?"
                cur.execute(query,(person_id))
                con.commit()
                self.destroy()
                messagebox.showinfo("Success","Contact Deleted Successfully",icon='info')
                MyPeople()
            
        
            except:
                messagebox.showerror("Failed","Unable to delete",icon='error')
                self.destroy()

        
    

class Update(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry("650x750")
        self.title("Update Person")
        self.resizable(False,False)

        #get Person From Database
        global person_id
        person = cur.execute("select * from persons where person_id = ?",(person_id,))
        person_info = person.fetchall()
        self.id = person_info[0][0]
        self.name = person_info[0][1]
        self.surname = person_info[0][2]
        self.email = person_info[0][3]
        self.phone = person_info[0][4]
        self.address = person_info[0][5]

        #frames.......
        self.top=Frame(self,height=150,bg='white')
        self.top.pack(fill=X)

        self.bottom=Frame(self,height=600,bg='#fcc324')
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
        self.ent_name.insert(0,self.name)
        self.ent_name.place(x=150,y=45)

        #Surname
        self.lbl_surname = Label(self.bottom, text= "Surname", font='arial 15 bold' , fg='white', bg='#fcc324')
        self.lbl_surname.place(x=40,y=80)
        self.ent_surname = Entry(self.bottom, width=30, bd=4)
        self.ent_surname.insert(0,self.surname)
        self.ent_surname.place(x=150,y=85)

        #Email
        self.lbl_email = Label(self.bottom, text= "Email", font='arial 15 bold' , fg='white', bg='#fcc324')
        self.lbl_email.place(x=40,y=120)
        self.ent_email = Entry(self.bottom, width=30, bd=4)
        self.ent_email.insert(0,self.email)
        self.ent_email.place(x=150,y=125)

        #Phone
        self.lbl_Phone = Label(self.bottom, text= "Phone", font='arial 15 bold' , fg='white', bg='#fcc324')
        self.lbl_Phone.place(x=40,y=160)
        self.ent_phone = Entry(self.bottom, width=30, bd=4)
        self.ent_phone.insert(0,self.phone)
        self.ent_phone.place(x=150,y=165)

        #Address
        self.lbl_address = Label(self.bottom, text= "Address", font='arial 15 bold' , fg='white', bg='#fcc324')
        self.lbl_address.place(x=40,y=300)
        self.ent_address = Text(self.bottom, width=23, height=15, wrap=WORD)
        self.ent_address.insert('1.0',self.address)
        self.ent_address.place(x=150,y=200)

        button = Button(self.bottom, text='Update Person', command=self.updatePerson)
        button.place(x=270,y=460)
        self.lift()

    def updatePerson(self):
        person_id = self.id
        name = self.ent_name.get()
        surname =self.ent_surname.get()
        email = self.ent_email.get()
        phone = self.ent_phone.get()
        address = self.ent_address.get(1.0,'end-1c')

        try :
            query = "update persons set person_name=?, person_surname=?, person_email=?, person_phone=?, person_address=? where person_id=?"
            cur.execute(query,(name,surname,email,phone,address,person_id))
            con.commit()
            self.destroy()
            messagebox.showinfo("Success","Info Updated Successfully",icon='info')
            
        
        except:
            messagebox.showerror("Failed","Info Not Updated",icon='error')
            self.destroy()

        
class Display(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry("450x650")
        self.title("Update Person")
        self.resizable(False,False)

        #get Person From Database
        global person_id
        person = cur.execute("select * from persons where person_id = ?",(person_id,))
        person_info = person.fetchall()
        self.id = person_info[0][0]
        self.name = person_info[0][1]
        self.surname = person_info[0][2]
        self.email = person_info[0][3]
        self.phone = person_info[0][4]
        self.address = person_info[0][5]

        #frames.......
        self.top=Frame(self,height=150,bg='white')
        self.top.pack(fill=X)

        self.bottom=Frame(self,height=600,bg='#fcc324')
        self.bottom.pack(fill=X)

        #Heading........
        self.top_Image=PhotoImage(file='icons/bold.png')
        self.top_Image_Label = Label(self.top,image=self.top_Image,bg='white')
        self.top_Image_Label.place(x=120,y=10)
        self.heading = Label(self.top,text="Details",font='arial 15 bold',fg='#003f8a',bg='white')
        self.heading.place(x=260,y=60)
        
        #Scrollbar....
        self.sb = Scrollbar(self.bottom,orient=VERTICAL)


        #Name
        self.lbl_name = Label(self.bottom, text= "Name", font='arial 15 bold' , fg='white', bg='#fcc324')
        self.lbl_name.place(x=40,y=40)
        self.ent_name = Entry(self.bottom, width=30, bd=4)
        self.ent_name.insert(0,self.name)
        self.ent_name.config(state='disabled')
        self.ent_name.place(x=150,y=45)
        


        #Surname
        self.lbl_surname = Label(self.bottom, text= "Surname", font='arial 15 bold' , fg='white', bg='#fcc324')
        self.lbl_surname.place(x=40,y=80)
        self.ent_surname = Entry(self.bottom, width=30, bd=4)
        self.ent_surname.insert(0,self.surname)
        self.ent_surname.config(state='disabled')
        self.ent_surname.place(x=150,y=85)

        #Email
        self.lbl_email = Label(self.bottom, text= "Email", font='arial 15 bold' , fg='white', bg='#fcc324')
        self.lbl_email.place(x=40,y=120)
        self.ent_email = Entry(self.bottom, width=30, bd=4)
        self.ent_email.insert(0,self.email)
        self.ent_email.config(state='disabled')
        self.ent_email.place(x=150,y=125)

        #Phone
        self.lbl_Phone = Label(self.bottom, text= "Phone", font='arial 15 bold' , fg='white', bg='#fcc324')
        self.lbl_Phone.place(x=40,y=160)
        self.ent_phone = Entry(self.bottom, width=30, bd=4)
        self.ent_phone.insert(0,self.phone)
        self.ent_phone.config(state='disabled')
        self.ent_phone.place(x=150,y=165)

        #Address
        self.lbl_address = Label(self.bottom, text= "Address", font='arial 15 bold' , fg='white', bg='#fcc324')
        self.lbl_address.place(x=40,y=300)
        self.ent_address = Text(self.bottom, width=23, height=15, wrap=WORD)
        self.ent_address.insert('1.0',self.address)
        self.ent_address.config(state='disabled')
        self.ent_address.place(x=150,y=200)

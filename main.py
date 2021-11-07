from tkinter import * 
import datetime
date = datetime.date.today()


class Application(object):
    def __init__(self,master):
        self.master = master

        #frames.......
        self.top=Frame(master,height=150,bg='white')
        self.top.pack(fill=X)

        self.bottom=Frame(master,height=500,bg='#adff2f')
        self.bottom.pack(fill=X)

        #Heading........
        self.top_Image=PhotoImage(file='icons/book.png')
        self.top_Image_Label = Label(self.top,image=self.top_Image,bg='white')
        self.top_Image_Label.place(x=120,y=10)
        self.heading = Label(self.top,text="My Address Book",font='arial 15 bold',fg='#ffa500',bg='white')
        self.heading.place(x=260,y=60)
        self.date_lbl = Label(self.top,text="Today's Date: "+str(date),font='arial 12 bold',bg='white',fg='#ffa500')
        self.date_lbl.place(x=450,y=5)

        



def main():
    root = Tk()
    app = Application(root)
    root.title("Address Book App")
    root.geometry("650x550")
    root.resizable(False,False)
    root.mainloop()

if __name__ =='__main__':
    main()
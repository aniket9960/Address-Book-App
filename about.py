from tkinter import *

class About:
    def __init__(self,root):
        self.root = root

        frame = Frame(root,bg='#ffa500',width=550,height=550)
        frame.pack(fill=BOTH)
        text = Label(frame,text="this is Our About Us page"
                                "\nYou can find more information about us here"
                                "\nthis application was created for educational purpose"
                                "\nabd we have learned alot!"
                            ,font='arial 14 bold', bg='#ffa500', fg='white')
        text.place(x=35,y=50)

def main():
    root=Tk()
    app = About(root)
    root.title("About Us")
    root.geometry("550x550")
    root.resizable(False,False)
    root.mainloop()
    
if __name__ == '__main__':
    main()

from _tkinter import *
from tkinter import Toplevel
import sqlite3

con = sqlite3.connect('database.db')
cur = con.cursor()

class MyPeople(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry("650x650")
        self.title("My People")
        self.resizable(False,False)


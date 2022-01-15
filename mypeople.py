from tkinter import *
import datetime
date = datetime.datetime.now().date()
date= str(date)
import mysql.connector
from addpeople import AddPeople
con=mysql.connector.connect(host="localhost",user="root",passwd="9570",database="data")
cur=con.cursor()

class MyPeople(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)

        self.geometry("650x650+600+200")
        self.resizable(False,False)
        self.title("My People")
        
        self.top = Frame(self, height=150, bg='#58eb34')#pinkish
        self.top.pack(fill=X)

        self.bottom = Frame(self, height=500, bg='#9b34eb')#yelowish
        self.bottom.pack(fill=X)

        # top frame design
        self.heading = Label(self.top, text='Phonebook App>My People',font=' timesnewroman 25 bold', bg='#FF1D58', fg='#1CFF3C')
        self.heading.place(x=100, y=55)
        self.top_image = PhotoImage(file='icons/network.png')
        self.top_image_label = Label(self.top, image=self.top_image, bg='#FF1D58')
        self.top_image_label.place(x=20, y=40)
        self.date_lbl= Label(self.top, text="Today's Date"+date, font='arial 15 bold')
        self.date_lbl.place(x=400, y=110)

        self.scroll=Scrollbar(self.bottom, orient=VERTICAL)
        self.listBox = Listbox(self.bottom, width=50, height=27)
        self.listBox.grid(row=0, column=0, padx=(40,0))

        self.scroll.config(command=self.listBox.yview)
        self.listBox.config(yscrollcommand=self.scroll.set)
        self.scroll.grid(row=0, column=1, sticky=N + S)


        #buttons
        btnadd= Button(self.bottom, text="Add", width=12, font='Sans 15 italic', command=AddPeople)
        btnadd.grid(row=0, column=2, padx=(20,10), sticky=N)
        btnupd= Button(self.bottom, text=" Update" , width=12, font='Sans 15 italic')
        btnupd.grid(row=0, column=2, padx=20, pady=50, sticky=N)

        btndisplay= Button(self.bottom, text=" Display", width=12, font='Sans 15 italic')
        btndisplay.grid(row=0, column=2, padx=20, pady=90, sticky=N)

        btnDelte= Button(self.bottom, text=" Delete ", width=12, font='Sans 15 italic')
        btnDelte.grid(row=0, column=2, padx=20, pady=130 ,sticky=N)
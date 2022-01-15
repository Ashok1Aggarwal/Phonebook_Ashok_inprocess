from tkinter import *
import datetime
from tkinter import messagebox
date = datetime.datetime.now().date()
date = str(date)
import mysql.connector

con = mysql.connector.connect(host="localhost", user="root", passwd="9570", database="data")
cur = con.cursor()


class AddPeople(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)

        self.geometry("650x650+600+200")
        self.resizable(False, False)
        self.title("Add People")

        self.top = Frame(self, height=150, bg='#58eb34')  # pinkish
        self.top.pack(fill=X)

        self.bottom = Frame(self, height=500, bg='#9b34eb')  # yelowish
        self.bottom.pack(fill=X)

        # top frame design
        self.heading = Label(self.top, text='My People>Add People', font=' timesnewroman 25 bold', bg='#FF1D58',
                             fg='#1CFF3C')
        self.heading.place(x=100, y=55)
        self.top_image = PhotoImage(file='icons/network.png')
        self.top_image_label = Label(self.top, image=self.top_image, bg='#FF1D58')
        self.top_image_label.place(x=20, y=40)
        self.date_lbl = Label(self.top, text="Today's Date" + date, font='arial 15 bold')
        self.date_lbl.place(x=400, y=110)

        #name
        self.label_name= Label(self.bottom, text="Name", font='arial 15 bold')
        self.label_name.place(x=49, y=40)
        self.entry_name= Entry(self.bottom, width=30, bd=4)
        self.entry_name.insert(0,"")
        self.entry_name.place(x=200, y=40)

        #sursurname
        self.label_surname = Label(self.bottom, text="surname", font='arial 15 bold')
        self.label_surname.place(x=49, y=80)
        self.entry_surname = Entry(self.bottom, width=30, bd=4)
        self.entry_surname.insert(0, "")
        self.entry_surname.place(x=200, y=80)

        #email
        self.label_mail = Label(self.bottom, text="mail", font='arial 15 bold')
        self.label_mail.place(x=49, y=120)
        self.entry_mail = Entry(self.bottom, width=30, bd=4)
        self.entry_mail.insert(0, "")
        self.entry_mail.place(x=200, y=120)
        #phn numbr
        self.label_phn = Label(self.bottom, text="phone number", font='arial 15 bold')
        self.label_phn.place(x=49, y=160)
        self.entry_phn = Entry(self.bottom, width=30, bd=4)
        self.entry_phn.insert(0, "")
        self.entry_phn.place(x=200, y=160)
        #address
        self.label_addrss = Label(self.bottom, text="address", font='arial 15 bold')
        self.label_addrss.place(x=49, y=200)
        self.entry_addrss = Text(self.bottom, width=30, height=14)
        self.entry_addrss.place(x=200, y=200)
        #button
        button = Button(self.bottom, text="Add new Person", command=self.add_people)
        button.place(x=270, y=460)

    def add_people(self):
        name = self.entry_name.get()
        surname= self.entry_surname.get()
        email = self.entry_mail.get()
        phone_number = self.entry_phn.get()
        address = self.entry_addrss.get(1.0, 'end-1c')


        if name and surname and email and phone_number and address !="":
            try:
                con = mysql.connector.connect(host="localhost", user="root", passwd="9570", database="data")
                cur = con.cursor()
                cur.execute("insert into addressbook values(%s,%s,%s,%s,%s)",(name,
                                                                              surname,
                                                                              email,
                                                                              phone_number,
                                                                              address))
                con.commit()
                messagebox.showinfo("Succesfully added inormation")
            except Exception as e:
                messagebox.showerror("Error",str(e))
        else:
            messagebox.showerror("Fill all of the en`tries", icon='warning')


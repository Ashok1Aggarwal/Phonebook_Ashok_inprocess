from mypeople import MyPeople

from tkinter import *
import datetime
date = datetime.datetime.now().date()
date= str(date)
class Application(object):
    def __init__(self,master):
        self.master = master

        #frfames

        self.top = Frame(master, height=150, bg='#FF1D58')     #pinkish
        self.top.pack(fill=X)

        self.bottom = Frame(master, height=500, bg='#FFF685')  #yelowish
        self.bottom.pack(fill=X)

        # top frame design
        self.top_image = PhotoImage(file='icons/book.png')
        self.top_image_label = Label(self.top,image=self.top_image, bg='#FF1D58')
        self.top_image_label.place(x=80, y=40)
        self.heading = Label(self.top, text='Phonebook App',font=' housebound 25 bold', bg='#FF1D58', fg='#1CFF3C')
        self.heading.place(x=160, y=55)
        self.date_lbl= Label(self.top, text="Today's Date"+date, font='arial 15 bold')
        self.date_lbl.place(x=400, y=110)


        #btn 1 view people
        self.viewbutton = Button(self.bottom, text= "     My People    ", font='arial 15 bold italic', fg="blue", bg="orange",command=self.my_people)
        self.viewbutton.place(x=250, y=70)
        #btn 2 add people
        self.addbutton = Button(self.bottom, text= "Add new People", font='arial 15 bold italic', fg="blue", bg="orange")
        self.addbutton.place(x=250, y=150)

        #btn 3 about me
        self.abtusbutton = Button(self.bottom, text="      about Me     ", font='arial 15 bold italic', fg="blue", bg="orange")
        self.abtusbutton.place(x=250, y=230)

    def my_people(self):
        people =MyPeople()

def main():
    root = Tk()
    app = Application(root)
    root.title("ASHOK BOOK ")
    root.geometry("650x550+350+100")
    root.resizable(False,False)
    root.mainloop()



if __name__ == '__main__':
    main()
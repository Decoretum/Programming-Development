from tkinter import*
from PIL import Image, ImageTk
from tkinter.scrolledtext import*
import mysql.connector
import datetime








class NoteSystem:
    def __init__(self):
        self.count = 0
        self.edit = False
        self.date = datetime.datetime.now()

    def login(self):
        print("Hi!")


    def AddNote(self):
        if self.edit == False:
            self.count += 1
            Head = HeadTaker.get()
            BodyText = NoteTaker.get("1.0",END)
            BodyCanvas.insert(INSERT,"Entry {} in {} {}, {} at the time of {}".format(self.count,self.date.strftime('%b'),self.date.strftime('%d'),self.date.strftime('%Y'),self.date.strftime('%X')))
            BodyCanvas.insert(INSERT,"\n")
            BodyCanvas.insert(INSERT,"\n")
            BodyCanvas.insert(INSERT,Head)
            BodyCanvas.insert(INSERT,"\n")
            BodyCanvas.insert(INSERT,BodyText)
            BodyCanvas.insert(INSERT,"\n")

        else:
            pass

    
    def Edit(self):
        if self.edit == False:
            self.edit = True
            EditButton.configure(text="Stop Editing")
            print("Editing is active!") 
        else:
            self.edit = False
            EditButton.configure(text="Edit")
            print("Editing is inactive!")    



Gael = NoteSystem()

app = Tk()
app.title("Decoretum System")
app.geometry("1000x600")

myfont = ("Verdana",12)
label = Label(text="DecoreNotes", font=myfont)
label.grid(column=0,row=0,sticky=W,padx=10,pady=10)

Info = Label(text="This Applications serves to take down \nnotes and record them with headers!", font=myfont)
Info.grid(column=0, row=1,padx=10,pady=10)

label2 = Label(text="Create your notes through this form!", bg="#EEEEDF", font=myfont)
label2.place(x=650,y=20)

Container = Frame(app, bg="#F0F0F8")
Container.place(x=650,y=80)

headerlabel = Label(Container,text="Note Header", font=myfont)
headerlabel.grid(column=0,row=0,sticky=W,pady=20)

HeadTaker = Entry(Container, bg="#F0F0F8",font=myfont)
HeadTaker.grid(column=0,row=1,sticky=W,pady=10, columnspan=1)

Notelabel = Label(Container,text="Note Body", font=myfont)
Notelabel.grid(column=0,row=2,sticky=W,pady=20)

NoteTaker = ScrolledText(Container,width=30,height=10,bg="#F0F0F8",font=myfont)
NoteTaker.grid(column=0,row=3,sticky=W,columnspan=1)

BodyCanvas= Text(app,bg="#E8E8E8",font=myfont,width=40,height=50)
BodyCanvas.grid(column=0,row=2,padx=10,pady=10)

Submit = Button(Container, text="Add Note", command= Gael.AddNote)
Submit.grid(column=0,row=4,sticky=W)

EditButton = Button(Container, text="Edit", command= Gael.Edit)
EditButton.grid(column=0,row=4,columnspan=1,sticky=W,padx=75)



app.mainloop()
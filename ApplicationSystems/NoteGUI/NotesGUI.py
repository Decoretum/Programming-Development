from tkinter import*
from PIL import Image, ImageTk
from tkinter.scrolledtext import*
import mysql.connector
import datetime



myDB = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Cubil97823",
)

databasepresent = False
database1 = ''
cursor = myDB.cursor()
cursor.execute("show databases")

if ('gaeldatabase',) in cursor:
    print("Database is present!")
    databasepresent = True
    
else:
    cursor = myDB.cursor()
    cursor.execute("create database gaeldatabase")
    databasepresent = True

if databasepresent == True:
    database1 = "gaeldatabase"
    myDB = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Cubil97823",
    database = database1)
    print("Database functional!")




class NoteSystem:
    def __init__(self):
        self.edit = False
        self.date = datetime.datetime.now()
        self.highest = 0       

    def initializeData(self):
        BodyCanvas.delete('1.0',END)
        HeadTaker.delete(0,END)
        NoteTaker.delete('1.0',END)
        BodyCanvas.configure(bg="#EEEEEE")
        cursor = myDB.cursor()
        cursor.execute("show tables")
        tables = []
        x = ('Notes', )
        x1 = ('notes', )
        for i in cursor:
            tables.append(i)    

        if x in tables or x1 in tables:
            #print("Table is here!")
            cursor.execute('select * from Notes')
            allqueries = cursor.fetchall()
            max = 0

            for query in allqueries:
                if query[4] == None:
                    BodyCanvas.insert(INSERT,"Entry {}".format(query[0]))
                    BodyCanvas.insert(INSERT,"\n")
                    BodyCanvas.insert(INSERT,"Title: " + str(query[2]))
                    BodyCanvas.insert(INSERT,"\n")
                    BodyCanvas.insert(INSERT,"Content: " + str(query[1]))
                    BodyCanvas.insert(INSERT,"Created on: " + str(query[3]))
                    BodyCanvas.insert(INSERT,"\n")
                    BodyCanvas.insert(INSERT,"\n")

                else:
                    BodyCanvas.insert(INSERT,"Entry {}".format(query[0]))
                    BodyCanvas.insert(INSERT,"\n")
                    BodyCanvas.insert(INSERT,"Title: " + str(query[2]))
                    BodyCanvas.insert(INSERT,"\n")
                    BodyCanvas.insert(INSERT,"Content: " + str(query[1]))
                    BodyCanvas.insert(INSERT,"Created on: " + str(query[3]))
                    BodyCanvas.insert(INSERT,"\n")
                    BodyCanvas.insert(INSERT,"Modified on: " + str(query[4]))
                    BodyCanvas.insert(INSERT,"\n")
                    BodyCanvas.insert(INSERT,"\n")

                if query[0] > max:
                    max = query[0]

            self.highest = max 
            

        else:
            cursor.execute("create table Notes (NoteID smallint(10) not null, NoteBody varchar(2000) not null, NoteHeader varchar(100) not null, NoteDate varchar(100) not null, EditDate varchar(100), constraint note_pk primary key (NoteID))")
            print("Table created!")




    def AddNote(self):
        cursor = myDB.cursor()
        if self.edit == False:
            self.highest += 1
            Head = HeadTaker.get()
            BodyText = NoteTaker.get("1.0",END)
            Date = str(self.date.strftime('%b')) + ' ' + str(self.date.strftime('%d')) + ' ' + str(self.date.strftime('%Y')) + ' ' + str(self.date.strftime('%X'))
            SQL = "insert into notes values (%s, %s, %s, %s)"
            SQLvalues = (self.highest,BodyText,Head,Date)
            cursor.execute(SQL,SQLvalues)
            myDB.commit()
            HeadTaker.delete(0,END)
            NoteTaker.delete('1.0',END)
            self.initializeData()

        else:
            cursor.execute("select * from notes")
            queries = cursor.fetchall()
            TargetKey = KeyEntry.get()
            Head = HeadTaker.get()
            Body = NoteTaker.get('1.0',END)
            Date = str(self.date.strftime('%b')) + ' ' + str(self.date.strftime('%d')) + ' ' + str(self.date.strftime('%Y')) + ' ' + str(self.date.strftime('%X'))
            if Head.isspace():
                Head = ''

            if Body.isspace():
                Body = ''

            for query in queries:
                if str(query[0]) == TargetKey:
                    cursor = myDB.cursor()
                    SQL = "update notes set NoteHeader = %s, NoteBody =  %s where NoteID = %s"
                    SQLvalues = (Head,Body,query[0])
                    cursor.execute(SQL,SQLvalues)

                    SQL2 = "update notes set EditDate = %s where NoteID = %s"
                    SQLvalues2 = (Date,query[0])
                    cursor.execute(SQL2,SQLvalues2)

                    myDB.commit()
                    self.initializeData()
                else:
                    pass
            HeadTaker.delete(0,END)
            NoteTaker.delete('1.0',END)
            self.Edit()
                

            

    
    def Edit(self):
        if self.edit == False:
            self.edit = True
            EditButton.configure(text="Stop Editing")
            Submit.configure(text="Edit Entry")
            #print("Editing is active!") 
            Key = KeyEntry.get()
            cursor = myDB.cursor()
            cursor.execute("select * from notes")
            queries = cursor.fetchall()
            HeadTaker.delete(0,END)
            NoteTaker.delete("1.0",END)
            for query in queries:
                if str(query[0]) == str(Key):
                    HeadTaker.insert(INSERT,str(query[2]).rstrip())
                    NoteTaker.insert(INSERT,str(query[1]).rstrip())
            myDB.commit()

        else:
            self.edit = False
            HeadTaker.delete(0,END)
            NoteTaker.delete('1.0',END)
            EditButton.configure(text="Edit Entry")
            Submit.configure(text="Add Note")
            KeyEntry.delete(0,END)
            #print("Editing is inactive!")

    def Delete(self):
        cursor = myDB.cursor()
        DelValue = KeyEntry.get()
        if repr(DelValue) != "''":
            print("Entry {} is deleted".format(DelValue))
            SQL = "delete from notes where NoteId = {}".format(DelValue)
            cursor.execute(SQL)
            myDB.commit()

        self.initializeData()
        




Gael = NoteSystem()


app = Tk()
app.title("Decoretum System")
app.geometry("1100x700")
app.configure(bg='#CACAE1')

myfont = ("Verdana",12)
label = Label(text="DecoreNotes", font=myfont, bg="#EEEE79")
label.grid(column=0,row=0,sticky=W,padx=10,pady=10,ipadx=10,ipady=10)

Info = Label(text="This Applications serves to take down \nnotes and record them with headers!", font=myfont, bg="#BFBFEF")
Info.grid(column=0, row=1,padx=10,pady=10)

label2 = Label(text="Create your notes through this form!", bg="#BFBFEF", font=myfont)
label2.place(x=700,y=20)

Container = Frame(app, bg="#BFBFEF")
Container.place(x=700,y=80)

Disclaimer = Label(app, text="Created by Gael Estrera using \nPython and MySQL database", bg="#BFBFEF", font=myfont)
Disclaimer.place(x=700, y=500)

EditLabel = Label(app, text="Edit/Del. Entry using \nEntry Number", font=myfont, bg="#BFBFEF")
EditLabel.place(x=500,y=80)

KeyEntry = Entry(app, bg="#8787CE", font=myfont, width=10)
KeyEntry.place(x=550, y=130)

DeleteLabel = Button(app, text="Delete Entry", command=Gael.Delete, font=myfont, bg="#FFFFE4")
DeleteLabel.place(x=540,y=170)

EditButton = Button(app, text="Edit Entry", command= Gael.Edit, font=myfont, bg="#FFFFE4")
EditButton.place(x=540, y=220)

headerlabel = Label(Container,text="Note Header", font=myfont, bg="#BFBFEF")
headerlabel.grid(column=0,row=0,sticky=N,pady=20)

HeadTaker = Entry(Container, bg="#8787CE",font=myfont)
HeadTaker.grid(column=0,row=1,sticky=N,pady=10, columnspan=1)

Notelabel = Label(Container,text="Note Body", font=myfont, bg="#BFBFEF")
Notelabel.grid(column=0,row=2,sticky=N,pady=20)

NoteTaker = ScrolledText(Container,width=30,height=10,bg="#8787CE", fg="black",font=myfont)
NoteTaker.grid(column=0,row=3,sticky=NSEW,columnspan=1)


BodyCanvas = ScrolledText(app,font=myfont,width=45,height=30,bg="#EEEEEE")
BodyCanvas.grid(column=0,row=2,padx=10,pady=10)




Submit = Button(Container, text="Add Note", command= Gael.AddNote, font=myfont, bg="#FFFFE4")
Submit.grid(column=0,row=4,sticky=W)





app.after_idle(Gael.initializeData)
app.mainloop()
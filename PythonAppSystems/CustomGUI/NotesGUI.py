from tkinter import*
from PIL import Image, ImageTk
from tkinter.scrolledtext import*
import mysql.connector
import datetime



myDB = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Cubil97823",
    database = "gaeldatabase"
)


class NoteSystem:
    def __init__(self):
        self.count = -1
        self.edit = False
        self.date = datetime.datetime.now()
        self.highest = 0       

    def login(self):
        print("Hi!")

    def initializeData(self):
        BodyCanvas.delete('1.0',END)
        BodyCanvas.configure(bg="#EEEEEE")
        cursor = myDB.cursor()
        cursor.execute("show tables")
        tables = []
        x = ('notes', )
        for i in cursor:
            tables.append(i)    

        if x in tables:
            print("Table is here!")
            cursor.execute('select * from notes')
            allqueries = cursor.fetchall()
            max = 0

            for query in allqueries:
                BodyCanvas.insert(INSERT,"Entry {} from the date of {} ".format(query[0],query[3]))
                BodyCanvas.insert(INSERT,"\n")
                BodyCanvas.insert(INSERT,"Title: " + str(query[2]))
                BodyCanvas.insert(INSERT,"\n")
                BodyCanvas.insert(INSERT,"Content: " + str(query[1]))
                BodyCanvas.insert(INSERT,"\n")
                BodyCanvas.insert(INSERT,"\n")
                if query[0] > max:
                    max = query[0]
            self.highest = max 
            

        else:
            cursor.execute("create table Notes (NoteID smallint(10) not null, NoteBody varchar(200) not null, NoteHeader varchar(100) not null, NoteDate varchar(100) not null, constraint note_pk primary key (NoteID))")
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
            self.initializeData()

        else:
            cursor.execute("select * from notes")
            queries = cursor.fetchall()
            TargetKey = KeyEntry.get()
            Head = HeadTaker.get()
            Body = NoteTaker.get('1.0',END)
            if Head.isspace():
                Head = ''

            if Body.isspace():
                Body = ''

            print(Head)
            print(Body)
            for query in queries:
                if str(query[0]) == TargetKey:
                    cursor = myDB.cursor()
                    if Head != '' and Body == '':
                        print("1")
                        SQL = "update notes set NoteHeader = %s where NoteID = %s"
                        SQLvalues = (Head,query[0])
                        cursor.execute(SQL,SQLvalues)
        
                    elif Head != '' and Body != '':
                        print("2")
                        SQL = "update notes set NoteBody = %s where NoteID = %s"
                        SQLvalues = (Body,query[0])
                        SQL2 = "update notes set NoteHeader = %s where NoteID = %s"
                        SQLvalues2 = (Head,query[0])
                        cursor.execute(SQL,SQLvalues)
                        cursor.execute(SQL2,SQLvalues2)

                    elif Head == '' and Body != '':
                        print("3")
                        SQL = "update notes set NoteBody = %s where NoteID = %s"
                        SQLvalues = (Body,query[0])
                        cursor.execute(SQL,SQLvalues)

                    myDB.commit()
                    self.initializeData()
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

    def Delete(self):
        cursor = myDB.cursor()
        DelValue = KeyEntry.get()
        if repr(DelValue) != "''":
            print("something is deleted")
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
label.grid(column=0,row=0,sticky=W,padx=10,pady=10)

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

DeleteLabel = Button(app, text="Delete Entry", command=Gael.Delete)
DeleteLabel.place(x=550,y=180)

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




Submit = Button(Container, text="Add Note", command= Gael.AddNote)
Submit.grid(column=0,row=4,sticky=W)

EditButton = Button(Container, text="Edit", command= Gael.Edit)
EditButton.grid(column=0,row=4,columnspan=1,sticky=W,padx=75)



app.after_idle(Gael.initializeData)
app.mainloop()

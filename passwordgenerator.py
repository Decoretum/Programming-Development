from tkinter import*
from tkinter.scrolledtext import*
import random
import string

special_characters = ['"','!','@','#','$','%','^','&','*','(',')','-','+','?','_','=','<','>','/']
class passwordgen:
    def __init__(self):
        self.list=[]
    
    def create(self):
        self.list.clear()
        for x in range(12):
            chooser = random.randint(1,3)
            if chooser == 1:
                randomizerlet = random.choice(string.ascii_letters)
                x = randomizerlet 
                self.list.append(str(x))
            elif chooser == 2:
                randomizernum = random.randint(1,9)
                x = randomizernum
                self.list.append(str(x))  
            elif chooser ==3:
                randomizerchar = random.choice(special_characters)
                x = randomizerchar 
                self.list.append(str(x))


        final = ''.join(self.list)
        formed.delete(0, END)
        formed.insert(0, final)
        lists.insert(INSERT,final)
        lists.insert(INSERT,'\n')

gael = passwordgen()

password = Tk()
password.title('Password Generator')
password.geometry('300x300')

label1 = Label(password,text='Password Generator')
label1.grid(row=0,column=3,sticky=N)

formed = Entry(password,width=50,bg='#F0E68C',fg='#000000')
formed.configure(state='normal')
formed.grid(row=1,column=3)

generate = Button(password,text='Generate Password',command=gael.create)
generate.grid(row=2,column=3)

lists = ScrolledText(password, width=20,height=10)
lists.configure(state='normal')
lists.grid(row=3,column=3)





password.mainloop()
from cmath import sqrt
import time
set1 = [9.24,9.21,9.22,10.84,11.54]
set = [-5,1000000]
def av(set):
    yes = sum(set)/len(set)
    rounded = '{:.2f}'.format(yes)
    yes1 = float(rounded)
    return yes1


def truncateave(set):
    set.remove(max(set))
    set.remove(min(set))
    yes = sum(set)/len(set)
    rounded = '{:.2f}'.format(yes)
    yes1 = float(rounded)
    return yes1

def creation(set):
    print('\n')
    print('How many groups?')
    answer = int(input())
    print('\n')
    print('Displacement for x?')
    answer1 = int(input())
    print('\n')
    print('Displacement for y?')
    answer2 = int(input())
    print('\n')
    listset1 = []
    listset2 = []
    counter = 0
    
    if answer == 0:
        print('\n')
        print('0 is not a possible input')
        creation(set)
        
    while counter < answer and answer != 0:
        set[0] += answer1
        set[1] += answer2
        print(set)
        listset1.append(set[0])
        listset2.append(set[1])
        counter += 1
    if counter == answer and answer != 0:
        ave1 = sum(listset1)/len(listset1)
        ave2 = sum(listset2)/len(listset2)
        new = [ave1,ave2]
        return new

def timetest(x):
    print('I will print this',x)
    time.sleep(1)
    print('3')
    time.sleep(1)
    print('2')
    time.sleep(1)
    print('1')
    time.sleep(1)
    print('done!')

def hypotenuse(x,y):
    answer = sqrt((x*x) + (y*y))
    rounded = '{:.2f}'.format(answer)
    return rounded
    

class Mage:
    def __init__(self,a,b,c):
        self.available = ''
        self.magicbusy = ''
        self.physicbusy = ''
        self.classification = a
        self.magictype = b
        self.special = c
        self.magiclevel = 0
        self.powerlevel = 0
        self.school = 'Arcane University of Bladespire'
        
    def schoolcall(self):
        print('Wizarding School: ',self.school)
    def status(self):
        print('Magic level:',self.magiclevel)
        print('Strength level:',self.powerlevel)
        print('Specialization:',self.special)
    def __str__(self):
        return str(self.magictype) + ' ' + str(self.classification) + '\n' + 'Magic Specialization: ' + str(self.special) + '\n' + 'Magic level:' + ' ' + str(self.magiclevel) + '\n' + 'Strength level:' + ' ' + str(self.powerlevel) + '\n' + self.school + '\n'

    def express(self):
        print('Specialization:',self.intent)

    def magictraining(self):
        if self.magicbusy != 'not' and self.physicbusy != 'not':
            print('Improving', self.magictype, 'mastery for the',self.classification)
            print('Studying the Arcane arts in the university, temporary unavailable for battle')
            print('\n')
            self.magiclevel += 1
            self.magicbusy = 'not'
        elif self.magicbusy == 'not':
            print(self.magictype, self.classification, 'is currently taking mastery training already')
            print('\n')
        elif self.physicbusy == 'not':
            print(self.magictype, self.classification, 'is currently unavailable for magic training')
            print('Physical training and exercises are currently being conducted')
            print('\n')
        
    def physicaltraining(self):
        if self.magicbusy != 'not' and self.physicbusy != 'not':
            print(self.magictype, self.classification, 'is undergoing physical fitness exercises and demonstrations')
            print(self.magictype, self.classification, 'will be currently unavailable for other activities')
            print('\n')
            self.powerlevel += 1
            self.physicbusy = 'not'
        elif self.magicbusy == 'not':
            print(self.magictype, self.classification, 'is currently unavailable for physical training')
            print(self.magictype, 'mastery training is being conducted')
            print('\n')
        elif self.physicbusy == 'not':
            print(self.magictype, self.classification, 'is already conducting physical training and exercises')
            print('\n')
    def rest(self):
        if self.magicbusy == 'not':
            print(self.magictype, self.classification, 'has finished', self.magictype, 'mastery and will be available for other activities' )
            print('\n')
            self.magicbusy = ''
            
        elif self.physicbusy == 'not':
            print(self.magictype, self.classification, 'has finished physical training and exercises and will be available for other activities' )
            print('\n')
            self.physicbusy = ''

class Enemy(Mage):
    def __init__(self,a,b,c):
        super().__init__(a,b,c)
        
    

class Testparent:
    def __init__(self,x,y):
        self.test1 = x
        self.test2 = y
    def __str__(self):
        return str(self.test1) + ' ' + 'and' +  ' ' + str(self.test2)
    def noevent(self):
       print('Hello there')
    def honors(self):
        print('1st!')

class son(Testparent):
    def __init__(self,x,y):
        super().__init__(x,y)
    def honors(self):
        print('2nd!')

class daughter(Testparent):
    def __init__(self,x,y):
        super().__init__(x,y)
    def noevent(self):
        print('I\'m different')
        
class ampon(Testparent):
    pass
    
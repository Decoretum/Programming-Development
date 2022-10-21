import random
a = 'a = Generate digits'
b = 'b = Very easy math questions'
choices = a+'\n'+b
class Test():
    def __init__(self):
        self.counter = 0
        self.correct = 0
        self.choices()
    def generate(self):
        print('\n')
        print(self.counter)
        print('Please input anything here')
        answer = str(input())
        while True:
            if answer != '':
                self.counter += 1
                self.generate()
            elif answer == '':
                print('\n')
                self.choices()
    def solve(self):
        one = random.randint(1,50)
        two = random.randint(1,50)
        type = random.randint(1,2)
        
        if type == 1:
            resultadd = one + two
            print('\n')
            print(self.correct)
            print('What is {yes1} plus {yes2}'.format(yes1=one,yes2=two))
            answer = int(input())
            if answer == resultadd:
                self.correct += 1
                print('Correct!')
                self.solve()
            elif answer != resultadd:
                print('Wrong!')
                self.solve()
            elif answer == 'Finished':
                print(self.correct)
                self.choices
        if type == 2:
            resultmult = one * two
            print('\n')
            print(self.correct)
            print('What is {yes1} multiplied to {yes2}'.format(yes1=one,yes2=two))
            answer = int(input())
            if answer == resultmult:
                self.correct += 1
                print('Correct!')
                self.solve()
            elif answer != resultmult:
                print('Wrong!')
                self.solve()
            elif answer == 000:
                print(self.correct)
                self.choices()



    def choices(self):
        print('\n')
        print('Since this is a test, what shall we do for now?')
        print('Counter =',self.counter)
        print(choices)
        answer = str(input())
        if answer == 'a':
            self.generate()
        elif answer == 'b':
            self.solve()
Gael = Test()
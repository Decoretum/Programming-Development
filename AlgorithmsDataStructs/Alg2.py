def MergeSort(array):
    if len(array) > 1:
        middlepoint = len(array)//2
        Left = array[:middlepoint]
        Right = array[middlepoint:]

        #Recursive function to the halves
        print('about to do some division!')
        MergeSort(Left)
        MergeSort(Right)

        i=j=k=0

        #Sorting the arrays by using 3 pointers (2 subarrays, 1 main array)
        while i < len(Left) and j < len(Right):
            if Left[i] < Right[j]:
                array[k] = Left[i]
                i+=1
            else:
                array[k] = Right[j]
                j+=1
            k+=1

        #This is to ensure if there are leftover elements from either side
        while i < len(Left):
            array[k] = Left[i]
            i+=1
            k+=1
        
        while j < len(Right):
            array[k] = Right[j]
            i+=1
            j+=1
        
        print(array)

def recursiveTest(array,goal,mark):
    stringgoal = 'mark {}, add till {}'.format(mark, goal)
    if len(array) < goal:
        array.insert(len(array),stringgoal)
        mark += 1
        recursiveTest(array,goal,mark)
    else:
        print(array)

def recursiveInput(array,begin):
    goallength = 10
    goalvalue = 25
    if array[-1] < goalvalue:
        newbegin = begin +3
        array.insert(len(array),newbegin)
        recursiveInput(array,newbegin)
    else:
        print(array)


def recursiveMark(array):
    mark = 0
    check = 0
    counter = 0
    if counter == 0:
        for digit in array:
            if type(digit) is not str:
                array[array.index(digit)] = str(digit) + 'M' + str(mark)
                mark += 1
                check = 1
                counter = 1
                
    elif counter != 0:
        print('Time for recursion!')
        recursiveMark(array)

    else:
        print(array)



class TreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
    
    def setLeft(self,Data):
        self.left = TreeNode(Data)
    
    def setRight (self,Data):
        self.right = TreeNode(Data)

    def checkLeft(self):
        self.left != None
    
    def checkRight(self):
        self.right != None

    def Children(self):
        childrenlist = []
        childrenleft = []
        childrenright = []
        LeftCurrent = self.left
        RightCurrent = self.right
        leftcounter = ''
        childrenlist.append(LeftCurrent.data)
        childrenlist.append(RightCurrent.data)
        counter = 0
        while LeftCurrent:
            childrenlist.append(TakingChild(LeftCurrent))
            if LeftCurrent.checkRight():
                childrenlist.append(TakingChild(LeftCurrent.right))
            else:
                break
            LeftCurrent = LeftCurrent.left


        while RightCurrent:
            childrenlist.append(TakingChild(RightCurrent))
            if RightCurrent.checkLeft():
                childrenlist.append(TakingChild(RightCurrent.left))
            else:
                pass
            RightCurrent = RightCurrent.right
          

        flattened = []
        flattened.append(childrenlist[0])
        flattened.append(childrenlist[1])
        childrenlist.remove(childrenlist[0])
        childrenlist.remove(childrenlist[0])
        for sublist in childrenlist:
            for item in sublist:
                flattened.append(item)

        print(flattened)
    
    def checking(self):
        children = []
        children.append(TakeChild(self))
        #print(children)
        print(children)


def TakingChild(Node):
    children = []
    if Node.left:
        children.append(Node.left.data)
   
    if Node.right:
        children.append(Node.right.data)
    
    return children


def TakeChild(Node):
    children = []
    while Node.checkLeft():
        children.append(Node.left.data)
        TakeChild(Node.left)
        
    
    while Node.checkRight():
        children.append(Node.right.data)
        TakeChild(Node.right)
    
    
    return children

Gael = TreeNode(200)

Gael.setLeft(15)
Gael.setRight(10)

Gael.left.setRight(20)
Gael.left.setLeft(90)

Gael.left.right.setLeft(12)
Gael.left.right.setRight(11)

Gael.right.setLeft(40)
Gael.right.setRight(71)
Gael.right.left.setRight(13)
Gael.right.right.setLeft(41)
Gael.right.right.left.setLeft(80)
Gael.right.right.setRight(42)
Gael.right.right.right.setLeft(21)
Gael.right.right.right.setRight(22)

Gael.Children()
Gael.left.right.Children()
Gael.right.right.right.Children() #node 42
Gael.right.Children() #Node 10
Gael.right.right.Children() #Node 71

#Gael.right.Children()


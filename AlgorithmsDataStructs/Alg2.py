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


def RecursiveChildLeft(Node):
    leftchildren = []
    while Node.left:
        leftchildren.append(Node.left.data)
        Node = Node.left
        break

    return leftchildren

def RecursiveChildRight(Node):
    rightchildren = []
    while Node.right:
        rightchildren.append(Node.right.data)
        Node = Node.right
        break

    return rightchildren

class TreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
    
    def setLeft(self,Data):
        self.left = TreeNode(Data)
    
    def setRight (self,Data):
        self.right = TreeNode(Data)

    def Children(self):
        childrenlist = []
        childrenleft = []
        childrenright = []
        LeftCurrent = self.left
        RightCurrent = self.right
        childrenlist.append(LeftCurrent.data)
        childrenlist.append(RightCurrent.data)
        while LeftCurrent.left:
            childrenlist.append(RecursiveChildLeft(LeftCurrent))
            childrenlist.append(RecursiveChildRight(LeftCurrent))
            if LeftCurrent.right:
                childrenlist.append(RecursiveChildLeft(LeftCurrent.right))
                childrenlist.append(RecursiveChildRight(LeftCurrent.right))
            LeftCurrent = LeftCurrent.left


        while RightCurrent.right:
            childrenlist.append(RecursiveChildLeft(RightCurrent))
            childrenlist.append(RecursiveChildRight(RightCurrent))
            if RightCurrent.left:
                childrenlist.append(RecursiveChildLeft(RightCurrent.left))
                childrenlist.append(RecursiveChildRight(RightCurrent.left))
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


Gael = TreeNode(200)

Gael.setLeft(15)
Gael.setRight(10)

Gael.left.setRight(20)
Gael.left.setLeft(90)

Gael.left.right.setLeft(12)
Gael.left.right.setRight(11)

Gael.right.setLeft(40)
Gael.right.setRight(71)
Gael.right.right.setLeft(41)
Gael.right.right.left.setLeft(80)
Gael.right.right.setRight(42)
Gael.right.right.right.setLeft(21)
Gael.right.right.right.setRight(22)

Gael.Children()
Gael.right.right.right.Children() #node 42
Gael.right.Children() #Node 10

#Gael.right.Children()


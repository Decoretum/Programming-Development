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

    def Children(self):
        childrenlist = []
        childrenleft = []
        childrenright = []
        NodeLeft = self.left
        NodeRight = self.right
        while NodeLeft != None:
            childrenlist.append(NodeLeft.data)
            if NodeLeft.left != None:
                childrenlist.append(NodeLeft.left.data)
                childrenleft.append(NodeLeft.left.data)
            else:
                pass

            if NodeLeft.right != None:
                childrenlist.append(NodeLeft.right.data)
                childrenleft.append(NodeLeft.right.data)
            else:
                pass
            NodeLeft = NodeLeft.left

        while NodeRight != None:
            childrenlist.append(NodeRight.data)
            if NodeRight.left != None:
                childrenlist.append(NodeRight.left.data)
                childrenright.append(NodeRight.left.data)
            else:
                pass

            if NodeRight.right != None:
                childrenlist.append(NodeRight.right.data)
                childrenright.append(NodeRight.right.data)
            else:
                pass
            NodeRight = NodeRight.right

        print('Childrens from this Node: ', childrenlist)
        print('All children Nodes from the left: ', childrenleft)
        print('All children Nodes from the right: ', childrenright)


Gael = TreeNode(200)
Gael.setLeft(15)
Gael.setRight(10)
Gael.left.setRight(20)
Gael.right.setLeft(40)
Gael.Children()


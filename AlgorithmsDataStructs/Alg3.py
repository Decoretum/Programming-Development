#Node

class Node:
    def __init__(self, data = None, next=None): 
        self.data = data
        self.next = next

    def set_data(self, data):
        self.data = data

    def delete_data(self):
        self.data = None

    def set_next(self, next):
        self.next = next

    def unlink(self):
        self.next = None

    def get_data(self):
        return str(self.data)

    def get_next(self):
        return self.next

#linked List

class LinkedList:
    def __init__(self, head = None):
        self.head = head

    def is_empty(self):
        return self.head == None

    def get_head(self):
        return self.head if not self.is_empty() else None

    def print_list(self):
        if not self.is_empty():
            current = self.head
            result = current.get_data()

            while(current.next):
                current = current.next
                result = result + ", " + current.get_data()
        
            print(result)
        else:
            print("List is empty!")

    def add_element(self, data):
        # Create a node object for the new data
        newNode = Node(data)
        print("Node for " + str(newNode.get_data()) + " is created!")

        # Check if linked list is empty
        if not self.is_empty():
          # Set head node as current node
            current = self.head

          # Traverse the nodes until the last node is reached.  Last node is represented as next = None.
            while (current.next):
                current = current.next
            
          # Now at the last node, we assign the new node as the next node to the current end node, making the new node the new end node.
            current.set_next(newNode)
            print(current.get_next().get_data() + " is inserted to the list!")
            
        else:
            # Assign the new node as the head of the linked list
            self.head = newNode
            print(newNode.get_data() + " is assigned as the head of the list!")
            

    def insert(self, index, data):
        # Create a node object for the new data
        newNode = Node(data)

        # Check if linked list is empty
        if not self.is_empty():
          # Instantiate the counter
            i = 0
            
            # Set head node as current node and instantiate another for node i-1
            next = self.get_head()
            previous = None

          # Traverse the nodes until we arrive at the intended index
            while (next.next and i < index):
                previous = next
                next = next.next
                i += 1

          # Two scenarios: either we arrive at end of the link or not

          # Check if we are the end of the link or not
            if not next.next:
                previous.set_next(newNode)  # Step 1
                newNode.set_next(next)      # Step 2
                print(previous.next.get_data() + " is now inserted at index " + str(index) + "!")
            else:
                previous.set_next(newNode)  # Similar to add_element()
                newNode.set_next(next)
                print(previous.next.get_data() + " is added to the list!")

        else:
      # Assign the new node as the head of the linked list
          self.head = newNode
          print(newNode.get_data() + " is assigned as the head of the list!")
            
    def remove(self, index):
        verdict = ''
        if not self.is_empty():
            if index == 0:
                oldhead = self.head
                newhead = self.head.next
                self.head = newhead
                verdict = "Removed head {}".format(oldhead.get_data())
                oldhead.unlink()
                oldhead.delete_data()
            else:
                i = 0
                previous = None
                next = self.get_head()
                while(next.next and i<index):
                    previous = next
                    next = next.next
                    i+=1
                current = next
                newconnector = current.next
                verdict = "Node {} removed at position {}".format(current.get_data(),index)
                current.unlink()
                current.delete_data()
                previous.next = newconnector
        print(verdict)
        
    def pop(self):
        verdict = ''
        if not self.is_empty():
            now = self.head
            back = None
            while(now.next):
                back = now
                now = now.next
            verdict = "Node {} has been removed from the end of the linked list".format(now.get_data())
            current = now
            back.unlink()
            current.delete_data()
        print(verdict)
    
        

    def replace(self,node,index):
        nodej = Node(node)
        verdict = ''
        if not self.is_empty():
            if index == 0:
                oldhead = self.head
                newhead = self.head.next
                self.head = nodej
                self.head.next = newhead
                verdict = "Removed head {} and replaced it with Node {}".format(oldhead.get_data(),nodej.get_data())
                oldhead.unlink()
                oldhead.delete_data()
            else:
                i = 0
                previous = None
                next = self.get_head()
                while(next.next and i<index):
                    previous = next
                    next = next.next
                    i+=1
                current = next
                newconnector = current.next
                verdict = "Node {} replaced by Node {} at position {}".format(current.get_data(), nodej.get_data(),index)
                current.unlink()
                current.delete_data()
                previous.next = nodej
                nodej.next = newconnector
        print(verdict)



#Stack

class Stack:
    def __init__(self, head = None):
        self.head = head

    def is_empty(self):
        return self.head == None

    def peek(self):
        return self.head.get_data() if not self.is_empty() else print("Stack is empty!")

    def print_stack(self):
        if not self.is_empty():
            current = self.head
            result = current.get_data()

            while(current.next):
                current = current.next
                result = current.get_data() + " <-- " + result
        
            return result
        else:
            return "List is empty!"

    def push(self, data):
        # Create a node object for the new data
        newNode = Node(data)
        print("Node for " + str(newNode.get_data()) + " is created!")
    
        # Check if stack is empty
        if not self.is_empty():
            # Link the new node to the current head node
            newNode.set_next(self.head)

          # Set the new node as the new head node.
            self.head = newNode

            print(self.head.get_data() + " is pushed to the stack!")
        else:
            # Assign the new node as the head of the linked list
            self.head = newNode
            print(newNode.get_data() + " is assigned as the head of the stack!")

    def pop(self):
        # Check if linked list is empty
        if not self.is_empty():
            # Set head node as current node
            current = self.head

            # Assign the node next to current node as the new head node
            self.head = current.get_next()

            # Unlink the old head node from the link
            current.unlink()
        
            # Return the popped node
            print(current.get_data() + " is popped from the stack!")
            return current.get_data()
        else:
            print("Stack is empty!")




#Queue

class Queue:
    def __init__(self,head=None):
        self.head = head 
        self.tail = ''
            
    def is_empty(self):
        return self.head == None
    def peek(self):
        if not self.is_empty():
            return self.head.get_data()
        else:
            return "Queue is empty!"
    def push(self,node):
        newnode = Node(node)
        if not self.is_empty():
            current = self.head   
            previous = None
            while(current.next):
                previous = current
                current = current.next
            self.tail = current
            if self.tail == None:
                self.tail = newnode
                self.head.next = newnode
                print(newnode.get_data() + " is pushed to the Queue!")
                
            else:
                self.tail.set_next(newnode)
                print(newnode.get_data() + " is pushed to the Queue!")
        else:
            self.head = newnode
            print(newnode.get_data() + " is pushed to the Queue as the head!")
            
    def pop(self):
        if not self.is_empty():
            print("Node {} has been removed from the head!".format(self.head.get_data()))
            newhead = self.head.next
            self.head.unlink()
            self.head = newhead
        else:
            print("Queue is empty!")
            
            
    
    def print_queue(self):
        if not self.is_empty():
            current = self.head
            result = current.get_data()

            while(current.next):
                current = current.next
                result = current.get_data() + " <- " + result
            
            self.tail = current
            print(result)
        else:
            print("Queue is empty!")
        
    
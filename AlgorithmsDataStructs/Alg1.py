#we are tying to replicate nodes having connections and relationships with other nodes
#Connections and relationships affect interactions
class Human:
    def __init__(self,name,university,course,nationality):
        self.Name = name
        self.University = university
        self.Course = course
        self.Nationality = nationality
        self.Relationship = {}
        

    def Connection(self,Node,Relationship):
        self.Relationship[Node] = Relationship
        Node.Relationship[self] = Relationship

    def Mutual(self,Node):
        mutuals = []
        condition = 0
        for key1 in self.Relationship:
            for key2 in Node.Relationship:
                if key1 == key2:
                    condition = 1
                    mutuals.append(key1)
        if condition == 1:
            print('{}\'s Mutual/s with {}:'.format(self.getName(),Node.getName())) 
            for x in mutuals:
                print('{} as {} to {}'.format(x.getName(),Node.Relationship[x],Node.getName()))
        else:
            print('You, {}, have no mutual/s with {}'.format(self.getName(),Node.getName()))

    def SameSchool(self,Node):
        if Node.University == self.University:
            print('{} studies in the same University as you, {}'.format(Node.getName(),self.getName()))
        else:
            print('{} and you don\'t study at the same university. {} studies at {}'.format(Node.getName(),Node.getName(),Node.University))

    def getName(self):
        return self.Name

    def Relationships(self):
        for key in self.Relationship:
            print(key.getName() + ' --> ' + self.Relationship[key])

    def RelationshipChange(self,Node,Change):
        self.Relationship.update({Node : Change})

    




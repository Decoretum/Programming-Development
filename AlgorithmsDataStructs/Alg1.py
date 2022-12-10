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
        for key1 in self.Relationship:
            for key2 in Node.Relationship:
                if key1 == key2:
                    print('{} is a mutual as {} to {}'.format(key1.getName(),Node.Relationship[key1],Node.getName()))

    def getName(self):
        return self.Name

    def Relationships(self):
        for key in self.Relationship:
            print(key.getName() + ' --> ' + self.Relationship[key])

    def RelationshipChange(self,Node,Change):
        self.Relationship.update({Node : Change})




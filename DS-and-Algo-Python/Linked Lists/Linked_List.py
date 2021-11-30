class Node():
    
    def __init__(self,data):
        self.data=data
        self.next=None
        
class LinkedList():
    
    def __init__(self):
        self.head=None
        self.tail=self.head
        self.length=0
        
    def append(self,data):
        new_node=Node(data)
        if self.head==None:
            self.head=new_node
            self.tail=self.head
            self.length=1
        else:
            self.tail.next=new_node
            self.tail=new_node
            self.length+=1
    
    def prepend(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node
        self.length+=1
        
    def findNextValue(self,data):
        prev=self.head
        while prev.next.data!=data:
            prev=prev.next
        return prev
        
    def findNextPosition(self,position):
        prev=self.head
        for i in range(position-1):
            prev=prev.next
        return prev
            
    def insert(self,position,data):
        prev=self.findNextPosition(position)
        if position==0:
            self.prepend(data)
        elif position>=self.length:
            self.append(data)
        else:
            new_node=Node(data)
            new_node.next=prev.next
            prev.next=new_node
    
    def delete_by_value(self,data):
        prev=self.findNextValue(data)
        prev.next=prev.next.next
        
    def delete_by_position(self,position):
        prev=self.findNextPosition(position)
        prev.next=prev.next.next
        
    def printl(self):
        if self.head==None:
            print('Empty')
            
        current_node=self.head
        while current_node!=None:
            print(current_node.data,end='->')
            current_node=current_node.next
            
if __name__=='__main__':
    l = LinkedList()
    l.append(10)
    l.append(5)
    l.append(6)
    l.prepend(1)
    l.insert(2,99)
    l.insert(5,23)
    l.delete_by_value(23)
    l.delete_by_position(4)
    l.printl()
        
        
    
        
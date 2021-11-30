class Node():
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
        
class DoublyLinkedList():
    def __init__(self):
        self.head=None
        self.tail=None
        self.length=0
        
    def append(self,data):
        new_node=Node(data)
        if self.head==None:
            self.head=new_node
            self.tail=self.head
            self.length+=1
        else:
            self.tail.next=new_node
            new_node.prev=self.tail
            self.tail=new_node
            self.length+=1
            
    def prepend(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head.prev=new_node
        self.head=new_node
        self.length+=1
        
    def insert(self,position,data):
        new_node=Node(data)
        if position==0:
            self.prepend(data)
        if position>=self.length:
            self.append(data)
        else:
            current_node=self.head
            for i in range(position-1):
                current_node=current_node.next
            new_node.next=current_node.next
            current_node.next.prev=new_node
            current_node.next=new_node 
            new_node.prev=current_node
            self.length+=1
    
    def delete(self,dele):
        
        # Base Case
        if self.head==None or dele==None:
            return
        
        # If node to be deleted is head node
        if self.head==dele:
            self.head=self.head.next

        # Change next only if node to be deleted is NOT the last node
        if dele.next!=None:
            dele.next.prev=dele.prev
        
        # Change prev only if node to be deleted is NOT the first node
        if dele.prev!=None:
            dele.prev.next=dele.next
            
    def delete_by_value(self,value):
        current_node=self.head
        while current_node.next.data!=value and current_node.next!=None:
            current_node=current_node.next
        
        if current_node.next.data==value:
            self.delete(current_node.next)
        else:
            print('Given value not found.')
    
    def delete_by_position(self,position):
        current_node=self.head
        for i in range(position-1):
            current_node=current_node.next
        self.delete(current_node.next)    
            
    def printd(self):
        if self.head==None:
            return
        current_node=self.head
        while current_node!=None:
            print(current_node.data,end=' ')
            current_node=current_node.next

d=DoublyLinkedList()
d.append(10)
d.append(5)
d.append(6)
d.prepend(1)
d.insert(2,22)
d.delete_by_value(6)
d.delete_by_position(3)
d.printd()                        
            
            
            
            
            
            
            
            
            
            
            
            
        
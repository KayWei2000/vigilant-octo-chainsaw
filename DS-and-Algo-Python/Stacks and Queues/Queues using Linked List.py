class Node():
    def __init__(self,data):
        self.data=data
        self.next=None
    
class Queue():
    def __init__(self):
        self.first=None
        self.last=None
        self.length=0
    
    def peek(self):
        print(self.first.data)
    
    def enqueue(self,data):
        new_node=Node(data)
        if self.last==None:
            self.first=new_node
            self.last=new_node
            self.length+=1
        else:
            self.last.next=new_node
            self.last=new_node
            self.length+=1
    
    def dequeue(self):
        if self.first==None:
            return
        self.first=self.first.next
        self.length-=1
    
    def print_queue(self):
        current_node=self.first
        while(current_node):
            print(current_node.data,end='->')
            current_node=current_node.next
   
myq = Queue()
myq.enqueue('google')
myq.enqueue('microsoft')
myq.enqueue('facebook')
myq.enqueue('apple')
myq.peek()
myq.dequeue()
myq.print_queue()


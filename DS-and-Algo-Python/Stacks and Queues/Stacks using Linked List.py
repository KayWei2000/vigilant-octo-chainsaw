class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
class Stack:
    def __init__(self):
        self.top=None
        self.bottom=None
        self.length=0
    
    def peek(self):
        print(self.top.data)
    
    def push(self,data):
        new_node=Node(data)
        new_node.next=self.top
        self.top=new_node
        self.length+=1
    
    def pop(self):
        if self.top==None:
            return
        self.top=self.top.next
        self.length-=1
    
    def prints(self):
        current_node=self.top
        while current_node!=None:
            print(current_node.data,end='->')
            current_node=current_node.next

mystack=Stack()
mystack.push('google')
mystack.push('microsoft')
mystack.push('facebook')
mystack.push('apple')
mystack.peek()
mystack.pop()
mystack.prints()


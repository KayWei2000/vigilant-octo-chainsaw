class Stack:
    def __init__(self):
        self.array=[]
    
    def __str__(self):
        return str(self.__dict__) #<__main__.Stack object at 0x000001E97E298940>
    
    def peek(self):
        print(self.array[len(self.array)-1])
    
    def push(self,data):
        self.array.append(data)
    
    def pop(self):
        self.array.pop()
    
mystack=Stack()
mystack.push('google')
mystack.push('microsoft')
mystack.push('facebook')
mystack.push('apple')
mystack.peek()  
mystack.pop()
print(mystack)        
    
    
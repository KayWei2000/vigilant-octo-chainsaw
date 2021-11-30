class Queue():
    def __init__(self):
        self.s1=[]
        self.s2=[]
        
    def enqueue(self,data): # s1: 3->2->1 3->2->1->4×
        for i in range(len(self.s1)): 
            item=self.s1.pop() # s2: 1->2->3
            self.s2.append(item) # s1: 4
        self.s1.append(data) # s1: 4->3->2->1
        
        for i in range(len(self.s2)):
            item=self.s2.pop()
            self.s1.append(item)

    def dequeue(self):
        if len(self.s1)==0:
            return
        else:
            self.s1.pop()
                
    def print_queue(self):
        for i in range(len(self.s1)-1,0,-1):
            print(self.s1[i],end=' ')
        print(self.s1[0])
    
    def peek(self):
        print(self.s1[len(self.s1)-1])
    
my_queue = Queue()
my_queue.enqueue(2)
my_queue.enqueue(5)
my_queue.enqueue(0)
my_queue.peek()
my_queue.dequeue()
my_queue.print_queue()

# stack using array: 尾进尾出  stack using linked list:头进头出
# queue using linked list: 尾进头出 
class Array:
    def __init__(self):
        self.length=0
        self.data=dict()
    
    def __str__(self):
        return str(self.__dict__) 
    #This will print the attributes of the array class(length and data) in string format when print(array_instance) is executed
    
    def get(self,index):
       return self.data[index]
   
    def push(self,item):
        self.data[self.length]=item
        self.length+=1
      
    def pop(self):
        lastitem=self.data[self.length-1]
        del self.data[self.length-1]
        self.length-=1
        return lastitem
     
    def delete(self,index):
        deleteditem=self.data[index]
        for i in range(index,self.length-1):
            self.data[i]=self.data[i+1]
        
        del self.data[self.length-1]
        self.length-=1
        return deleteditem
    
arr=Array()
arr.push(3)
arr.push('hi')
arr.push(34)
arr.push(20)
arr.push('hey')
arr.push('welcome')
arr.delete(3)
arr.pop()
print(arr)
    
        
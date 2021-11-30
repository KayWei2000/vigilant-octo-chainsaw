class Hashtable:
    def __init__(self,size):
        self.size=size
        self.data=[None]*self.size

    def __str__(self):
        return str(self.__dict__)
    
    def hash(self,key):
        return len(key) % self.size
    
    def set(self,key,value):
        hash_value=self.hash(key)
        if not self.data[hash_value]:
            self.data[hash_value]=[[key,value]]
        else:
            self.data[hash_value].append([key,value])
        
    def get(self,key):
        hash_value=self.hash(key)
        for i in range(len(self.data[hash_value])):
            if self.data[hash_value][i][0]==key:
                return self.data[hash_value][i][1]
    
    def remove(self,key):
        hash_value=self.hash(key)
        for i in range(len(self.data[hash_value])):
            if self.data[hash_value][i][0]==key:
               del self.data[hash_value][i]
               return 
           
    def keys(self):
        for i in range(self.size):
            if self.data[i]:
                for j in range(len(self.data[i])):
                    print(self.data[i][j][0])   
    
    def values(self):
        for i in range(self.size):
            if self.data[i]:
                for j in range(len(self.data[i])):
                    print(self.data[i][j][1])
                
h=Hashtable(2)
print(h)
#{'size': 2, 'data': [None, None]}

h.set('one',1)
h.set('two',2)
h.set('three',3)
h.set('four',4)
h.set('five',5)
print(h)
#{'size': 2, 'data': [[['four', 4], ['five', 5]], [['one', 1], ['two', 2], ['three', 3]]]}

print(h.get('one'))
#1

h.remove('one')
print(h)
#{'size': 2, 'data': [[['four', 4], ['five', 5]], [['two', 2], ['three', 3]]]}
                
h.keys()
'''four
five
two
three'''

h.values()
'''4
5
2
3'''                
    
    
                    
        
    
    
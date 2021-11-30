class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        
class BST:
    def __init__(self):
        self.root=None
    
    def insert(self,data):
        new_node=Node(data)
        if self.root==None:
            self.root=new_node
            return
        current_node=self.root
        while True:
            if current_node.data<data:
                if current_node.left==None:
                    current_node.left=new_node
                else:
                    current_node=current_node.left
            if current_node.data>data:
                if current_node.left==None:
                    current_node.right=new_node
                else:
                    current_node=current_node.right
                    
    def search(self,data):
        current_node=self.root
        while True:
            if current_node==None:
                return 'Not Found'
            if current_node.data==data:
                return 'Found'
            if current_node.data>data:
                current_node=current_node.left
            else:
                current_node=current_node.right  

    def BFS(self): # result记录结果 queue退根节点 进左右孩子
        current_node=self.root
        BFS_result=[] 
        queue=[] 
        queue.append(current_node)
        
        while queue:
            BFS_result.append(queue.pop(0))
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)
        return BFS_result
    
    def Recursive_BFS(self,queue,BFS_result):
       current_node=self.root
       BFS_result.append(queue.pop(0))
       if queue==None:
           return BFS_result
       if current_node.left:
           queue.append(current_node.left)
       if current_node.right:
           queue.append(current_node.right)
           return self.Recursive_BFS(queue,BFS_result)
            
        
        
my_bst = BST()
my_bst.insert(5)
my_bst.insert(3)
my_bst.insert(7)
my_bst.insert(1)
my_bst.insert(13)
my_bst.insert(65)
my_bst.insert(0)
my_bst.insert(10)
print(my_bst.BFS())
print(my_bst.Recursive_BFS([my_bst.root], []))
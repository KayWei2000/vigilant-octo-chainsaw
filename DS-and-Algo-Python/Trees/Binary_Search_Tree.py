class Node():
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        
class BinarySearchTree:
    def __init__(self):
        self.root=None
    
    def insert(self,data):
        new_node=Node(data)
        if self.root==None:
            self.root=new_node
        else:
            current_node=self.root
            while True:
                if data<current_node.data:
                    if current_node.left==None:
                        current_node.left=new_node
                    else:
                        current_node=current_node.left
                elif data>current_node.data:
                    if current_node.right==None:
                        current_node.right=new_node
                    else:
                        current_node=current_node.right
                

    def lookup(self,data):
        current_node=self.root
        while True:
            if current_node==None:
                return False
            if current_node.data==data:
                return True
            elif current_node.data>data:
                current_node=current_node.left
            else:
                current_node=current_node.right
    
    def print_tree(self):
        if self.root!=None:
            self.printt(self.root)
    #Inorder Traversal       
    def printt(self,current_node):
        if current_node!=None:
            self.print(current_node.left)
            print(str(current_node.data))
            self.print(current_node.right)
              
my_bst = BinarySearchTree()
my_bst.insert(5)
my_bst.insert(3)
my_bst.insert(7)
my_bst.insert(1)
my_bst.insert(13)
my_bst.insert(65)
my_bst.insert(0)
my_bst.insert(10)
my_bst.print_tree()
                            
    
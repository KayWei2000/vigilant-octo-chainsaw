from Binary_Search_Tree import Node,BinarySearchTree

def printInorder(root):
    if root:
        printInorder(root.left)
        
        print(root.data)
        
        printInorder(root.right)
        
def printPostorder(root):
    if root:
        printPostorder(root.left)
        
        printPostorder(root.right)
        
        printPostorder(root)
        
def printPreorder(root):
    if root:
        print(root)
        
        printPreorder(root.left)
        
        printPreorder(root.right)
        
my_bst = BinarySearchTree()
my_bst.insert(5)
my_bst.insert(3)
my_bst.insert(7)
my_bst.insert(1)
my_bst.insert(13)
my_bst.insert(65)
my_bst.insert(0)
my_bst.insert(10)

printInorder(my_bst)

    
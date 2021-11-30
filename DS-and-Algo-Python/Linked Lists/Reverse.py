from Linked_List import Node,LinkedList
            
my_linked_list = LinkedList()
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)
my_linked_list.append(6)

def reverse(self):
        if self.length<=1:
            return self
        else:
            current_node=self.head
            prev_node=None
            self.tail=self.head
            while current_node:
                next_node=current_node.next #保存下一个结点地址
                current_node.next=prev_node #反转
                prev_node=current_node #更新
                current_node=next_node #更新
            self.head=prev_node
            return self

reversed_linked_list=reverse(my_linked_list)
reversed_linked_list.printl()





        
            
        
        
        
        
        
        
        
        
        
        

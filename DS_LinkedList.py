
#<-----------------------------------------------Linked list creation------------------------------------------------------------->
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
        self.last_node = None
    def display(self):
        current = self.head
        while current:
            print(current.data,"-->",end="")
            current = current.next
    def insert_start(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        
        if self.last_node is None:
            self.last_node = self.head
    def insert_end(self,data):
        if self.head is None:
            self.head = Node(data)
            self.last_node = self.head
        else:
            self.last_node.next = Node(data)
            self.last_node = self.last_node.next
    def remove(self,target):
        if self.head is None:
            return None
        if self.head.data == target:
            self.head = self.head.next
            return self.display()
        current = self.head
        while current.next:
            if current.data == target:
                current.next = current.next.next
            current = current.next
    
LL = LinkedList()
LL.insert_start(100)
LL.insert_start(200)
LL.insert_end(50)
LL.display()

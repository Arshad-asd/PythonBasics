
#<-----------------------------------------------Linked list Node create------------------------------------------------------------->

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

#<-----------------------------------------------Linked list creation------------------------------------------------------------->
class LinkedList:
    def __init__(self):
        self.head = None
        self.last_node = None
    def display(self):
        current = self.head
        while current:
            print(current.data,"-->",end="")
            current = current.next
        print("None")
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
    def find_len(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next
        return count
# LL = LinkedList()
# LL.insert_start(100)
# LL.insert_start(200)
# LL.insert_end(50)
# LL.insert_end(100)
# LL.display()
#<-----------------------------------------------Linked list to DELETE elment particular POSTION------------------------------------------------------------->

class PostionDelete(LinkedList):
    def delete(self,postion):
        current = self.head
        index = 0
        if self.head is None:
            print("Empty list")
            return 
        while current and index < postion-1:
            prev = current
            current = current.next
            index += 1
        if current is None:
            print("Position out of boundary")
            return
        elif index == 0:
            self.head = self.head.next
        else:
            prev.next = current.next
# postde = PostionDelete()
# postde.insert_end(100)
# postde.insert_start(50)
# postde.insert_start(200)
# postde.insert_start(100)
# postde.delete(2)
# postde.display()
#<-----------------------------------------------Linked list Find duplicate------------------------------------------------------------->
class FindDuplicate(LinkedList):
    def duplicates(self):
        current = self.head
        seen_values = set()
        duplicates_list = []

        while current:
            if current.data in seen_values:
                duplicates_list.append(current.data)
            else:
                seen_values.add(current.data)
            current = current.next
        return duplicates_list

    def display_duplicates(self):
        duplicates_list = self.duplicates()
        print("Duplicates:", end=" ")
        for value in duplicates_list:
            print(value, "-->", end="")
        print()
# find_dup = FindDuplicate()
# find_dup.insert_end(100)
# find_dup.insert_start(50)
# find_dup.insert_start(200)
# find_dup.insert_start(100)
# find_dup.display_duplicates()
#<-----------------------------------------------Linked list Remove Nth Node From End of List------------------------------------------------------------->
class Remove(LinkedList):
    def remove_nth(self,n):
        length = self.find_len()
        index = 0
        current = self.head
        while current and index < length-n:
            prev = current
            current = current.next
            index += 1
        if current is None:
            return []
        elif current == 0:
            self.head = self.head.next
        else:
            prev.next = current.next

# ll =Remove()
# ll.insert_start(50)
# ll.insert_start(200)
# ll.insert_start(100)
# ll.insert_start(90)
# ll.insert_start(40)
# ll.insert_start(70)
# ll.display()
# ll.remove_nth(2)
# ll.display()
# #<-----------------------------------------------How Would You Detect a Cycle in a Linked List?------------------------------------------------------------->
class FloydsCycle(LinkedList):
    def has_cycle(self):
        if not self.head or not self.head.next:
            return False
        slow = self.head
        fast = self.head.next
        while fast and fast.next:
            if slow == fast:
                return True
            slow = slow.next
            fast = fast.next.next
        return False

ll =FloydsCycle()
ll.insert_start(50)
ll.insert_start(200)
ll.insert_start(100)
ll.insert_start(90)
ll.insert_start(40)
ll.insert_start(70)
ll.head.next.next.next.next.next = ll.head.next
cycle = ll.has_cycle()
print(f"its cycle {cycle}")
#<--------------


'''
What is a Linked List? :-
A linked list is a data structure that consists of a sequence of elements, where each element (referred to as a node) contains data and a reference (or link)
to the next node in the sequence. Unlike arrays, linked lists do not require contiguous memory allocation, allowing for efficient insertions and deletions.

Types of Linked Lists :-
* Singly Linked List: Each node contains data and a reference to the next node.
* Doubly Linked List: Each node contains data, a reference to the next node, and a reference to the previous node.
* Circular Linked List: In this variant, the last node points back to the first node, forming a circle.

Use Case of Linked Lists :-
* Dynamic Memory Allocation: Linked lists can easily grow and shrink in size by adding or removing nodes, making them suitable for applications where the size of
the data structure is not known in advance.

* Efficient Insertions/Deletions: Linked lists allow for efficient insertions and deletions, particularly in scenarios where these operations occur frequently, 
such as in implementing stacks, queues, and other dynamic data structures.  

*Real-time Applications: Linked lists are used in real-time applications where memory constraints are tight and dynamic memory management is crucial, 
such as in operating systems and embedded systems.

Basic Operations and Time Complexity :-
Insertion

At the beginning: O(1)
At the end: O(n) for singly linked lists (O(1) if tail pointer is maintained), O(1) for doubly linked lists with a tail pointer.
At a specific position: O(n)
Deletion

From the beginning: O(1)
From the end: O(n) for singly linked lists, O(1) for doubly linked lists with a tail pointer.
From a specific position: O(n)
Traversal: O(n)

Search: O(n)

Practicals :- 
1 . Node Intialize
2 . Linked List Creation,Traversing,Insert_start,Insert_end,Find_len 
3 . Add Element Particular Postion
4 . Remove Element Particular Postion
5 . Find Duplicate
6 . Remove Nth Node From End of List
7 . Detect a Cycle in a Linked List
8 . Find Midile Linked Lis
9 . Sort Linked List
'''


#<----------------------------------------------1-Linked list Node create------------------------------------------------------------->

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

#<----------------------------------------------2-Linked list creation------------------------------------------------------------->
class LinkedList:
    def __init__(self):
        self.head = None
        self.last_node = None
    def traverse(self):
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
        while current and current.next:
            if current.data == target:
                current.next = current.next.next
                if not current.next:
                    current.next = self.last_node
            else:
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
# LL.traverse()

#<----------------------------------------------3-Linked list to Add elment particular POSTION------------------------------------------------------------->
class PossitionAdd(LinkedList):
    def add_specific(self, val, position):
        if position < 0:
            return "wrong position"
        new_node = Node(val)

        if position == 0:
            new_node.next = self.head
            self.head = new_node
            if self.last is None:
                self.last = new_node
        current = self.head
        index = 0
        while current and index < position-1:
            current = current.next
            index +=1
        if current is None:
            return "Index out of range"
        new_node.next = current.next
        current.next = new_node

#<----------------------------------------------4-Linked list to DELETE elment particular POSTION------------------------------------------------------------->

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
#<----------------------------------------------5-Linked list Find duplicate------------------------------------------------------------->
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
#<----------------------------------------------6-Linked list Remove Nth Node From End of List------------------------------------------------------------->
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
# #<----------------------------------------------7-How Would You Detect a Cycle in a Linked List?------------------------------------------------------------->
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
#<----------------------------------------------8-How Would You Find Midile Linked List?------------------------------------------------------------->
class Middle(LinkedList):
    def find_middle(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.data

Midd = Middle()
Midd.insert_start(50)
Midd.insert_start(200)
Midd.insert_start(100)
Midd.insert_start(90)
Midd.insert_start(40)
Midd.insert_start(70)
res = Midd.find_middle()
print(res)

#<----------------------------------------------9-How Would You Sort Linked List?------------------------------------------------------------->

def buble_sorting(self):
    outer = self.head
    while outer:
        inner = self.head
        while inner and inner.next:
            if inner.val > inner.next.val:
                temp = inner.next.val
                inner.next.val = inner.val
                inner.val = temp
            else:
                inner = inner.next
        outer = outer.next
    return self.traverse()

#<----------------------------------------------9-How Would You Reverse Linked List?------------------------------------------------------------->
class ReverseLL(LinkedList):
    def reverse(self):
        current = self.head
        prev = None
        while current:
            new_node = current.next
            current.next = prev
            prev = current
            current = new_node
        self.head = prev

ll = ReverseLL()
ll.insert_start(10)
ll.insert_end(20)
ll.insert_end(30)
ll.traverse()
ll.reverse()
ll.traverse()

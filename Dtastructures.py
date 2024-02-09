
                                  #BASIC INBUILT DATA STRUCTURES OPERATIONS


# creating  and indexin string
"""
x = 'frog'
print(x[3])
#list
x=['pig','cow','horse']
#tuple
x = ('kevin','niklas','jenny','craiag')
print(x[0])
"""
# slicing
"""  
x = 'computer'
print(x[1:4])
print(x[1:6:2])
print(x[3:])
print(x[:5])
print(x[-1])
print(x[-3:])
print(x[:-2])
"""
# adding/concatenating
# string
"""
x ='horse' + 'shoe'
print(x)
#list
y=['pig','cow'] + ['horse']
print(y)
#tuple
z=('kevin','niklas','jenny') + ('craig',)
print(z)
"""
# multiplaying
# string
"""
x = 'bug'*3
print(x)
#list
y = [8,5]*3
print(y)
#tuple
z = (2,4)*3
print(z)
"""
# checking membership
# string
"""
x = 'bug'
print('u' in x)
#list
y = ['pig','cow','horse']
print('cow' not in y)
#tuple
z = ('kevin','niklas','jenny','craiag')
print('niklas' in z)
"""
# itreing item
"""
x = [7,8,3]
for item in x:
    print(item)
#index and item
y = [7,8,3]
for index,item in enumerate(y):
    print(index,item)
"""
# number of items
# string
"""
x = 'bug'
print(len(x))
#list
y = ['pig','cow','horse']
print(len(y))
#tule
z = ('kevin','niklas','jenny','craig')
print(len(z))
"""
# minium
# string
""""
x = 'bug'
print(min(x))
#list
y = ['pig','cow','horse']
print(min(y))
#tuple
z = ('kevin','niklas','jenny','craig')
print(min(z))
"""
# maximum
# string
"""
x = 'bug'
print(max(x))
#list
y = ['pig','cow','horse']
print(max(y))
#tuple
z = ('kevin','niklas','jenny','craig')
print(max(z))
"""
# sum
"""
#string
#x = [5,7,'bug']   #unsported oprend type error
#print(sum(x))
#list
y = [2,5,6,8]
print(sum(y))
#tuple
z = (50,60,70,80)
print(sum(z))
"""
# sorting
# string
"""
x = 'bug'
print(sorted(x))
#list
y = ['pig','cow','horse']
print(sorted(y))
#tuple
z = ('kelvin',' niklas','jenny','craig')
print(sorted(z))
"""
# sorting by second letter
# tuple
"""
z = ('kelvin','niklas','jenny','craig')
print(sorted(z,key=lambda k : k[1]))
"""
# count
# string
"""
x = 'hippo'
print(x.count('p'))
#list
y = ['cow','pig','horse']
print(y.count('cow'))
#tule
z = ('kelvin','niklas','jenny','craig')
print(z.count('jenny'))
"""
# index(item)
"""
#string
x = 'hippo'
print(x.index('p'))
#list
y = ['horse','cow','pig']
print(y.index('cow'))
#tuple
z = ('kelvin','niklas','jenny','craig')
print(z.index('jenny'))
"""
# 1.cunstrctors in list
"""
x = list()
y = ['a',25,'dog',8.43]
tuple1 = (10,20)
z = list(tuple1)
print(z)
#1.1.list compreshension
a = [m for m  in range(8)]
print(a)
b = [i**2 for i in range(10) if i > 4]
print(b)
#1.2 delete
x = [5,3,8,6]
del(x[2])
print(x)
#1.3.append
x.append(7)
print(x)
#extend
y = [12,3]
x.extend(y)
print(x)
#insert
x.insert(1,9)
print(x)
x.insert(1,['a','m'])
print(x)
#remove
x.remove(3)
print(x)
#reverse
x.reverse()
print(x)
#sort
x = [5,3,5,6]
x.sort()
print(x)
"""
# constuctor Tuples
"""
x = ()
x = (1,2,3)
x = 2,
print(x)
print(x,type(x))
list1 = [2,4,6]
x = tuple(list1)
print(x,type(x))
#deletion tuple
#del(x[1]) #is immutable
#x[1]=8 #fails
y = ([1,2],3)#delete the 2
del(y[0][1])
print(y)
y+=(4,)#concatenating two string
print(y)
"""
# 1.cunstructors in set
"""
x = {3,5,3,5}
print(x)
y = set(x)
print(y)
list1 = [2,4,6]
z = set(list1)
print(z)
#1.1 opreations
x = {3,8,5}
print(x)
x.add(7)
print(x)
x.remove(3)
print(x)
#get length f set x
print(len(x))
#check membership in x
print(5 in x)
#pop random item from set x
print(x.pop(),x)
#delete all items from set x
x.clear()
print(x)
"""
# mathamatical set operations
""""
s1 = {1,2,3}
s2 = {3,4,5}
print(s1 & s2)
print(s1 | s2)
print(s1 ^ s2)
print(s1 _ s2)
print(s1)
"""


                    #WEEK-4               # singly linked list creation
"""
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class linkedlist:
    def __init__(self) :
       self.head = None
       self.last_node = None
    def add(self,data):
        if self.last_node is None:
           self.head = Node(data)
           self.last_node = self.head
        else:
            self.last_node.next = Node(data)
            self.last_node = self.last_node.next
    def display(self):
        current = self.head
        while current is not None:
            print(current.data,'-->',end="")
            current = current.next
l = linkedlist()
l.add(10)
l.add(90)
l.add(20)
l.display()
"""

                                      # doubly linked list
"""
class Node:
     def __init__(self,data) :
          self.previous = None
          self.data = data
          self.next = None
class DoublyLL:
     def __init__(self):
          self.head = None
          self.start_node = None
          self.last_node = None
     def add(self,data):
        if self.last_node is None:
             self.head = Node(data)
             self.last_node = self.head
        else:
             new_node = Node(data)
             self.last_node.next = new_node
             new_node.previous = self.last_node
             new_node.next = None
             self.last_node = new_node
     def diaplay(self,Type):
        if Type == 'Left_to_right':
           current = self.head
           while current is not None:
               print(current.data,'-->',end="")
               current = current.next
           print()
        else:
            current = self.last_node
            while current is not None:
                  print(current.data,'-->',end="")
                  current = current.previous
Dll = DoublyLL()
Dll.add(10)
Dll.add(20)
Dll.add(60)
Dll.diaplay('Left_to_right')
Dll.diaplay('Right_to_left')
"""

                                  # array to linked list
""""
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
def array_to_LL(array):
    head = Node(array[0])
    current = head
    for i in range(1,len(array)):
        new_node = Node(array[i])
        current.next = new_node
        current = new_node
    return head
array = [50,90,30,20]
head = array_to_LL(array)
current = head
while current:
    print(current.data,'-->',end='')
    current = current.next
    """

                                   # add node at end and begining
"""
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None
        self.last = None

    def add_begining(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        if self.last == None: # If LinkedList is empty
            self.last = new_node # Or this can be written as "self.last = self.head"

    def add_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node

    def display(self):
        if self.head is None:
            print('[Linked list is empty]')
            return
        else:
            current = self.head
            while current is not None:
                print(current.data, " --> ", end="")
                current = current.next
            print()


LL = LinkedList()
LL.display()
# LL.add_begining(10)
# LL.add_begining(90)
LL.add_end(60)
LL.add_end(80)
LL.display()
"""


                                       #delte a node  given position
"""
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class linkeslist:
    def __init__(self):
        self.head = None
        self.last = None
    def add(self,data):
        new_node = Node(data)
        if self.last is None:
          new_node.next = self.head
          self.head = new_node
          self.last = self.head
        else:
            self.last.next = new_node
            self.last = self.last.next
    def delete(self,position):
        if self.head is None:
           print('list is emphty')
           return
        index = 0
        current = self.head
        while current.next and index < position:
            previus = current
            current = current.next
            index += 1
        if index < position:
            print('out of boundary')
        elif index == 0:
            self.head = self.head.next
        else:
            previus.next = current.next
    def display(self):
        current = self.head
        while current is not None:
            print(current.data,'-->',end="")
            current = current.next

ll = linkeslist()
ll.add(30)
ll.add(80)
ll.add(70)
ll.add(45)
ll.delete(1)
ll.display()
"""


                                         # add element at specified position
"""
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class linkedlist:
    def __init__(self):
        self.head = None
        self.last = None
    def add(self,data):
        new_node = Node(data)
        if self.last is None:
            new_node.next = self.head
            self.head = new_node
            self.last = self.head
        else:
            self.last.next = new_node
            self.last = self.last.next
    def add_specigfied(self,data,Position):
        new_node = Node(data)
        index = 0
        current = self.head
        while current.next and index <Position:
            previos = current
            current = current.next
            index +=1
        if index < Position:
            print('out of boundary')
        elif index == 0:
            self.head = new_node
            new_node.next = current
        else:
            new_node.next = previos.next
            previos.next = new_node
    def display(self):
        if self.head is None:
            print("list is emphty")
        current = self.head
        while current is not None:
            print(current.data,'-->',end="")
            current = current.next
        print()

ll = linkedlist()
ll.add(12)
ll.add(6)
ll.add(90)
ll.add(71)
ll.add_specigfied(10,3)
ll.display()
"""


                                       #binary search
"""
def binary_search(array,value):
    left = 0
    right = len(array)-1
    while left <= right:
        mid = (left+right)//2
        if array[mid] < value:
            left = mid + 1
        elif array[mid] > value:
            right = mid - 1
        else:
            return mid
    return -1
array = [20,40,60,80]
value = 40
result = binary_search(array,value)
if result != -1:
    print('element position at',str(result))
else:
    print('element is not found')
"""
                                        #linear Search
"""
def linear_search(array,value):
    for i in range(0,len(array)):
        if array[i] == value:
            return i
    return -1

array = [10,20,12,40,50]
value = 20
result = linear_search(array,value)
if result != -1:
    print('element at index is',str(result))
else:
    print('not found')
"""

                                #reverse a linked list in reverse order
# Time Complexity : O(n)
# Space Complexity : O(n) as 'next'

"""
class Node:

	# Constructor to initialize the node object
	def __init__(self, data):
		self.data = data
		self.next = None


class LinkedList:
	def __init__(self):
		self.head = None
		self.last = None

	# Function to reverse the linked list
	def reverse(self):
		prev = None
		current = self.head
		while(current is not None):
			next = current.next
			current.next = prev
			prev = current
			current = next
		self.head = prev

	# Function to insert a new node at the beginning
	def add(self, data):
		new_node = Node(data)
		if self.last is None:
		   new_node.next = self.head
		   self.head = new_node
		else:
			self.last.next = new_node
			new_node.next = self.last
			self.last = new_node
			

	
	def printList(self):
		current= self.head
		while(current):
			print (current.data,'-->',end=" ")
			current = current.next


llist = LinkedList()
llist.add(20)
llist.add(4)
llist.add(15)
llist.add(85)

print ("Given Linked List")
llist.printList()
llist.reverse()
print ("\nReversed Linked List")
llist.printList()
"""
                          #  program to remove duplicate nodes from a sorted linked list


"""
class Node:

	# Constructor to initialize
	# the node object
	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList:

	# Function to initialize head
	def __init__(self):
		self.head = None
		self.last = None

	# Function to insert a new node at the beginning
	def add(self, new_node):
		new_node = Node(new_node)
		if self.last is None:
		   new_node.next = self.head
		   self.head = new_node
		   self.last = new_node
		else:
			self.last.next = new_node 
			self.last = new_node
	
	def printList(self):
		current= self.head
		while(current):
			print(current.data , end = ' ')
			current = current.next
	
	# This function removes duplicates
	# from a sorted list		
	def removeDuplicates(self):
		current = self.head
		if current is None:
			return
		while current.next is not None:
			if current.data == current.next.data:
				new = current.next.next
				current.next = None
				current.next = new
			else:
				current = current.next
		return self.head

llist = LinkedList()

llist.add(30)
llist.add(30)
llist.add(20)
llist.add(20) 
llist.add(13)
llist.add(13)
llist.add(11)
llist.add(11)
llist.add(11)

print ("Created Linked List: ")
llist.printList()
print()
print("Linked List after removing",
			"duplicate elements:")
llist.removeDuplicates()
llist.printList()
"""


                              # convert lowercase to uppercase - review question

"""
string = input('Enter any string: ')
new_string =''
for i in string:
    if(ord(i) >= 97 and ord(i) <= 122):
        new_string = new_string + chr((ord(i) - 32))
    else:
        new_string = new_string + i

# print uppercase string
print('In Upper Case:',new_string)
"""
                     #find given chracter count and display that character count & character
"""
string = 'aabbbccc'
for i in range(0,len(string)):
    if string[i] == string[i+1] and i+1<len(string):
      continue 
    a = string.count(string[i])
    print(str(a)+string[i])
    """


                            #WEEK-5              # buble sort
"""
def Buble_sort(array):
    n = len(array)
    for i in range(n-1):
        for j in range (0,n-i-1):
            if array[j] > array[j+1]:
                array[j],array[j+1] = array[j+1],array[j]
        print(array)

array = [10,34,25,80,95,1]

Buble_sort(array)

print('sorted list is')
for i in range(len(array)):
    print(array[i]," ",end="")
"""
                                           # selection sort
"""
def selection_sort(array):
    n = len(array)
    for i in range(n-1):
        min_posi = i
        for j in range(i,n):
            if array[j] < array[min_posi]:
                min_posi = j
        array[min_posi],array[i] = array[i],array[min_posi]
        print(array)

array = [10,90,50,20,40,25]
selection_sort(array)
print('the sorted array is')
for i in range(len(array)):
    print(array[i]," ",end="")
"""
                                       #insertion sort
"""
def insertion_sort(array):
    for i in range(1,len(array)):
        key = array[i]
        j = i-1
        while j>=0 and key<array[j]:
           array[j+1] = array[j]
           j -= 1
        array[j+1] = key
        print(array)
array = [12,45,33,9,87,4]
insertion_sort(array)

print('sorted array is ')
for i in range(len(array)):
    print(array[i]," ",end="")
"""
#quick sort
"""def Quick_sort(array):
    length = len(array)
    if length <= 1:
        return array
    else:
        pivot = array.pop()
    greater = []
    lower = []
    for item in array:
        if item >pivot:
            greater.append(item)
        else:
            lower.append(item)
    return Quick_sort(lower) +[pivot] + Quick_sort(greater)

array = [5,16,7,8,9,1,2,3,14]
print('unsorted array is',array)
print( 'sorted array is',Quick_sort(array))

"""
                                                 #merge sort
"""
def merge_sort(array):
    if len(array) > 1:
        mid = len(array)//2
        left_array = array[:mid]
        right_array = array[mid:]
        merge_sort(left_array)
        merge_sort(right_array)
        i = 0
        j = 0
        k = 0
        while i < len(left_array) and j < len(right_array):
            if left_array[i] < right_array[j]:
                array[k] = left_array[i]
                k=k+1
                i=i+1
            else:
                array[k] = right_array[j]
                j=j+1
                k=k+1
        while i < len(left_array):
            array[k] = left_array[i]
            i = i+1
            k = k+1
        while j < len(right_array):
                array[k] =right_array[j]
                j = j+1
                k = k+1

array = [20,1,50,40,10,5,17]
print("unsorted array is",array)
merge_sort(array)
print("sorted arraaaay is",array)
"""



                                          #stack push and pop operation
"""

stack = []

# append() function to push
# element in the stack
size = int(input('enter stack size'))
print("push element to stack")
for i in range(0,size):
    item = input()
    stack.append(item)
print('Initial stack')
print(stack)

# pop() function to pop
# element from stack in
# LIFO order
print('\nElements popped from stack:')
print(stack.pop())
print(stack.pop())
print(stack.pop())

print('\nStack after elements are popped:')
print(stack)
"""
                            #stack implimenting in linked list
"""
class Node:
    def __init__(self,data) :
        self.data = data
        self.next = None
class Stack:
    def __init__(self) :
       self.head = None
    def isemphty(self):
        if self.head == None:
            return True
        else:
            return False
    def push(self,data):
        if self.head == None:
            self.head = Node(data)
        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
    def pop(self):
        if self.isemphty():
            return None
        else:
            pop_node = self.head
            self.head = self.head.next
            pop_node.next = None
            return pop_node.data
    def peek(self):
        if self.isemphty():
            return None
        else:
            return self.head.data
    def display(self):
        iter_node = self.head
        if self.isemphty():
            print("stack under flow")
        else:
            while iter_node is not None:
                print(iter_node.data,"--> ",end="")
                iter_node = iter_node.next
            return

my_stack = Stack()
my_stack.push(10)
my_stack.push(50)
my_stack.push(60)
my_stack.push(12)
my_stack.display()
print("\ntop elment in stack",my_stack.peek())
my_stack.pop()
my_stack.pop()
my_stack.display()
print("\ntop elment in stack",my_stack.peek())
"""
                                                     #queue
"""
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Queue:
    def __init__(self):
        self.front = self.rear = None
    def isempty(self):
        return self.front == None
    def inequeue(self,data):
        temp = Node(data)
        if self.rear is None:
            self.front = self.rear = temp
        else:
            self.rear.next = temp
            self.rear = temp
    def dequeue(self):
        if self.isempty():
            return
        temp = self.front
        print(self.front.data)
        self.front = temp.next
        if self.rear is None:
            self.rear = None
    def display(self):
        iter_node = self.front
        if self.isempty():
            print("stack under flow")
        else:
            while iter_node is not None:
                print(iter_node.data,"--> ",end="")
                iter_node = iter_node.next
            return
My_Queue = Queue()
My_Queue.inequeue(10)
My_Queue.inequeue(20)
My_Queue.inequeue(30)
My_Queue.inequeue(40)
My_Queue.display()
print("\ndequeue element is")
My_Queue.dequeue()
My_Queue.dequeue()
My_Queue.display()
print()
print("Queue Front : " + str(My_Queue.front.data if My_Queue.front != None else -1))
print("Queue Rear : " + str(My_Queue.rear.data if My_Queue.rear != None else -1))

"""
                             #Hash Table Collision Handling Using Chaining
"""
class HasTable:
    def __init__(self,size=10):
        self.size = size
        self.data_map = [None]*size
    def Hash(self,key):
        hash = 0
        for char in key:
            hash +=ord(char)
        return hash % self.size
    def print_table(self):
        for i,record in enumerate(self.data_map):
            print(i ,":",record)
    def set_item(self,key,data):
        index = self.Hash(key)
        if self.data_map[index] == None:
            self.data_map[index] = []
        self.data_map[index].append([key,data])
    def get_item(self,key):
        index = self.Hash(key)
        for kv in self.data_map[index]:
            if kv[0] == key:
                print(kv[1])
    def Del_item(self,key):
        index = self.Hash(key)
        for i,kv in enumerate(self.data_map[index]):
            if kv[0] == key:
                del self.data_map[index][i]

My_hashtable = HasTable()
My_hashtable.set_item("20","orange")
My_hashtable.set_item("02","mango")
My_hashtable.set_item("10","apple")
My_hashtable.print_table()
My_hashtable.get_item("02")
My_hashtable.Del_item("02")
My_hashtable.print_table()
"""
                                #stack1 poped element push to stck2 -REVIW QUESTIONS
"""
stack_1 = []
stack_2 = []
stack_1.append(10)
stack_1.append(20)
stack_1.append(40)
temp = stack_1.pop()
if(temp):
    stack_2.append(temp)
print(stack_1)
print(stack_2)
"""
        #remove  mid element of  stack1 and remaing elment add in another stack -EVIEW QUESTIONS
"""
temp = -1
def remove_mid_and_add_to_next(stack1, stack2):
    n = len(stack1)
    mid = (n // 2) +1
    for i in range(mid-1):
        stack2.append(stack1.pop())
    global temp 
    temp = stack1.pop()
    while stack1:
        stack2.append(stack1.pop())

stack_1 = [10,20,5,6,20,8,1]
stack_2 = []
print(stack_1)
remove_mid_and_add_to_next(stack_1,stack_2)
stack_1.append(temp)
print(stack_1)
print(stack_2)
"""
                                            #reverse a string-REVIW QUESTION
"""
def reverse_string(string):
    stack = []
    for char in string:
        stack.append(char)
    reversed_string = ""
    while stack:
        reversed_string += stack.pop()
    return reversed_string
str = "hello"
print(reverse_string(str))
"""
                                              #week - 6     Tree creation 
"""
class TreeNode:
    def __init__(self, data, children = []):
        self.data = data
        self.children = children
    
    def __str__(self, level=0):
        ret = "  " * level + str(self.data)  + "\n"
        for child in self.children:
            ret += child.__str__(level + 1)
        return ret
    def addChild(self, TreeNode):
        self.children.append(TreeNode)

tree = TreeNode('Drinks', [])
cold = TreeNode('Cold', [])
hot = TreeNode('Hot', [])
cool = TreeNode('cool',[])
tree.addChild(cold)
tree.addChild(hot)
tree.addChild(cool)
tea = TreeNode('Tea', [])
coffee = TreeNode('Coffee', [])
cola = TreeNode('Cola', [])
cola1 = TreeNode("cola1",[])
fanta = TreeNode('Fanta', [])
cold.addChild(cola)
cold.addChild(fanta)
hot.addChild(tea)
hot.addChild(coffee)
cola.addChild(cola1)
print(tree)
"""
#binary tree
"""
class BinaryTree:
    def __init__(self, size):
        self.customList = size * [None]
        self.lastUsedIndex = 0
        self.maxSize = size
    
    def insertNode(self, value):
        if self.lastUsedIndex + 1 == self.maxSize:
            return "The Binary Tree is full"
        self.customList[self.lastUsedIndex] = value
        self.lastUsedIndex += 1
        return "The value has been successfully inserted"

    def searchNode(self, nodeValue):
        for i in range(len(self.customList)):
            if self.customList[i] == nodeValue:
                return "Success"
        return "Not found"
    
    def preOrderTraversal(self, index):
        if index > self.lastUsedIndex:
            return
        print(self.customList[index])
        self.preOrderTraversal(index*2)
        self.preOrderTraversal(index*2 + 1)

    def inOrderTraversal(self, index):
        if index > self.lastUsedIndex:
            return
        self.inOrderTraversal(index*2)
        print(self.customList[index])
        self.inOrderTraversal(index*2+1)
    
    def postOrderTraversal(self, index):
        if index > self.lastUsedIndex:
            return
        self.postOrderTraversal(index*2)
        self.postOrderTraversal(index*2+1)
        print(self.customList[index])
    
    def levelOrderTraversal(self, index):
        if self.customList is None:
            print('cant display')
            return
        if index!=0:
           index = index*(index-1)+1
        for i in range(index, self.lastUsedIndex):
            print(self.customList[i])
    
    def deleteNode(self, value):
        if self.lastUsedIndex == 0:
            return "There is not any node to delete"
        for i in range(1, self.lastUsedIndex+1):
            if self.customList[i] == value:
                self.customList[i] = self.customList[self.lastUsedIndex]
                self.customList[self.lastUsedIndex] = None
                self.lastUsedIndex -= 1
                return "The node has been successfully deleted"
    
    def deleteBT(self):
       self.customList = None
       return "The BT has been successfully deleted"

    
newBT = BinaryTree(10)
list = [10,50,2,6,11,21,90,30]
for i in list:
    newBT.insertNode(i)
# newBT.insertNode("Drinks")
# newBT.insertNode("Hot")
# newBT.insertNode("Cold")
# newBT.insertNode("Tea")
# newBT.insertNode("Coffee")
newBT.levelOrderTraversal(3)
print(newBT.deleteBT())
newBT.levelOrderTraversal(1)
"""

#binary search tree(preorder,inorder,post order)
"""
class Node:
    def __init__(self,val):
      self.node_data = val
      self.right = None
      self.left = None
      self.min_val = float('-inf')
      self.max_val = float('inf')
    def insert_node(self,data):
      if self.node_data is None:
         self.node_data = data
         return
      if self.node_data == data:
         return
      if self.node_data > data:
         if self.left:
            self.left.insert_node(data)
         else:
               self.left = Node(data)
      else: 
         if self.right:
            self.right.insert_node(data)
         else:
            self.right = Node(data)
    def minValue(node):
       current = node
       while current and current.left is not None:
          current = current.left
       return current
    def delete_node(self,root,node):
       if root is None:
          return root
       if node < root.node_data:
          root.left = self.delete_node(root.left,node)
       elif node > root.node_data:
          root.right = self.delete_node(root.right,node)
       else:
          if root.left is None:
             temp = root.right
             root = None
             return temp
          elif root.right is None:
             temp = root.left
             root = None
             return temp

          temp = self.minValue(root.right)
          root.right = self.delete_node(root.right,temp.node)
       return root
    def dfs_preOrder(self):
       print(self.node_data," ",end="")
       if self.left:
          self.left.dfs_preOrder()
       if self.right:
          self.right.dfs_preOrder()
    def dfs_postorder(self):
       if self.left:
          self.left.dfs_postorder()
       if self.right:
          self.right.dfs_postorder()
       print(self.node_data," ",end="")
    def dfs_inorder(self):
       if self.left:
          self.left.dfs_inorder()
       print(self.node_data," ",end="")
       if self.right:
          self.right.dfs_inorder()

    def BFS(self):
      queue = []
      results = []
      queue.append(self)
      while len(queue) > 0:
        current_node = queue.pop(0)
        results.append(current_node.node_data)
        if current_node.left is not None:
            queue.append(current_node.left)
        if current_node.right is not None:
            queue.append(current_node.right)
      print(results)
    def search(self,data):#search an element present or not
        if self.node_data == data:
           print("node found")
           return
        if data<self.node_data:
           if self.left:
              self.left.search(data)
           else:
              print("node not found")
        else:
           if self.right:
              self.right.search(data)
           else:
              print("node note found")
    def is_bst(self):
        if self.node_data < self.min_val or self.node_data > self.max_val:
            return False
        if self.left is not None and not self.left.is_bst():
            return False
        if self.right is not None and not self.right.is_bst():
            return False
        return True

#find closest value inBTS
def closest_value(root, target):
    closest = root.node_data
    while root:
        if abs(root.node_data - target) < abs(closest - target):
            closest = root.node_data
        if target < root.node_data:
            root = root.left
        elif target > root.node_data:
            root = root.right
        else:
            break
    return closest

root = Node(12)
root.insert_node(10)
root.insert_node(40)
root.insert_node(20)
root.insert_node(15)
root.insert_node(2)
root.delete_node(root,20)
print('preorder')
root.dfs_preOrder()
print('dfs')
root.BFS()
print('inorder')
root.dfs_inorder()
print('postorder')
root.dfs_postorder()
print()
root.search(0)
print("closest value is",closest_value(root,14.5))
# Check if the binary tree is a valid BST
if root.is_bst():
    print("The binary tree is a valid BST")
else:
    print("The binary tree")
"""


# # max heap
# class Heap:
#     def __init__(self,array):
#         self.array = array

#     def shiftdown(self, i = 0):
#         max = i
#         left = 2*i + 1
#         right = 2*i + 2
#         if i >= len(self.array) - 1:
#             return
#         if self.array[right] > self.array[max]:
#             max = right
#         if self.array[left] >self.array[max]:
#             max = left
#         if i != max:
#             self.array[max], self.array[i] = self.array[i], self.array[max]
#             self.shiftdown(max)
#     def shiftup(self, i):
#         parent = int((i - 1) / 2)
#         if self.array[i] > self.array[parent]:
#             self.array[i], self.array[parent] = self.array[parent], self.array[i]
#             self.shiftup(parent)
#         return

#     def insert(self,value):
#         self.array.append(value)
#         self.shiftup(len(self.array) - 1)

#     def delete(self):
#         self.array[0] = self.array.pop(len(self.array) - 1)
#         self.shiftdown()


# array = [10,5,3,2,4]
# heep1 = Heap(array)
# print(heep1.array)
# heep1.insert(15)
# print(heep1.array)

#min heap:
# class Heap:
#     def __init__(self, array):
#         self.array = array

#     def shiftdown(self, i = 0):
#         n = len(self.array)
#         min = i
#         left = 2*i + 1
#         right = 2*i + 2
#         if i >= len(self.array) - 1:
#             return
#         if left < n and self.array[left] < self.array[min]:
#             min = left
#         if right < n and self.array[right] < self.array[min]:
#             min = right
#         if min != i:
#             self.array[i], self.array[min] = self.array[min], self.array[i]
#             self.shiftdown(min)

#     def shiftup(self, i):
#         parent = int((i - 1) / 2)
#         if i <= 0:
#             return
#         if self.array[i] < self.array[parent]:
#             self.array[i], self.array[parent] = self.array[parent], self.array[i]
#             self.shiftup(parent)
#         return

#     def insert(self,value):
#         self.array.append(value)
#         self.shiftup(len(self.array) - 1)

#     def delete(self):
#         self.array[0] = self.array.pop(len(self.array) - 1)
#         self.shiftdown()


# array = [2,4,7,9,10]
# hp = Heap(array)
# print(hp.array)
# hp.insert(1)
# print(hp.array)

#Heap sorting

# class Heap:
#     def __init__(self, array):
#         self.array = array

#     def shiftdown(self, n, i):
#         max = i
#         left = 2 * i + 1
#         right = 2 * i + 2
#         if i >= n:
#             return
#         if left < n and self.array[left] > self.array[max]:
#             max = left
#         if right < n and self.array[right] > self.array[max]:
#             max = right
#         if max != i:
#             self.array[max], self.array[i] = self.array[i], self.array[max]
#             self.shiftdown(n, max)
#         return

#     def sort(self):
#         n = len(self.array)
#         for i in range(n//2)-1,-1,-1):
#             self.shiftdown(n,i)
#         for i in range(n - 1, -1, -1):
#             self.array[i], self.array[0] = self.array[0], self.array[i]
#             self.shiftdown(i,0)
#         return self.array

# arr = [20,10,80,2,4,1]
# hp = Heap(arr)
# print(hp.array)
# print(hp.sort())

#trie program
"""
class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        current.end_of_word = True

    def search(self, word):
        current = self.root
        for char in word:
            if char not in current.children:
                return False
            current = current.children[char]
        return current.end_of_word

    def starts_with(self, prefix):
        current = self.root
        for char in prefix:
            if char not in current.children:
                return False
            current = current.children[char]
        return True

    def display(self):
        words = []
        def dfs(node, prefix):
            if node.end_of_word:
                words.append(prefix)
            for char in node.children:
                dfs(node.children[char], prefix + char)
        dfs(self.root, "")
        print(words)

 
trie = Trie()
trie.insert("hello")
trie.insert("world")
trie.insert("python")
trie.display() # prints ['hello', 'world', 'python']
print(trie.search("world"))
print(trie.starts_with("thon"))
"""
#graph BFS DFS
"""
class Graph:
    def __init__(self):
        self.adj_list = {}

    def print_graph(self):
        for vertex in self.adj_list:
            print(vertex, ':', self.adj_list[vertex])

    def add_vertex(self, vertex):
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = []
            return True
        return False



    def add_edge(self, v1, v2):
          if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
              self.adj_list[v1].append(v2)
              self.adj_list[v2].append(v1)
              return True
          return False

    def remove_edge(self, v1, v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            self.adj_list[v1].remove(v2)
            self.adj_list[v2].remove(v1)
            return True
        return False

    def remove_vertex(self, vertex):
        if vertex in self.adj_list.keys():
            for other_vertex in self.adj_list[vertex]:
                self.adj_list[other_vertex].remove(vertex)
            del self.adj_list[vertex]
            return True
        return False
    def BFS(self,s):
        visited=[False]*(len(self.adj_list)+1)
        queue=[]
        queue.append(s)
        visited[s]=True
        while queue:
            s=queue.pop(0)
            print(s,end=" ")
            for i in self.adj_list[s]:
                if visited[i]==False:
                    queue.append(i)
                    visited[i]=True
    def DFSUtil(self,v,visited):
        visited.add(v)
        print(v,end=" ")
        for neighbour in self.adj_list[v]:
            if neighbour not in visited:
                self.DFSUtil(neighbour,visited)

    def DFS(self):
        visited=set()
        for vertex in self.adj_list:
            if vertex not in visited:
                self.DFSUtil(vertex,visited)

my_graph = Graph()
my_graph.add_vertex(1)
my_graph.add_vertex(2)
my_graph.add_vertex(3)
my_graph.add_vertex(4)

my_graph.add_edge(1,2)
my_graph.add_edge(1,3)
my_graph.add_edge(1,4)
my_graph.add_edge(2,4)
my_graph.add_edge(3,4)
my_graph.print_graph()
print("DFS order")
my_graph.DFS()
print('\nBFS order')
my_graph.BFS(2)
print()
my_graph.remove_vertex(4)
print("after deletion")
my_graph.print_graph()

print()
my_graph.print_graph()
my_graph.DFS()
"""
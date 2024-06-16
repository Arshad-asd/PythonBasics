#<--------------------------------------------------------Stack-Implementation-Using-List--------------------------------------------------------------------------->
class Stack:
    def __init__(self) -> None:
        self.itemes = []
    def push(self,iteme):
        self.itemes.append(iteme)
    def pop(self):
        if not self.is_empty():
            self.itemes.pop()
    def is_empty(self):
        return len(self.itemes) == 0
    def peek(self):
        if not self.is_empty():
            return self.itemes[-1]
    def size(self):
        return len(self.itemes)
#<--------------------------------------------------------Queue-Implementation-Using-List--------------------------------------------------------------------------->
class Queue:
    def __init__(self) -> None:
        self.items = []
    def enqueue(self,iteme):
        self.items.insert(0,iteme)
    def dequeue(self):
        if not self.is_empty():
            self.items.pop()
    def is_empty(self):
        return len(self.items) == 0
    def size(self):
        return len(self.items)
    def front(self):
        self.items[-1]
    def rear(self):
        self.items[0]
#<--------------------------------------------------------Stack-Implementation-Using-LinkedList--------------------------------------------------------------------------->
class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.next = None
class Stack:
    def __init__(self) -> None:
        self.head = None
    def push(self,data):
        new_node = Node(data)
        if self.head is  None:
           self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
    def pop(self):
        if self.head is None:
            return None
        else:
            popped = self.head.data
            self.head = self.head.next
        return popped
    def peek(self):
        if self.head is None:
            return None
        else:
            return self.head.data
    def display(self):
        current = self.head
        while current:
            print(current.data,'-->',end="")
            current = current.next
        print()

#<--------------------------------------------------------Queue-Implementation-Using-LinkedList--------------------------------------------------------------------------->
class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.next = None
class Stack:
    def __init__(self) -> None:
        self.front = None
        self.rear = None
    def enqueue(self,data):
        new_node = Node(data)
        if self.rear is None:
            self.rear = new_node
            self.front = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
    def dequeue(self):
        if self.front is None:
            return None
        else:
            removed = self.front.data
            if self.rear == self.front:
                self.rear = None
                self.front = None
            else:
                self.front = self.front.next
        return removed
    def peek(self):
        if self.front is None:
            return None
        else:
            return self.front.data
    def display(self):
        current = self.front
        while current:
            print(current.data,'-->',end="")
        print()
#<--------------------------------------------------------Satack-Implementation-Using-Queue--------------------------------------------------------------------------->

class MyStack:
    def __init__(self):
        self.queue1 = []
        self.queue2 = []

    def push(self, x: int) -> None:
        self.queue1.append(x)

    def pop(self) -> int:
        if not self.queue1:
            return None
        while len(self.queue1) > 1:
            self.queue2.append(self.queue1.pop(0))
        popped_element = self.queue1.pop(0)
        self.queue1, self.queue2 = self.queue2, self.queue1
        return popped_element

    def top(self) -> int:
        if not self.queue1:
            return None
        while len(self.queue1) > 1:
            self.queue2.append(self.queue1.pop(0))
        top_element = self.queue1[0]
        self.queue2.append(self.queue1.pop(0))
        self.queue1, self.queue2 = self.queue2, self.queue1
        return top_element

    def empty(self) -> bool:
        return not self.queue1
#<--------------------------------------------------------Queue-Implementation-Using-Satack--------------------------------------------------------------------------->
class MyQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        self.stack1.append(x)

    def pop(self) -> int:
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop() if self.stack2 else None

    def peek(self) -> int:
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2[-1] if self.stack2 else None

    def empty(self) -> bool:
        return not self.stack1 and not self.stack2

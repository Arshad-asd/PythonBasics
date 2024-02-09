#<-----------------------------------------------Hash Table create------------------------------------------------------------->
class HastTable:
    def __init__(self,size) -> None:
        self.size = size
        self.table = [None]*size
    def hashing(self,key):
        hash = 0
        for char in key:
            hash += ord(char)
        return hash % self.size
    def set_item(self,key,value):
        index = self.hashing(key)
        if self.table[index] is None:
            self.table[index] = []
        self.table[index].append([key,value])
    def get_item(self,key):
        index = self.hashing(key)
        for kv in self.table[index]:
            if kv[0] == key:
                print('value is',kv[1])
    def delete_item(self,key):
        index = self.hashing(key)
        for i,kv in enumerate(self.table[index]):
            if kv[0] == key:
                del self.table[index][i]
        return self.display()
    def display(self):
        for i ,kv in enumerate(self.table):
            print(i,":",kv)
    def is_prime(self,num):
        if num < 2:
            return False
        for i in range(2,int(num**0.5)+1):
            if num % i == 0:
                return False
        return True
    def display_prime(self):
        prime_sum = 0
        for i,kv in enumerate(self.table):
            print(i,":",kv)
            if kv:
                for item in kv:
                    if self.is_prime(item[1]):
                        prime_sum += item[1]
        print(f"sum of prime numbers {prime_sum}")

hash_table = HastTable(10)
hash_table.set_item("A", 2)
hash_table.set_item("B", 10)
hash_table.set_item("C", 8)
hash_table.set_item("D", 11)
hash_table.set_item("A", 30)
hash_table.get_item("A")
hash_table.display_prime()
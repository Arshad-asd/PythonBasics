#<-----------------------------------------------Hash Table create handles collisions CHAINING------------------------------------------------------------->
# class HastTable:
#     def __init__(self,size) -> None:
#         self.size = size
#         self.table = [None]*size
#     def hashing(self,key):
#         hash = 0
#         for char in key:
#             hash += ord(char)
#         return hash % self.size
#     def set_item(self,key,value):
#         index = self.hashing(key)
#         if self.table[index] is None:
#             self.table[index] = []
#         self.table[index].append([key,value])
#     def get_item(self,key):
#         index = self.hashing(key)
#         for kv in self.table[index]:
#             if kv[0] == key:
#                 print('value is',kv[1])
#     def delete_item(self,key):
#         index = self.hashing(key)
#         for i,kv in enumerate(self.table[index]):
#             if kv[0] == key:
#                 del self.table[index][i]
#         return self.display()
#     def display(self):
#         for i ,kv in enumerate(self.table):
#             print(i,":",kv)
#     def is_prime(self,num):
#         if num < 2:
#             return False
#         for i in range(2,int(num**0.5)+1):
#             if num % i == 0:
#                 return False
#         return True
#     def display_prime(self):
#         prime_sum = 0
#         for i,kv in enumerate(self.table):
#             print(i,":",kv)
#             if kv:
#                 for item in kv:
#                     if self.is_prime(item[1]):
#                         prime_sum += item[1]
#         print(f"sum of prime numbers {prime_sum}")

# hash_table = HastTable(10)
# hash_table.set_item("A", 2)
# hash_table.set_item("B", 10)
# hash_table.set_item("C", 8)
# hash_table.set_item("D", 11)
# hash_table.set_item("A", 30)
# hash_table.get_item("A")
# hash_table.display_prime()

#<-----------------------------------------------Hash Table CREATION  handles collisions useing OpenAddressing------------------------------------------------------------->
class HastTable:
    def __init__(self, size) -> None:
        self.size = size
        self.table = [None] * size

    def hashing(self, key):
        hash_val = 0
        for char in key:
            hash_val += ord(char)
        return hash_val % self.size

    def linear_probing_set(self, key, value):
        index = self.hashing(key)
        while self.table[index] is not None:
            if self.table[index][0] == key:
                self.table[index][1] = value
                return
            index = (index + 1) % self.size
        self.table[index] = [key, value]

    def quadratic_probing_set(self, key, value):
        index = self.hashing(key)
        i = 0
        while self.table[index] is not None:
            if self.table[index][0] == key:
                self.table[index][1] = value
                return
            i += 1
            index = (index + i**2) % self.size
        self.table[index] = [key, value]

    def linear_probing_get(self, key):
        index = self.hashing(key)
        while self.table[index] is not None:
            if self.table[index][0] == key:
                print('value is', self.table[index][1])
                return
            index = (index + 1) % self.size
        print('Not found key')

    def quadratic_probing_get(self, key):
        index = self.hashing(key)
        i = 0
        while self.table[index] is not None:
            if self.table[index][0] == key:
                print('value is', self.table[index][1])
                return
            i += 1
            index = (index + i**2) % self.size
        print("not found")

    def traversal(self):
        for i, kv in enumerate(self.table):
            print(i, ' : ', kv)


HT = HastTable(10)
HT.double_hashing_set('A', 10)
HT.double_hashing_set('B', 20)
HT.double_hashing_set('AB', 200)
HT.double_hashing_set('BA', 300)
HT.traversal()
HT.double_hashing_get('BA')

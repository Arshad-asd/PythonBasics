
# Remove duplicate in list with out useing extar list,set,dict

def duplicate_remove(lists):
    index = 0
    while index < len(lists):
        current_element = lists[index]
        if current_element in lists[index + 1:]:
            lists.remove(current_element)
        else:
            index += 1
    return lists
my_list = [1, 2, 2, 3, 4, 4, 5,9,2,4,8,5,10,6,5,99,66,7,8,]
print(duplicate_remove(my_list))

#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        first = head
        while first:
            current = head
            while current and current.next :
                if current.val >= current.next.val:
                    temp = current.next.val
                    current.next.val = current.val
                    current.val = temp
                    current = current.next
                else:
                    current = current.next
            first = first.next
        return head

# Find missing elements in an array
arr = [1, 8, 9, 5, 6, 7, 10]
arr.sort()
n = arr[-1]

#Method 1
print(arr)
result = []
for i in range(len(arr)):
    temp = arr[-1]-arr[i]
    if temp not in arr and temp !=0:
            result.append(temp)
         
print(result)

#Method 2
for i in range(len(arr)-1):
    curr = arr[i]
    next = arr[i+1]
    if next-curr >1:
        for missing in range(curr+1,next):
            result.append(missing)
print(result)


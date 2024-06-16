#Zip function 
names = ['Alice', 'Bob', 'Charlie']
ages = [30, 25, 35]

for name,age in zip(names,ages):
    print(f'name:{name},age:{age}')

#enumerate function
list1 = ['a','b','c']
for index, value in enumerate(list1):
    print(f"Index: {index}, Value: {value}")

#map function
numbers = [1, 2, 3, 4, 5]
squared = map(lambda x: x**2, numbers)
print("squared numbers",list(squared))

#fileter function
even_numbers = filter(lambda x: x%2 ==0, numbers)
print("even numbers",list(even_numbers))

#any function
list2 = [False,True,False]
result = any(list2)
print("result:",result)

#all function
list3 = [True,True,True]
result = all(list3)
print("result of all :",result)


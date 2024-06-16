people = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 30},
    {"name": "Charlie", "age": 22},
    {"name": "David", "age": 35},
    {"name": "Eva", "age": 28}
]


b = sorted(people,key = lambda x : x["age"])
print(b)

people = [
    {'name':'don','salary':100000,'languages':'python'},
    {'name':'xavi','salary':40000,'languages':'React'},
    {'name':'alex','salary':50000,'languages':'Javascrips'},
    {'name':'riya','salary':60000,'languages':'React'},
    {'name':'mark','salary':700000,'languages':'python'}
]
arr = []
for i in range(len(people)):
    print(f'{people[i]["name"]}:{people[i]["salary"]}')
    temp = people[i]['languages']
    arr.append(temp)
print('languages :',list(set(arr)))


objects = [{'name':'johon','age':21},{'name':'jain','age':25},{'name':'mark','age':22}]
for i in range(len(objects)):
    for j in range(len(objects)-i-1):
        if objects[j]["age"] > objects[j+1]['age']:
            objects[j],objects[j+1]=objects[j+1],objects[j]

print(objects)

def remove_key_vowels(d:dict)->dict:
    vowles = {'a','e','i','o','u'}
    for key in list(d.keys()):
        if key[0] in vowles:
            del d[key]
    return d

d = {'apple': 1, 'banana': 2, 'orange': 3, 'kiwi': 4, 'peach': 5}
print(remove_key_vowels(d))

#Interchange keys and values in a dict
d = {'a':1,'b':2,'c':3}
def swap_key_value(d:dict)->dict:
    for key in list(d.keys()):
        val = d.pop(key)
        d[val] = key
    return d
print(swap_key_value(d))

# Running list comprehension to filter out dicts without a certain key from a list of dicts
list_of_dicts = [
    {'name': 'John', 'age': 30},
    {'name': 'Alice', 'age': 25, 'city': 'New York'},
    {'name': 'Bob', 'age': 35, 'city': 'Los Angeles'},
    {'name': 'Emma', 'age': 40}
]
key_to_filter = 'city'
filterd_list = [key for key in list_of_dicts if key_to_filter in key]
print(filterd_list)

# Merge json objects
obj1 = [
    {"id": 1, "name": "arshad"},
    {"id": 2, "name": "anas"},
    {"id": 3, "name": "noufal"},
]
obj2 = [
    {"salary": 50000, "designation": "IT"},
    {"salary": 40000, "designation": "IT"},
]

merged_list = []

for i in range(min(len(obj1), len(obj2))):
    # Combine dictionaries from both lists
    combined_dict = {**obj1[i], **obj2[i]}
    merged_list.append(combined_dict)
# If obj1 is longer, append the remaining items
if len(obj1) > len(obj2):
    merged_list.extend(obj1[len(obj2):])
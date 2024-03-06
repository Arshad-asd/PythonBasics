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
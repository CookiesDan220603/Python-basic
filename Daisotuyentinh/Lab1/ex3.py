dic = {1: 15, 2: 7, 3: 10, 4: 15, 5: 9, 6: 15, 7: 14, 8: 7, 10: 15}

print("-----")
print(dic)
print("-----")
n = int(input("Enter n value: ")) 
## Ex3.a
count = 0
for i in dic:
    if (n == dic[i]):
        count += 1
print("Value '%d' appears %d times."%(n, count))

##Ex3.b
x = int(input("Enter the value of element you want to update: "))
k = int(input("Enter the value you update: "))
for i in dic:
    if (x == dic[i]):
        dic.update({i: k})

print("Dictionary after update: ")
print(dic)

##Ex3.c
value_delete = int(input("Enter the value you want to delete: "))
for i in list(dic.keys()):
    if (value_delete == dic[i]):
        dic.pop(i)
print("Dictionary after delete: ")
print(dic)

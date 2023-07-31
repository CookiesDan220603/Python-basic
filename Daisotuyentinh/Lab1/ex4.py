set1 = {1, 2, 3, 4, 5, 6, 7}
set2 = {4, 5, 6, 7, 8, 9, 10}

## Ex4a
print("Exercise 4a:")
ans = set1.intersection(set2)
print(ans)
print("-----")

## Ex4b
print("Exercise 4b:")
ans = set1.union(set2)
print(ans)
print("-----")


## Ex4c 
print("Exercise 4c:")
x = int(input("Enter value x you want to add into Set 2: "))
print("Set 2 before add value '%d':"%(x))
print(set2)
set2.add(x)
print("Set 2 after add value '%d':"%(x))
print(set2)
print("-----")


## Ex4d
print("Exercise 4d:")
y = int(input("Enter value you want to delete in Set 1: "))
print("Set 1 before delete value '%d':"%(y))
print(set1)
set1.remove(y)
print("Set 1 after delete value '%d':"%(y))
print(set1)
print("--- End ---")
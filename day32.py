'''add'''
fruits = {"apple", "banana"}
fruits.add("mango")

print(fruits)

'''clear'''
fruits = {"apple", "banana", "mango"}
fruits.clear()

print(fruits)

'''discard'''
fruits = {"apple", "banana", "mango"}
fruits.discard("banana")

print(fruits)

'''intersection'''
A = {1, 2, 3}
B = {2, 3, 4}

print(A.intersection(B))

'''pop'''
fruits = {"apple", "banana", "mango"}
fruits.pop()

print(fruits)

'''remove'''
fruits = {"apple", "banana", "mango"}
fruits.remove("banana")

print(fruits)

'''union'''
A = {1, 2, 3}
B = {3, 4, 5}

print(A.union(B))

'''update'''
A = {1, 2, 3}
B = {4, 5}

A.update(B)

print(A)
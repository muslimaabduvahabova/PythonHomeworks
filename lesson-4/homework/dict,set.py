### Dictionary Exercises
#### 1. Sort a Dictionary by Value
my_dict = {'a': 1, 'c': 3, 'b': 2, 'd': 4}
dict(sorted(my_dict.items(), key=lambda item: item[1]))
dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))
print(dict(sorted(my_dict.items(), key=lambda item: item[1])))
print(dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True)))
#### 2. Add a Key to a Dictionary
added_dict = {0: 10, 1: 20}
added_dict[2] = 30
print(added_dict)
##### another option
added_dict2 = {0: 10, 1: 20}
added_dict2.update({2: 30})
print(added_dict2)
#### 3. Concatenate Multiple Dictionaries
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
result = {}
result.update(dic1)
result.update(dic2)
result.update(dic3)
print(result)
##### another option
result2 = {**dic1, **dic2, **dic3}
print(result2)
#### 4. Generate a Dictionary with Squares
n = 5
dict1 = {}
for i in range(1, n + 1):
    dict1[i] = i * i
print(dict1)
##### another option
n = 5
dict2 = {i: i * i for i in range(1, n + 1)}
print(dict2)
#### 5. Dictionary of Squares (1 to 15)
m = 15
d1 = {}
for i in range(1, m + 1):
    d1[i] = i * i 
print(d1)
##### another option
d2 = {}
for i in range(1, 16):
    d2[i] = i * i
    print(d2)
##### another option
d3 = {i: i* i for i in range(1, 16)}
print(d3)
### Set Exercises
#### 1. Create a Set
my_set = {10, 20, 30, 40, 50}
type(my_set)
print(my_set)
#### 2. Iterate Over a Set
for item in my_set:
    print(item)
#### 3. Add Member(s) to a Set
set1 = {1,2,3,4}
set1.add(5)
print(set1)
##### another option
set2 = {1,2,3}
set2.update([4,5,6])
print(set2)
#### 4. Remove Item(s) from a Set
my_set.remove(20)
print(my_set)
##### another option
my_set.discard(60)
print(my_set)
##### another option
my_set.clear()
print(my_set)
#### 5. Remove an Item if Present in the Set
set3 = {'a', 'b','c','d','e'}
set3.discard('c')
print(set3)
set3.discard('f')
print(set3)

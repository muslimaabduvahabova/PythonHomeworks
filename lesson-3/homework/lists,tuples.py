#### 1. Create and Access List Elements
fruit = ['apple', 'banana', 'mango', 'cherry', 'strawberry']
print(fruit[2])
#### 2. Concatenate Two Lists
list1 = [1,2,3,4]
list2 = [5,6,7,8]
single_list = list1 + list2

print(single_list)
#### 3. Extract Elements from a List
numbers = ['a','b', 'c', 'd', 'e', 'f']
numbers [0]
middle_index = len(numbers) // 2
numbers[middle_index]
numbers [-1]
result = [numbers [0], numbers[middle_index], numbers [-1]]
print(result)
#### 4. Convert List to Tuple
movies = ['Harry Potter', 'Twilight', 'Bad Boys', 'Rush Hour', 'King Richard']
movies_touple = tuple(movies)
print(movies_touple)
#### 5. Check Element in a List
cities = ['London', 'Vashington', 'Paris', 'Ottava', 'Bern', 'Dubai']
print('Paris' in cities)
#### 6. Duplicate a List Without Using Loops
number = [1,2,3,4,5,6]
doubled = number * 2 
print(doubled)
##### another option
copied = number + number.copy()
print(copied)
#### 7. Swap First and Last Elements of a List
my_list = ['a','b', 'c', 1, 2, 3, 'd', 'f', 'g']
my_list.reverse()
print(my_list)
##### another option
your_list = ['a','b', 'c', 1, 2, 3, 'd', 'f', 'g']
your_list[0], your_list[-1] = your_list[-1], your_list[0]
print(your_list)
#### 8. Slice a Tuple
my_tuple = (1,2,3,4,5,6,7,8,9,10)
slice_part = my_tuple[3:8]
print(slice_part)
#### 9. Count Occurrences in a List
colors = ['pink', 'white', 'black', 'pink', 'red', 'blue']
colors.count('pink')
#### 10. Find the Index of an Element in a Tuple
animals = ('dog', 'cat', 'tiger', 'lion', 'bear', 'horse')
animals.index('lion')
#### 11. Merge Two Tuples
num1 = (10,20,30)
num2 = (40,50,60)
merged = num1 + num2
print(merged)
#### 12. Find the Length of a List and Tuple
m_list = [1,2,3,4,5]
m_tuple = ('a','b','c','d')
list_length = len(m_list)
tuple_length = len(m_tuple)
print(list_length)
print(tuple_length)
#### 13. Convert Tuple to List
num_tuple = (60,70,80,90,100)
list_version = list(num_tuple)
print(list_version)
#### 14. Find Maximum and Minimum in a Tuple
num_tuple = (7, 9, 10, 15, 23, 18, 62)
maximum = max(num_tuple)
minimum = min(num_tuple)
print('Max', maximum)
print('Min', minimum)
#### 15. Reverse a Tuple
words = ("apple", "banana", "cherry", "date")
reversed_tuple = words[::-1]
print(reversed_tuple)

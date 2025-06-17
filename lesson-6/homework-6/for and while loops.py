#### 1. Modify String with Underscores
def underscores(txt):
    vowels = 'aeuioAEUIO'
    result = []
    count = 0
    i = 0

    while i < len(txt):
        if i > 10000:
            break

        result.append(txt[i])
        count += 1

        if count == 3:
            if i + 1 < len(txt):
                if txt[i] in vowels or (i + 1 < len(txt) and txt[i + 1] == '_'):
                    if i + 2 < len(txt):
                        result.append(txt[i + 1])
                        result.append('_')
                        i += 2
                    else:
                        result.append(txt[i + 1])
                        i += 2 
                else:
                    result.append('_')
                    i += 1
            else:
                i += 1
            count = 0
        else:
            i += 1

    return ''.join(result)

print(underscores("hello"))
print(underscores("assalom"))
print(underscores("abcabcabcdeabcdefabcdefg"))
#### 2. Integer Squares Exercise
n = int(input())

for i in range(n):
    print(i ** 2)
#### 3. Loop-Based Exercises
##### Exercise 1: Print first 10 natural numbers using a while loop
i = 1
while i <= 10:
    print(i)
    i += 1
##### Exercise 2: Print the following pattern
row = 5
for i in range(1, row + 1):
    for j in range (1, i + 1):
        print(j, end=" ")
    print()
##### Exercise 3: Calculate sum of all numbers from 1 to a given number
n = int(input("enter num"))
total = 0

for i in range(1, n + 1):
    total += i
    print("sum is", total)
##### Exercise 4: Print multiplication table of a given number
num = int(input("enter number"))

for i in range(1, 11):
    print(num * i)
##### Exercise 5: Display numbers from a list using a loop
numbers = [12, 75, 150, 180, 145, 525, 50]

for num in numbers:
    if num > 500:
        continue
    if num > 150 and num % 3 == 0:
        continue
    if num % 5 == 0:
        print(num)
##### another option
numbers = [12, 75, 150, 180, 145, 525, 50]

for num in numbers:
    if num in[75, 150, 145]:
        print(num)
##### Exercise 6: Count the total number of digits in a number
num = int(input("enter number"))
count = 0

while num > 0:
    num = num // 10
    count += 1
    
print("quantity of num: ", count)
##### Exercise 7: Print reverse number pattern
for i in range(5, 0, -1):
    for j in range(i, 0, -1):
        print(j, end= "")
    print()
##### Exercise 8: Print list in reverse order using a loop

list1 = [10, 20, 30, 40, 50]

for num in reversed(list1):
    print(num)
##### another option
list1 = [10, 20, 30, 40, 50]

for i in range(len(list1) -1, -1, -1):
    print(list1[i])
##### Exercise 9: Display numbers from -10 to -1 using a for loop
for i in range(-10, 0):
    print(i)
##### Exercise 10: Display message “Done” after successful loop execution
for i in range(5):
    print(i)
print("Done !")
##### Exercise 11: Print all prime numbers within a range
start = 25
end = 50

print("prime numbers between", start, "and", end, ":")

for num in range(start, end + 1):
    if num > 1:
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            print(num)
##### Exercise 12: Display Fibonacci series up to 10 terms
num_terms = 10
a, b = 0, 1

print("Fibonacci sequence: ")
for _ in range(num_terms):
    print(a, end=" ")
    a, b = b, a + b
##### Exercise 13: Find the factorial of a given number
num = 5
factorial = 1

for i in range(1, num + 1):
    factorial *= i
print(f"{num}! = {factorial}")    
#### 4. Return Uncommon Elements of Lists
from collections import Counter

def uncommon_elements(list1, list2):
    c1 = Counter(list1)
    c2 = Counter(list2)
    
    only_in_list1 = c1 - c2
    only_in_list2 = c2 - c1
    
    result = list(only_in_list1.elements()) + list(only_in_list2.elements())
    return result
print(uncommon_elements([1,1,2], [2,3,4]))
print(uncommon_elements([1,2,3], [4,5,6]))
print(uncommon_elements([1,1,2,3,4,2], [1,3,4,5]))

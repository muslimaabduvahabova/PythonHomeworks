#### 1 Age Calculator
from datetime import datetime

name = 'Jacob'
year = 1992

current_year = datetime.now().year
age = current_year - year

print(f"hello, {name}, you are {age} years old")
#### 2 Extract Car Names
txt = 'LMaasleitbtui'
txt [1:13:2]
txt [0:13:2]
#### 3 Extract Car Names
txt1 = 'MsaatmiazD'
txt1 [0:10:2]
txt1 [1:10:2]
car = txt1[9] + txt1[2] + txt1[5] + txt1[7] + txt1[1] 
print(car)
### 4 Extract Residence Area
txt2 = "I'am John. I am from London"
parts = txt2.split("from")
area = parts[1].strip()
print(area)
#### 5 Reverse String
name
name [::-1]
print(name [::-1])
#### 6 Count Vowels
text = input('enter a string')
vowels = "aeiouAEIOU"
count = 0
for char in text:
    if char in vowels:
        count += 1
print('Number of vowels', count)
#### 7. Find Maximum Value
nums = input("Enter numbers separated by spaces: ")
nums_list = nums.split()
nums_int = [int(num) for num in nums_list]
print('Maximum value: ', max(nums_int))
#### 8. Check Palindrome
words = input('enter a word')
if words == words[::-1]:
    print("It's a palindrome!")
else:
    print('not a palindrome.')
#### 9. Extract Email Domain
email = input()
domain = email.split('@')[1]
print('Domain: ', domain)
#### 10. Generate Random Password
import random 
chars = "abcdefg12345"
password = 'm8s5i6a1'

for i in range(8):
    password += random.choice(chars)
print('Password: ', password)

#### 1. Leap Year Function
def is_leap(year):
    """
    Determines whether a given year is a leap year.

    A year is a leap year if:
    - It is divisible by 4, and
    - It is NOT divisible by 100, unless it is also divisible by 400.

    Parameters:
    year (int): The year to be checked.

    Returns:
    bool: True if the year is a leap year, False otherwise.
    """
    if not isinstance(year, int):
        raise ValueError("Year must be an integer.")
    
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

year = int(input('Enter a year: '))
print(is_leap(year))
##### another option
def is_leap(year):
    """
    Determines whether a given year is a leap year.

    A year is a leap year if:
    - It is divisible by 4, and
    - It is NOT divisible by 100, unless it is also divisible by 400.

    Parameters:
    year (int): The year to be checked.

    Returns:
    bool: True if the year is a leap year, False otherwise.
    """
    if not isinstance(year, int):
        raise ValueError("Year must be an integer.")
    
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

year = 2024
print(is_leap(year))
 #### 2. Conditional Statements Exercise
n = 7

if n % 2 != 0:
    print('wierd')
elif n % 2 == 0 and 2 <= n <= 5:
    print('not wierd')
elif n % 2 == 0 and 6 <= n <= 20:
    print('wierd')
elif n % 2 == 0 and n > 20:
    print('not wierd')
#### 3. Even Numbers Between a and b
a = 4
b = 12
if a > b:
    a, b = b, a
start = a if a % 2 == 0 else a + 1
even_numbers = list(range(start, b + 1, 2))

print (even_numbers)

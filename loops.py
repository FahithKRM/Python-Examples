# Python has two types of loops(for and while)

# Type 1 - For
# for loop mostly used we know the number of iterations (no of times repeat the process)
"""
for i in range(1, 10):
    print(i)
"""

# Type 2 - While
# for loop mostly used we dontn't know the number of iterations (no of times repeat the process)
"""
i = 0 
while(i <= 10):
    print(i)
    i += 1
"""

###---------------------------------------------------------------------------------------------###


# 1. Iterate through a list of numbers: Create a list of numbers and 
# use a for loop to print each number.
"""list = [23, 45, 89, 90, 14, 67, 98, 37, 29, 10]

for num in list : 
    print(num, end=' ')"""


# 2. Sum of numbers: Write a for loop to calculate the sum of all numbers in a list.
"""total = 0
for num in list :
    total += num
print("\nTotal : ", total)"""

# 3. Count occurrences: Use a for loop to count how many times a specific element appears in a list.
"""char = ['a', 'r', '6', '7', '0', 'a', 'b', 'a', '6', 'a']
target = 'a'

count = 0
for ch in char:
    if ch == target:
        count += 1
print("\'", target, "\' occures in ", count, ' times')"""

# 4. Print a pattern: Use nested for loops to print a pattern, like a triangle of stars.


"""for i in range(1, 3):
    for i in range(1, 7):
        print('+', end='')
    print()

for i in range(1, 5):
    for i in range(1, 3):
        print(" ", end='')

    for i in range(1, 3):
        print("+", end='')

    for i in range(1, 3):
        print(" ", end='')
    print()

for i in range(1, 3):
    for i in range(1, 7):
        print('+', end='')
    print()"""

# 5. Iterate through a dictionary: Create a dictionary and use a for loop to print each key-value pair.
"""price_list = {'Tea':80, 'Bun':250, 'Ticket':1300, 'Water':190, 'Juice':160}

total = 0
for key, value in price_list.items():
    total += value
    print(key, " : ", value)
print("Total price List : ", total)
cash = int(input("Customer give the cash : "))
print(f"Balance give to the customer is ",cash-total)"""

# 6. Find the maximum value: Write a for loop to find the maximum value in a list of numbers.
"""max_num = list[0]

for num in list:
    if max_num < num :
        max_num = num

print("Maximum number is : ", max_num)"""

# 7. Filter elements: Use a for loop to create a new list that contains only the elements that meet a certain condition (e.g., all even numbers from a list).
"""for num in list:
    if num %2 == 0 : 
        print(num, end=' ')"""



# 8. Read 10 numbers and find the average

# total = 0
# for _ in range (1, 11):
#     num = int(input(f"Enter the number  : "))
#     total += num
# print("Average of the value : ", total/10)

# 9. Read 5 numbers and return its cubic

# for i in range(1, 6):
#     print(f"{i}^3 = {i**3}")




######### While Loop #########i = 0
"""while(i == 0):
    print("True")
    i = 1
"""
# Print Numbers from 1 to 10:
# Write a while loop that starts at 1 and increments by 1 until it reaches 10, printing each number.
"""i = 1
while(i <= 10):
    print(i, end=' ')
    i += 1
    """

# Sum of First 10 Natural Numbers:
# Use a while loop to calculate the sum of the first 10 natural numbers (1 through 10).

"""i = 1
total = 0
while(i <= 10):
    total += i
    i += 1
print("Sum of first 10 numbers", total)"""

# Guess the Number Game:
# Create a game where the computer randomly selects a number between 1 and 100. The user has to guess the number, and the program should keep asking for guesses until the user gets it right, providing hints if the guess is too high or too low.
"""import random
randomNum = random.randint(1, 100)
count = 0 

while (True):
    inputNum = int(input("Enter the number : "))
    count += 1
    if randomNum > inputNum : 
        print("Too Low")
    elif randomNum < inputNum : 
        print("Too High")
    else :
        print("You Guessed it! ❤️ after {count} attemts!")
        break"""

# Factorial Calculation:
# Write a while loop to calculate the factorial of a given number. The factorial of a number ( n ) is the product of all positive integers less than or equal to ( n ).in
"""num = int(input("Enter the number : "))
result = 1
print(f"{num}! = ", end='')
while(num >= 1):
    result *= num
    num -=1
print(f"{result}")"""




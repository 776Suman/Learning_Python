# %% [markdown]
# # Module 2: Control Flow Assignments
# ## Lesson 2.1: Conditional Statements
# ### Assignment 1: Simple if Statement
# 
# Write a program that asks the user to input a number and prints whether the number is positive.
# 
# ### Assignment 2: if-else Statement
# 
# Write a program that asks the user to input a number and prints whether the number is positive or negative.
# 
# ### Assignment 3: if-elif-else Statement
# 
# Write a program that asks the user to input a number and prints whether the number is positive, negative, or zero.
# 
# ### Assignment 4: Nested if Statement
# 
# Write a program that asks the user to input a number and prints whether the number is positive and even, positive and odd, or negative.
# 
# ## Lesson 2.2: Loops
# ### Assignment 5: for Loop
# 
# Write a program that prints all the numbers from 1 to 10 using a for loop.
# 
# ### Assignment 6: while Loop
# 
# Write a program that prints all the numbers from 1 to 10 using a while loop.
# 
# ### Assignment 7: Nested Loops
# 
# Write a program that prints a 5x5 grid of asterisks (*) using nested loops.
# 
# ### Assignment 8: break Statement
# 
# Write a program that asks the user to input numbers until they input 0. The program should print the sum of all the input numbers.
# 
# ### Assignment 9: continue Statement
# 
# Write a program that prints all the numbers from 1 to 10 except 5 using a for loop and continue statement.
# 
# ### Assignment 10: pass Statement
# 
# Write a program that defines an empty function using the pass statement.
# 
# ### Assignment 11: Combining Loops and Conditionals
# 
# Write a program that asks the user to input a number and prints all the even numbers from 1 to that number using a for loop.
# 
# ### Assignment 12: Sum of Digits
# 
# Write a program that calculates the sum of the digits of a number input by the user using a while loop.
# 
# ### Assignment 13: Prime Number Check
# 
# Write a program that checks if a number input by the user is a prime number using a for loop.
# 

# %%
#assignment 1
#question 1
num = int(input("Enter a number: "))
if num>0:
    print("The number is positive.")

# %%
##assignment 5
##question 5
for i in range(1,11):
    print(i)


# %%
##assignment 6
##question 6
i = 5
while i <=10:
    print(i)
    i += 1

# %%


# %%
##assignment 7
##question 7
for i in range(5):
    for j in range(5):
        print("*", end="")
    print()

# %%
##assignment 8
##question 7
total = 0
while True:
    num = int(input("Enter a number (0 to stop):"))
    if num == 0:
        break
    total += num
print("Sum:", total)

# %%
##assignment 9
##question 9
for i in range(1,11):
    if i ==5:
        continue
    print(i)

# %%
##assignment 10
##question 10
for i in range(5):
    pass # Placeholder for future Logic

# %%
##assignment 11
##question 11
num = int(input("Enter a number:"))
for i in range(1,num+1):
    if i %2==0:
        print(i)


# %%
##assignment 12
##question 12
num = int(input("Enter a number:"))
total = 0
while num>0:
    digit = num %10
    total += digit
    num //=10
print("Sum of digits:", total)

# %%
##assignment 13
##question 13
num = int(input("Enter a number:"))
if num <= 1:
    print("Not a prime number")
else:
    is_prime = True
    for i in range(2,num):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print("Prime number")
    else:
        print("Not a prime number")

# %%
#assignment 2
#question 2
num = int(input("Enter a number: "))
if num > 0:
    print("The number is positive.")
else:
    print("The number is negative.")

# %%
#assignment 3
#question 3
num = int(input("Enter a number: "))
if num > 0:
    print("The number is positive.")
elif num < 0:
    print("The number is negative.")
else:
    print("The number is zero.")



# %%
#assignment 4
##question 4
num = int(input("Enter a number: "))
if num > 0:
    print("The number is positive.")
elif num < 0:
    print("The number is negative.")
else:
    print("The number is zero.")



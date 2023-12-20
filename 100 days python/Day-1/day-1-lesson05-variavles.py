'''
Instructions
This program takes two inputs. The first input is stored in a variable called a. The second input is stored in a variable called b.

Write a program that switches the values stored in the variables a and b.

Warning . You don't need to print anything. The print statement is already in the template code. However, your program should work for different inputs. e.g. any value of a and b.
'''

# There are two variables, a and b from input
a = input()
b = input()
# 🚨 Don't change the code above ☝️
####################################
# Write your code below this line 👇

c = a
a = b
b = c


# 🚨 Don't change the code below 👇
print("a: " + a)
print("b: " + b)


'''
Resposta: 

# There are two variables, a and b
a = input()
b = input()
# Create a third variable to help switch the values
c = a
a = b
b = c

print("a: " + a)
print("b: " + b)

'''
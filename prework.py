# Question 1
# Write a function to print "hello_USERNAME!" USERNAME is the input of the function.
from operator import truediv


def hello_name(username):
    print("Hello, " + username + "!")

username = input("Please enter your username: ")
hello_name(username)


# Question 2
# Write a python function, first_odds that prints the odd numbers 
# from 1-100 and returns nothing
def first_odds():
   for list in range (1,100,2):
    print(list)
print(first_odds())
# You don't need the print() around first_odds() 
# unless you want to print "None" 
# which I think thats what the question is asking


# Question 3
# Please write a Python function, 
# max_num_in_list to return the max number of a given list.

def max_num_in_list(a_list):
    print(max(a_list))

a_list = list(range(0,10))
max_num_in_list(a_list)

# Question 4
# Write a function to return if the given year is a leap year. 
# A leap year is divisible by 4, but not divisible by 100, 
# unless it is also divisible by 400.
# The return should be boolean Type (true/false).

def is_leap_year(a_year):
    if int(a_year) % 400 == 0:
        return True
    if int(a_year) % 100 == 0:
        return False
    if int(a_year) % 4 == 0:
        return True
    else:
        return False
print(is_leap_year(2300))
print(is_leap_year(2004))

# Question 5
# Write a function to check to see if all numbers in list are consecutive numbers. 
# For example, [2,3,4,5,6,7] are consecutive numbers, 
# but [1,2,4,5] are not consecutive numbers. 
# The return should be boolean Type.

def is_consecutive(a_list):
    return sorted(a_list) == list(range(min(a_list), max(a_list)+1))
    
print(is_consecutive(a_list))
            
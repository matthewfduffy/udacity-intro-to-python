"""
    #20. Practice Debugging
    In the workspace below there is a piece of code in the `user_input_numlist.py` Python file. 
    The code prompts the user to enter 10 two-digit numbers. 
    It should then find and print the sum of all of the even numbers among those that were entered.

    But there is a bug in the code:
    When a user enters a number, they get the following TypeError. 

    `TypeError: Not all arguments converted during string formatting`
    
    [Expected Output:]
        >>> user_list: [23, 24, 25, 26, 27, 28, 29, 30, 31, 22]
        >>> The sum of even numbers in user_list is: 130.
"""


# This is the base program. Leave commented out for reference.
# user_input_numlist.py
# initiate empty list to hold user input and sum value of zero
# user_list = []
# list_sum = 0

# # seek user input for ten numbers 
# for i in range(10):
#     userInput = input("Enter any 2-digit number: ")
    
# # check to see if number is even and if yes, add to list_sum
# # print incorrect value warning  when ValueError exception occurs
#     try:
#         number = userInput
#         user_list.append(number)
#         if number % 2 == 0:
#             list_sum += number
#     except ValueError:
#         print("Incorrect value. That's not an int!")

# print("user_list: {}".format(user_list))
# print("The sum of the even numbers in user_list is: {}.".format(list_sum))

# Debugging Script Above
user_list = []
list_sum = 0

# seek user input for ten numbers 
for i in range(10):
    userInput = input("Enter any 2-digit number: ")
    try:
        number = int(userInput)     # cast userInput to int
        user_list.append(number)
        if number % 2 == 0:
            list_sum += number
    except ValueError:
        print("Incorrect value. That's not an int!")

print("user_list: {}".format(user_list))
print("The sum of the even numbers in user_list is: {}.".format(list_sum))
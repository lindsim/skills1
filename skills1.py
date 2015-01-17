# Things you should be able to do.

number_list = [-5, 6, 4, 8, 15, 16, 23, 42, 2, 7]
word_list = [ "What", "about", "the", "Spam", "sausage", "spam", "spam", "bacon", "spam", "tomato", "and", "spam"]

# Write a function that takes a list of numbers and returns a new list with only the odd numbers.
def all_odd(number_list):
    new_list = []
    for item in number_list:
        if item % 2 == 1:
            new_list.append(item)

    return new_list

# Write a function that takes a list of numbers and returns a new list with only the even numbers.
def all_even(number_list):
    new_list = []
    for item in number_list:
        if item % 2 == 0:
            new_list.append(item)

    return new_list
    

# Write a function that takes a list of strings and a new list with all strings of length 4 or greater.
def long_words(word_list):
    new_list = []
    for item in word_list:
        if len(item) >= 4:
            new_list.append(item)

    return new_list

# Write a function that finds the smallest element in a list of integers and returns it.
def smallest(number_list):
    current_low = number_list[0]
    for x in range (1, len(number_list)):
        if current_low > number_list[x]:
            current_low = number_list[x]
         
    return current_low

# Write a function that finds the largest element in a list of integers and returns it.
def largest(number_list):
    current_high = number_list[0]
    for x in range (1, len(number_list)):
        if current_high < number_list[x]:
            current_high = number_list[x]
         
    return current_high

# Write a function that takes a list of numbers and returns a new list of all those numbers divided by two.
def halvesies(number_list):
    new_list = []
    for item in number_list:
        new_list.append(item / 2.0)

    return new_list

# Write a function that takes a list of words and returns a list of all the lengths of those words.
def word_lengths(word_list):
    new_list = []
    for item in word_list:
        new_list.append(len(item))
    
    return new_list

# Write a function (using iteration) that sums all the numbers in a list.
def sum_numbers(number_list):
    total = 0
    for num in number_list:
        total = total + num
  
    return total 

# Write a function that multiplies all the numbers in a list together.
def mult_numbers(number_list):
    total_multiply = number_list[0]
    for x in range (1, len(number_list)):
        total_multiply = total_multiply * number_list[x]
  
    return total_multiply 

# Write a function that joins all the strings in a list together (without using the join method) and returns a single string.
def join_strings(word_list):
    giant_string = ""
    for item in word_list:
        giant_string = giant_string + item
  
    return giant_string


# Write a function that takes a list of integers and returns the average (without using the avg method)
def average(number_list):
    x = sum_numbers(number_list)
    ave = x / len(number_list)
    return ave








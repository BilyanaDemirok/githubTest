# Task_1: Define a variable named 'my_first_string_variable' and 
#   assign 'This is a string type content.' value to it.
# Solution:
my_first_string_variable = 'This is a string type content.'


# Task_2: Print the value of my_first_string_variable to stdout.
# Solution:
print(my_first_string_variable)

# Task_3: Print the value of my_first_string_variable to stdout as in the following format:
#   'Value of my_first_string_variable: This is a string type content.'
#   Hint: Use string substantiation.
# Solution:
print(f'Value of my_first_string_variable: This is a string type content')


# Task_4: Define two integer variables named 'num_1' and 'num_2' with the values of 100 and 200 respectively.
# Solution:
num_1, num_2 = 100, 200

# Task_5: Substract num_1 from num_2 and assing the result to a variable named 'substracted'.
# Solution:

num_1, num_2 = 100, 200
substracted = num_2 - num_1
print(substracted)

# Task_6: Print the value of substracted variable in the format of 'The result of substracting 100 from 200 equals to 100.'
#   Hint: Use string substantiation for all the variables involved in the substraction.
# Solution:
print('The result of substracting 100 from 200 equals to 100.')

# Task_7: 
#   - Define a string type variable named 'name' with the value of 'John'.
#   - Define a string type variable named 'lastname' with the value of 'Doe'.
# Print 'My name is John Doe.' to stdout by using string concatanation.
# Solution:
name = 'John'
lastname = 'Doe'
print('My name is ' +name +' '+lastname)

# Task_8: Define a list type variable named 'favorite_colours' with the value of 'black', 'red', 'orange'.
# Solution:
favorite_colours_list = ['black', 'red', 'orange']
print(favorite_colours_list)

# Task_9: Print the second item of the favorite_colours as: 'The second favorite of colour is red.'
# Hint: Use string substitution.
# Solution:
favorite_colours_list = ['black', 'red', 'orange']
favorite_cities = ['rome', 'madrid', 'paris']
print(f'The second favorite colour is {favorite_colours_list[1]}')
print(f'the sum of 2 and 3 equals {2+3}')

# Task_10: Add 'blue' to the favorite_colours list.
# Solution:
favorite_colours_list = ['black', 'red', 'orange']
favorite_colours_list.append('blue')
print(favorite_colours_list)

# Task_11: Print the following messages to the stdout.
#   'The content of the favorite_colours list: ['black', 'red', 'orange', 'blue']'
#   'The length of favorite_colours list is 4.'
# Hint: Use 2 print statements.
# Solution:
content = ['black', 'red', 'orange', 'blue']
print(len(content))

# Task_12: Print the first 2 items of the favorite_colours list by using list slicing.
# Solution:
content = ['black', 'red', 'orange', 'blue']
print(content[:2])

# Task_13: Print the content of the favorite_colours list as:
#   1 - black
#   2 - red
#   3 - orange
#   4 - blue
# Solution:
favorite_colours = ['black', 'red', 'orange', 'blue']
for item in favorite_colours:
    print(f'{favorite_colours.index(item) +1} - {item}')

# Task_14: Define a dictionary variable with the name of 'user' and 
#   assign keys 'name', 'lastname', 'favorite_colours' with the previously (see above tasks) defined values.
# Solution:
user = {'name': name, 'lastname': lastname, 'favorite_colours': favorite_colours}


# Task_15: Print the user variable.
# Solution:
print(user)


# Task_16: Add a new key 'age' to the 'user' variable with the value of 39. And, print the user.
# Solution:
user['age'] = 39


# Task_17: Update the last favorite colour of the user variable as 'white'. Print the user.
# Solution:
user['favorite_colours'][-1] = 'white'
print(user)

#Your first python program
from pygame import Color


print("Leonardo Adorkor")
print('o------')
print(' ||||')
print('🧒' * 10)

# Variables
price = 10 # Numbers
rating = 4.9 # Floats
name = 'Leo' # Stings
is_published = True #Boolean
print(price) 

#Check in a patient named John Smith.He's 20 years old and is a new patient
full_name = 'John Smith'
age = 20
is_new = True

# Gettin' input
Food = input('What is your favourite food? ')
print(Food + ' good')

# Exercise
# Ask two questions: person's name and favourite colour.
# Then, print a message like "Mosh likes blue"
name = input('What is your name? ')
print('Hi ' + name)
Color = input('What is your favourite color? ')
print(Color + ' Nice')

# Type conversion
birth_year = input('Birth year: ')
age = 2024 - int(birth_year)
print(age)

# Ask a user their weight(in pounds), convert it to kilograms and print on the terminal.
weight_lbs = input('Weight (lbs): ')
weight_kg = int(weight_lbs) * 0.45
print(weight_kg)

#Strings
course = '''    
Hi John,

Here is our first email to you

Thank you,
The support team.

'''
print(course)



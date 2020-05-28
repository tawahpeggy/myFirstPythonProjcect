# #
# # print(""+'*'+""+""+"*")
# # print("*"+''+"*"+""+"*"+"")
# # print("*"+''+""+""+"*")
# # print(""+'*'+""+"*"+"")
# # print(""+''+"*"+""+"")
# # print("Baby Bru love")
# # # variables
# # patient_name = 'john smith'
# # patient_age = 20
# #
# # is_a_new_patient = True
# # print(patient_name)
# # receiving user input and printing
# # name = input('what is your full name ')
# # color = input('what is your most favourite color ')
# # print("wow! nice name u got there " + name + "." + " i like " + color + " too! ")
# # # type conversion
# # # a program that takes as input year_of _birth and prints out age.
# birth_year = input('please input your year of birth:')
# age = 2020 - int(birth_year)
# # print('you are :')
# # print(age)
# # getting the type
# print(type(birth_year))
# print(type(age))
# # a program to convert kg into pounds
# weight = input("how much do you weight in kg ")
# pound = int(weight) * 2.205
# print(pound)
# # inverse ie pound to kg
# p_weight = input("how much do u weight in pounds")
# kilogram = int(p_weight)/2.205
# print(kilogram)
# # strings
# # index of a string
# name = 'tawah peggy che nico'
# print(name[10])
# # negative index prints from the back
# print(name[1:7])
# # multiple line string
# desert = '''thanks for the dessert
# am excited to try
# i love u'''
# print(desert)
# # cloning a string
# surName = name[:]
# print(surName)
# # exercise
# name = 'peggy'
# print(name[1:-1])
# # formatted strings
# fName = 'peggy'
# lName ='tawah'
# message = f'{fName}  {[ lName ]} is a software engineer'
# print(message)
# # string inbuilt methods
# course = 'python for BEginners'
# # get length
# print(len(course))
# # to uppercase
# print(course.upper())
# # to lowercase
# print(course.lower())
# # getting index of a value
# print(course.find('t'))
# # check if a character exist
# print('python' in course)
# # arithmetic operations
# print(23+10)
# print(23-10)
# print(23/10)
# print(23*10)

# Math functions
# import math
# math_functions = -17.5
# print(math.floor(math_functions))
# print(math.ceil(math_functions))
# print(abs(math_functions))
# print(round(math_functions))
# # if statement
# is_hot = True
# is_cold = False
# if is_hot:
#          print("it's a hot day please be sure to drink plenty of water")
# #  if else
# elif is_cold:
#             print("its a cold day be sure to wear warm cloths and stay indoors")
# else:
#     print('its a lovely day')
# print("it's always a lovely day")
# # if else exercise
# house_price = 1000000
# good_credit = True
# good_percent = 10/100
# bad_percent = 20/100
# bad_credit = True
# if good_credit:
#                x = house_price * good_percent
#                print('the down payment  with good_credit is:')
#                print(x)
# elif bad_credit:
#                 y = house_price * bad_percent
#                 print('the down payment  with bad_credit is:')
#
#                 print(y)
# else:
#     print("sorry you can't afford the property")
# # logical operators
# # exercises
# print(' please answer with a True or False ')
# income = input(' please do you have a steady income? ')
# good_credit = input(' please have you ever been recommended with a good credit? ')
# if income == 'True' and good_credit == 'True':
#     print(' u have been selected for the job ')
# elif income == 'True' or good_credit == 'True':
#     print(' you have been selected but will need to go through a 3 months training ')
# elif good_credit == 'True':
#     print(''' you have been selected but will need
#            to increase your income from somewhere in the next 3months so as to get u to
#            have an increase in 40percent salary ''')
# elif income == 'True':
#     print(''' you have been selected but will need good reviews
#             from somewhere in the next 3months so as to get u to have
#              an increase in 40 percent salary''')
# elif income == 'False' and good_credit == 'False':
#     print(" you have lost the job ")
# else:
#     print('re-apply!')
# # comparative operators
# # exercise
# temperature = 30
# if temperature > 30:
#     print('its a hot day')
# elif temperature < 10:
#     print('its a cold day')
# else:
#     print('its neither hot nor cold')
# # exercise
# name = input(' please input your name ')
# if len(name) < 3:
#     print('name is too short')
# elif len(name) > 50:
#     print('name is toooo long')
# else:
#     print('name looks good')
# # project:weight converter
# weight = input("how much do you weigh ?")
# type = input(" was your input in kilogram or in pounds ")
# if type == 'kilogram' or type == 'Kilogram' or type == 'KILOGRAM':
#     print(f' you are: {int(weight) * 2.205} l(bs)')
# elif type == 'pounds' or type == 'POUNDS' or type == 'Pounds':
#     print(f' you are: {int(weight)/2.205} kg')
# else:
#     print('you are weightless')
# while loops
name = 1
while name <= 10:
    print('*' * name)
    name = name + 1
print('done')
# Guessing game challenge
guess_number = 10
guess_limit = 3
guess_time = 0
while guess_time < guess_limit:
    guessing_trial = int(input(' please guess a number between 1 to 10 '))
    guess_time += 1
    if guessing_trial == guess_number:
        print('congratulations! You win')
        break
else:
    print('Sorry Try Again!')
# # car game
# start = 'car started! Ready to go'
# stop = 'car stopped'
# quit = 'quit'
# help = input('what do you want')
# if help==help or help== Help or help==HELP:





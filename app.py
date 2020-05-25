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
import math
math_functions = -17.5
print(math.floor(math_functions))
print(math.ceil(math_functions))
print(abs(math_functions))
print(round(math_functions))
# if statement
is_hot = True
is_cold = False
if is_hot:
         print("it's a hot day please be sure to drink plenty of water")
#  if else
elif is_cold:
            print("its a cold day be sure to wear warm cloths and stay indoors")
else:
    print('its a lovely day')
print("it's always a lovely day")


# Erika Tatiana Gomez Caballero
# homework
from faker import Faker
import random
# Explique que es una lista y de un ejemplo

'''
. A list is an ordered sequence of elements, it can include all types of data
. It is mutable, meaning it can be replaced or changed.
'''

names = ['Tatiana', 'Yeison', 'Sofia', 'Lauren']
print(f'This is an example of lists: {names}')

# a.Create a Python list called plants containing the names of three plants.
plants = ['pinos','ginko', 'cicas']
print(plants)

# b.Append a new plant to the list plants and print the updated list.
plants.append('cedro')
print(plants)

# 2.Tuples: explain what a tuple is and give an example.

'''
. A tuple is a collection of immutable elements, that is, 
they cannot be modified.

. takes up less memory space

. they go inside parentheses
'''
# ejemplo:
numeros = (1,2,3,4,5)
print(f'This is an example of tuples: {numeros}')

# a.Create a tuple named colors containing the names of three colors. Print the
# tuple.

colors = ('pink', 'black', 'blue')
print(colors)

'''b. Try to modify the first element of the tuple colors and observe the result.
Explain why you encountered an error or not.
'''
# TypeError: 'tuple' object does not support item assignment

# 3.Sets: explain what a set is and give an example.

'''
. A set is a collection of elements, which has no repeated elements, 
are immutable and cannot be indexed.

. It can be inside braces or inside parentheses and square brackets.
'''
setejemplo = {1,2,3,4,5,6,7}
print(f'This is a example of sets: {setejemplo}')

''' a.Create two sets, set1 and set2, containing some numbers. Find and print
the intersection of these two sets.
'''

set1 = {1,2,3}
set2 = {3,4,5,6}

intersection = set1 & set2
print(intersection)

'''
b.Add a new element to set1 and remove an element from set2. Print both
sets after these operations.
'''

set1.add(7)
set2.remove(3)

print(set1, set2)

# 4.Dictionaries: explain what a dictionary is and give an example.

'''
. A dictionary is a collection of pairs with their key value

. cannot be indexed
'''

nombres = {'nombres': ['tati', 'sofi'],
           'ciudades': ['Popayan', 'Barcelona']
           }

print(f'This is a example of dictionary: {nombres}')

'''
a.Create a dictionary called student with keys "name", "age", and "grade",
and assign appropriate values. Print the dictionary.
'''

student = {'name': 'Tati',
           'age': 25,
           'grade': 'Biologist'
           }
print(student)

'''
b. Update the age of the student in the dictionary and print the updated
dictionary.
'''

student['age'] = 26

print(student)

'''
5. Make a comparison about Lists, Tuples, Sets and Dictionaries. Explain when to use
each of these collections.
'''

'''
Lists are mutable, so any type of data can be added.

A tuple being immutable can be used in cases where we do not want our information 
to be changed.

We can use the set when we do not want two elements to share the same information.

Since the dictionary is key value, we can use it when we need to join several 
elements that belong to a key
'''

# Exercise: Weather Data Analysis

'''
1. Data: Create two lists:
• cities: containing the names of different cities (e.g., "New York", "London", "Tokyo").
• temperatures: containing the current temperatures (in Celsius) of corresponding
cities.
'''

fake = Faker('es_ES')
cities = [fake.city() for _ in range(20)]
print(cities)

temperatures = [round(random.uniform(-10, 40), 2) for _ in range(20)]
print(temperatures)

'''
a. Define a function named analyze_weather that takes the following parameters:
• city_names: A list containing the names of cities.
• city_temperatures: A list containing the current temperatures of
corresponding cities.

b. Inside the function, iterate through the lists of city names and temperatures. For
each city:
• Check if the temperature is above 20 degrees Celsius.
• If the temperature meets the condition, print a message indicating that it's a
warm day in the city.
• If the temperature is 20 degrees Celsius or below, print a message indicating
that it's a cool day in the city.
'''


def analize_weather(cities, temperatures):
    for c, t in zip(cities, temperatures):
        print(f'the city of  {c} have a temperature of: {t} grades')
        if t > 20:
            print(f'{c} have a warm day')
        else:
            print(f'{c} it is a cool day')


analize_weather(cities, temperatures)

'''
c. Create a new function to print the average temperature for all the cities.
'''


def average_temperature(temperatures):
    average = sum(temperatures)/len(temperatures)
    return average

result = average_temperature(temperatures)
print(f'The average temperature es: {result} grades')

# d. Print the max temperature for all the cities and print the name of the city.


def temperature(cities, temperature):
    max_temperature = max(temperature)
    maximum_index = temperature.index(max_temperature)
    city_maximum_temperature = cities[maximum_index]
    print(f'the hottest city is  {city_maximum_temperature}, with {max_temperature} grades')


temperature(cities, temperatures)

# 3. Create a similar exercise with data from your domain.
bacterias = ['psicrófilos', 'termofilas', 'basofilas']
temperaturas_a_sobrevivir = [-34, 45, 27]

print(f'Existen algunos tipos de microorganismos como: {bacterias}')
print(f'Las tenperaturas a las que sobreviviven las anteriores bacterias{temperaturas_a_sobrevivir}')


def bacterias_y_entorno(bacterias, temperaturas_a_sobrevivir):

    for b,t in zip(bacterias, temperaturas_a_sobrevivir):
        if t > 40:
            print(f'Esta bacteria llamada {b} le gusta vivir en entornos calientes')

        elif t < 0:
            print(f'A las bacterias {b}, le gusta vivir en ambientes muy frios')

        else:
            print(f'A las bacterias {b}, no le gusta vivir en ambientes extremos')


bacterias_y_entorno(bacterias,temperaturas_a_sobrevivir)

# Classwork
''' 1) If/Else:
a) Write a Python program that checks if a given number is even or odd. Print "Even"
if the number is even, and "Odd" if it's odd.
b) Modify the previous program to check if a number is positive, negative, or zero.
Print the corresponding message.'''


def par(num):
    if num % 2 == 0:
        print('Es par')
    else:
        print('Es impar')


par(6)


def positivo(num):
    if num == 0:
        print('es cero')

    elif num < 0:
        print('Es negativo')

    else:
        print('ES positivo')

positivo(-2)

'''
2) For and while
a) Write a Python program to print the square of each number from 1 to 5 using a for
loop.
'''
def cuadrado():
    for numero in range(1,6):
        print(numero ** 2)


cuadrado()

# Write a Python program to show the sum of the numbers from 1 to 100.
def suma_total():
    suma = 0
    for su in range(1, 101):
        suma = suma + su
    return suma


resultado = suma_total()
print(resultado)

# while
n = 5
while n <= 5:
    print(n**2)
    n = n + 1
# fibonnacii
fibonnaci = [0,1]
n = 2
while(n < 30):
    fibonnaci.append(fibonnaci[n-1] + fibonnaci[n-2])
    n = n + 1
print(fibonnaci)

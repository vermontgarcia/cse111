"""
Author: Vermont Garcia
Program: tire_volume
Purpose: Write a Python program that calls functions and methods to get the current date and to append values to a text file.

Problem Statement:

  Many companies wish to understand the needs and wants of their customers more deeply so the company can create products that
  fill those needs and wants. One way to understand customers more deeply is to record the values entered by customers while they
  are using a program and then to analyze those values. One common way to record values is for a program to store them in a file.

Milestone Requirements:

  The size of a car tire in the United States is represented with three numbers like this: 205/60R15. The first number is the width of the tire in millimeters.
  The second number is the aspect ratio. The third number is the diameter in inches of the wheel that the tire fits. The volume of space inside a tire can be
  approximated with this formula:

      v = π*w^2*a(w*a + 2,540*d)/10,000,000,000

  Where:
    - v is the volume in liters,
    - π is the constant PI, which is the ratio of the circumference of a circle divided by its diameter (use math.pi),
    - w is the width of the tire in millimeters,
    - a is the aspect ratio of the tire, and
    - d is the diameter of the wheel in inches.

  - Write a Python program that reads from the keyboard the three numbers for a tire and computes and outputs the volume of space inside that tire.

Core Requirements:

  The prove milestone required you to write a program named tire_volume.py that computes the approximate volume of air inside a tire.
  
  Add code near the end of that program that does the following:

    - Gets the current date from the computer’s operating system.
    - Opens a text file named volumes.txt for appending.
    - Appends to the end of the volumes.txt file one line of text that contains the following five values:
      - current date (Do NOT include time)
      - width of the tire
      - aspect ratio of the tire
      - diameter of the wheel
      - volume of the tire (rounded to two decimal places)

    - Write (appending rows) data entered to a file volumes.txt with a csv format without headers following the next format:
      2020-03-18, 185, 50, 14, 24.09
      2020-04-16, 205, 60, 15, 39.92

Exceeding the Requirements:

  - Find tire prices for four or more tire sizes online. Add a set of if … elif … else statements in your program that use the tire width, tire aspect ratio,
    and wheel diameter that the user enters to find a price and then print the price.
  
  - After your program prints the tire volume to the terminal window, your program should ask the user if he wants to buy tires with the dimensions that
    user entered. If the user answers “yes”, your program should ask for her phone number and store her phone number in the volumes.txt file.
    
    2020-03-18, 185, 50, 14, 24.09
    2020-04-16, 205, 60, 15, 39.92, 55.87, 9182736450
"""

from math import pi
from datetime import datetime

def main():
  w = int(input('Enter value for width: '))
  a = int(input('Enter value for aspect ratio: '))
  d = int(input('Enter value for diameter of the wheel: '))

  v = round(pi*w*w*a*(w*a + 2540*d)/10000000000, 2)
  
  print(f'The aproximate volume for a tire: {w}/{a}R{d} is: {v} liters')

  price = get_price(w,a,d)

  if price != None:
    formated_price = f'{price: .2f}'.strip()
    print()
    print(f'The price for a tire {w}/{a}R{d} is $ {formated_price}')
    print()
    user_want_but = input('Do you want to by a tire y/n? ')
    if (user_want_but == 'y'):
      phone = input('Please enter your phone number: ')
      with open('volumes.txt', 'at') as volumes_file:
        print(f'{get_date()}, {w}, {a}, {d}, {v}, {formated_price}, {phone}', file=volumes_file)
    else:
      with open('volumes.txt', 'at') as volumes_file:
        print(f'{get_date()}, {w}, {a}, {d}, {v}, {formated_price}', file=volumes_file)
  else:
    with open('volumes.txt', 'at') as volumes_file:
      print(f'{get_date()}, {w}, {a}, {d}, {v}', file=volumes_file)

def get_date():
  return f'{datetime.now(): %Y-%m-%d}'

def get_price(w,a,d):
  tire_type = f'{w}/{a}R{d}'

  prices = {
    '185/50R14': 85.23,
    '205/60R15': 113.40,
    '275/55R20': 260.57,
    '255/70R17': 285.99
  }

  try:
    return prices[tire_type]
  except:
    return None

main()

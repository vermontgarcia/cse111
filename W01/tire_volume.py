"""
Author: Vermont Garcia
Program: tire_volume
Purpose: Write a Python program that gets input from a user, performs arithmetic, and displays results for the user to see..

Core Requirements:

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
"""

from math import pi

def main():
  w = int(input('Enter value for width: '))
  a = int(input('Enter value for aspect ratio: '))
  d = int(input('Enter value for diameter of the wheel: '))

  v = pi*w*w*a*(w*a + 2540*d)/10000000000

  print(f'The aproximate volume for a tire: {w}/{a}R{d} is: {v: .2f} liters')

main()

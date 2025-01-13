"""
Author: Vermont Garcia
Program: boxes
Purpose: Write a Python program that calculates the number of boxes required to pack the provided number of items.


A manufacturing company needs a program that will help its employees pack manufactured items into boxes for shipping. Write a Python program named boxes.py that asks the user for two integers:

the number of manufactured items
the number of items that the user will pack per box
Your program must compute and print the number of boxes necessary to hold the items. This must be a whole number. Note that the last box may be packed with fewer items than the other boxes.
"""

import math

def main():
  items = int(input('Enter the number of total items required to pack: '))
  items_per_box = int(input('Enter the number items that fit in the box: '))

  boxes = math.ceil(items / items_per_box)

  print(f'For {items} items, packing {items_per_box} items in each box, you will need {boxes} boxes.')


main()

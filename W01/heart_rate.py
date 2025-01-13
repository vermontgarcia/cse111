"""
Author: Vermont Garcia
Program: heart_rate
Purpose: Write a Python program that asks for a person’s age and computes and outputs the slowest and fastest rates necessary to strengthen his heart.

When you physically exercise to strengthen your heart, you
should maintain your heart rate within a range for at least 20
minutes. To find that range, subtract your age from 220. This
difference is your maximum heart rate per minute. Your heart
simply will not beat faster than this maximum (220 - age).
When exercising to strengthen your heart, you should keep your
heart rate between 65% and 85% of your heart’s maximum rate.
"""

def main():
  age = int(input('Please enter your age: '))

  max_rate = 220 - age

  print(f'Max rate: {max_rate}')

  low_rate = max_rate * 0.65
  hight_rate = max_rate * 0.85

  print(f"When exercising to strengthen your heart, you should keep your heart rate between {low_rate: .0f} and {hight_rate: .0f} of your heart’s maximum rate.")

main()
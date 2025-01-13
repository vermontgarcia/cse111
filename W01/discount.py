"""
Author: Vermont Garcia
Program: discount
Purpose: Wwrite a Python program that gets a customer’s subtotal as input and gets the current day of the week from your computer’s operating system.

Core Requirements:

  - Your program asks the user for the subtotal but does not ask the user for the day of the week. Your program gets the day of the week from your 
    computer’s operating system.
  - Your program correctly computes and prints the discount amount if applicable.
  - Your program correctly computes and prints the sales tax amount and the total amount due.

Stretch Challenges:

  - Add code to your program that the computer will execute if today is Tuesday or Wednesday and the customer is not purchasing
    enough to receive the discount. This added code should compute and print the difference between $50 and the subtotal
    which is the additional amount the customer would need to purchase in order to receive the discount.
  - Near the beginning of your program replace the code that asks the user for the subtotal with a loop that
    repeatedly asks the user for a price and a quantity and computes the subtotal. This loop should
    repeat until the user enters "0" for the price.
"""


from datetime import datetime

def main():
  current_date = datetime.now()
  day_of_week = 2 #current_date.weekday()
  tax_percentage = 0.06

  while True:
    subtotal = float(input('Enter the subtotal amount: '))
    if subtotal == 0:
      break
    else:
      if subtotal >= 50 and (day_of_week == 1 or day_of_week == 2):
        discount = subtotal * 0.1
        subtotal -= discount
        sales_tax = subtotal * tax_percentage
        total = subtotal + sales_tax

        print(f'Discount: {discount: .2f}')
        print(f'Sales Tax: {sales_tax: .2f}')
        print(f'Total: {total: .2f}')
      else:
        if day_of_week == 1 or day_of_week == 2:
          amount_to_discount = 50 - subtotal
          print(f'Amount to get 10% discount: {amount_to_discount: .2f}')
        sales_tax = subtotal * tax_percentage
        total = subtotal + sales_tax

        print(f'Sales Tax: {sales_tax: .2f}')
        print(f'Total: {total: .2f}')

main()

'''
Author: Vermont Garcia
Program: receipt
Purpose: Write a Python program named receipt.py that prints to the terminal window a receipt for a customer’s grocery order.

Milestone Requirements:

  Program must contain at least these two functions:
    - main
    - read_dictionary
  
  And must read and process these two CSV files:

    - The products.csv file is a catalog of all the products that the grocery store sells.
    - The request.csv file contains the items ordered by a customer.

Final Requirements:

  During this prove assignment, you will add code to finish printing a receipt and to handle
  any exceptions that might occur while your program is running. Specifically, your program must
  do the following:

    - Print the store name at the top of the receipt.
    - Print the list of ordered items.
    - Sum and print the number of ordered items.
    - Sum and print the subtotal due.
    - Compute and print the sales tax amount. Use 6% as the sales tax rate.
    - Compute and print the total amount due.
    - Print a thank you message.
    - Get the current date and time from your computer’s operating system and print the current date and time.
    - Include a try block and except blocks to handle FileNotFoundError, PermissionError, and KeyError.

Stretching and Exceeding Requirements:

  - Program print a reminder of how many days until the New Years Sale begins (Jan 1) at the bottom of the receipt.
  - Program print a "return items by" date that is 9:00 PM 30 days in the future at the bottom of the receipt.
'''

import csv
from datetime import datetime, timedelta

def main():
  products_dic = read_dictionary('products.csv', 0)
  if products_dic:
    ordered_products_list = get_ordered_products_list(products_dic)
    print_receipt(ordered_products_list)


def print_receipt(products):
  store_name = 'The Best Groceries Store'
  print()
  print(store_name)
  today = datetime.today()
  retur_limit_day = today + timedelta(days=30)
  print(today.strftime("%a %b %d %H:%M:%S %Y"))
  print()
  sub_total = 0
  total_products = 0
  for product in products:
    name, quantity, price = product
    sub_total += price * quantity
    total_products += quantity
    print(f'{name}: {quantity} @ {price}')
  print()
  print(f'Subtotal: $ {sub_total :.2f}')
  print(f'Sales Tax: $ {sub_total * 0.06 :.2f}')
  print(f'Total: $ {sub_total * 0.06 + sub_total :.2f}')
  print()
  print(f'Number of Items: {total_products}')
  print()
  print(f'Thank you for shopping at {store_name}')
  print()
  print(f'Return items by: {retur_limit_day.strftime("%a %b %d 9:00 PM %Y")}')
  print()
  days_to_new_year_sale = get_days_to_jan_first() 
  print(f'{days_to_new_year_sale} Days until our New Years Sale (Jan 1st)')
  print()


def get_days_to_jan_first():
  '''
    Funtion that calculates the days until January First next year
  
    Parameters
        None
    Return: the numer of days until January First next year
  '''
  today = datetime.today().date()
  next_jan_first = datetime(today.year + 1, 1, 1).date()
  days_until_jan_first = (next_jan_first - today).days
  return days_until_jan_first
 
def read_dictionary(filename, key_column_index):
  '''
    Read the contents of a CSV file into a compound
    dictionary and return the dictionary.
    
    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
          to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
  '''
  try:
    with open(filename, 'rt') as csv_file:
      reader = csv.reader(csv_file)
      next(reader)
      products_dic = {}
      for line in reader:
        product_id = line[key_column_index]
        products_dic[product_id] = line
      return products_dic
  except FileNotFoundError as not_found_error:
    print('Error: Missing File')
    print(not_found_error)
  except PermissionError as perm_err:
    print('Error: User doesn\'t have permission to read files')
    print(perm_err)

def get_ordered_products_list(products_dic):
  '''
    Read the contents of an order CSV file and creates a list
    with customer request
  
    Parameters
      products_dic: The dictionary of Products.
    Return: A compound List that contains
      the customer order.
  '''
  try:
    products_list = []
    filename = 'request.csv' 
    with open(filename) as csv_file:
      reader = csv.reader(csv_file)
      next(reader)
      for line in reader:
        product_id, quantity = line
        products_list.append([products_dic[product_id][1].title(), int(quantity), float(products_dic[product_id][2])])
    return products_list
  except FileNotFoundError as not_found_error:
    print('Error: Missing File')
    print(not_found_error)
  except KeyError as key_error:
    print(f'Error: Unknown product ID in the {filename} file, ID: {key_error}')
  except PermissionError as perm_err:
    print('Error: User doesn\'t have permission to read files')
    print(perm_err)

if __name__ == '__main__':
  main()

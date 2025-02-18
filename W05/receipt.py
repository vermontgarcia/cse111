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
'''

import csv

def main():
  print('All Products')
  print()
  products_dic = read_dictionary('products.csv', 0)
  print(products_dic)
  print()
  print('Requested Items:')
  print()

  with open('request.csv') as csv_file:
    reader = csv.reader(csv_file)
    next(reader)
    for line in reader:
      product_id, quantity = line
      print(f'{products_dic[product_id][1]}: {quantity} @ {products_dic[product_id][2]}')

  print()

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
  with open(filename, 'rt') as csv_file:
    reader = csv.reader(csv_file)
    next(reader)
    products_dic = {}
    for line in reader:
      product_id = line[key_column_index]
      products_dic[product_id] = line
    return products_dic

if __name__ == '__main__':
  main()

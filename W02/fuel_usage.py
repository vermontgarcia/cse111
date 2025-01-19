"""
Author: Vermont Garcia
Program: fuel_usage
Purpose: Write a Python program that asks for three parameters (starting odometer in miles, endinmg odometer in miles and amount of fuel in gallons)
  then calculate mpg and lp100k.
"""


def main():
  start_value = int(input('Enter starting odometer value(miles): '))
  end_value = int(input('Enter ending odometer value(miles): '))
  fuel = float(input('Enter amout of fuel used (gallons): '))

  efficiency = mpg(start_value, end_value, fuel)

  print(f'{efficiency:.1f} miles per gallon')
  print(f'{mpg_to_lp100km(efficiency):.2f} liters per 100 kilometers')



def mpg(start, end, gallons):
  '''
    Function that computes the MPG of a vehicle
    Parameters:
      start: starting odometer in miles
      end: ending odometer in miles
      gallons: fuel amount in US gallons
    Return:
      Fuel efficiency in MPG
  '''
  return (end - start)/gallons

def mpg_to_lp100km(mpg):
  '''
    Function that converts MPG to litters per 100km
    Parameters:
      mpg: Value of MPG
    Return:
      Fuel efficiency converted in liters per 100km
  '''
  return 235.215/mpg

main()
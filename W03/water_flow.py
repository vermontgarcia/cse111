'''
Author: Vermont Garcia
Program: water_flow
Purpose: Write a Python program that could help an engineer design a water distribution system.

Problem Statement

  - Getting clean water to all buildings in a city is a large and expensive task. Many cities will build an elevated water tank,
    and install a pump that pushes water up to the tank where the water is stored. In the city, when a thirsty person opens a
    water faucet, water runs from the tank through pipes to the faucet. Earth’s gravity pulling on the water in the elevated
    tank pressurizes the water and causes it to spray from the faucet.

    Before a city builds a water distribution system, an engineer must design the system and ensure water will flow to all
    buildings in the city. An engineer must choose the tower height, pipe type, pipe diameter, and pipe path. Engineers use
    software to help them make these choices and design a working water distribtuion system.

Milestone Requirements:

  - During this prove milestone, you will write three program functions and three test functions as described in the Steps section below.

    - water_flow.py
      - water_column_height
      - test_pressure_gain_from_water_height
      - pressure_loss_from_pipe 
    - test_water_flow.py
      - test_water_column_height
      - test_test_pressure_gain_from_water_height
      - test_pressure_loss_from_pipe

'''

WATER_DENSITY = 998.2
EARTH_ACCELERATION_OF_GRAVITY =	9.80665
WATER_DYNAMIC_VISCOSITY =	0.0010016

def water_column_height(tower_height, tank_height):
  return tower_height + 3 * tank_height / 4

def pressure_gain_from_water_height(height):
  return WATER_DENSITY * EARTH_ACCELERATION_OF_GRAVITY * height / 1000

def pressure_loss_from_pipe(pipe_diameter, pipe_length, friction_factor, fluid_velocity):
  return (-1 * friction_factor * pipe_length * WATER_DENSITY * fluid_velocity ** 2) / (2000 * pipe_diameter)


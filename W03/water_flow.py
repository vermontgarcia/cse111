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

Core Requirements:

  - 
    - water_flow.py
      - pressure_loss_from_fittings
      - reynolds_number
      - pressure_loss_from_pipe_reduction 
    - test_water_flow.py
      - test_pressure_loss_from_fittings
      - test_reynolds_number
      - test_pressure_loss_from_pipe_reduction

Exceeding the Requirements:

  - Add earth's acceleration gravity constant
  - Add water density constant
  - Add water dynamic viscosity constant
'''

WATER_DENSITY = 998.2000000
EARTH_ACCELERATION_OF_GRAVITY =	9.8066500
WATER_DYNAMIC_VISCOSITY =	0.0010016

def water_column_height(tower_height, tank_height):
  """
    Calculates water column height.
    Parameters
        tower_height: number
        tank_height: number
    Return: number calculated for water column height
  """
  return tower_height + 3 * tank_height / 4

def pressure_gain_from_water_height(height):
  """
    Calculates pressure gain from water height.
    Parameters
        height: number
    Return: number calculated for pressure gain from water height
  """
  return WATER_DENSITY * EARTH_ACCELERATION_OF_GRAVITY * height / 1000

def pressure_loss_from_pipe(pipe_diameter, pipe_length, friction_factor, fluid_velocity):
  """
    Calculates pressure loss from pipe.
    Parameters
        pipe_diameter: numnber 
        pipe_length: number
        friction_factor: number
        fluid_velocity: number
    Return: number calculated for pressure loss from pipe
  """
  return (-friction_factor * pipe_length * WATER_DENSITY * fluid_velocity ** 2) / (2000 * pipe_diameter)

def pressure_loss_from_fittings(fluid_velocity, quantity_fittings):
  """
    Calculates pressure loss from fittings.
    Parameters
        fluid_velocity: number
        quantity_fittings: number
    Return: number calculated for pressure loss from fittings
  """
  return round((-0.04 * WATER_DENSITY * fluid_velocity ** 2 * quantity_fittings) / 2000, 3)

def reynolds_number(hydraulic_diameter, fluid_velocity):
  """
    Calculates reynolds number.
    Parameters
        hydraulic_diameter: number
        fluid_velocity: number
    Return: number calculated for reynolds number
  """
  return WATER_DENSITY * hydraulic_diameter * fluid_velocity / WATER_DYNAMIC_VISCOSITY

def pressure_loss_from_pipe_reduction(larger_diameter, fluid_velocity, reynolds_number, smaller_diameter):
  """
    Calculates pressure loss from pipe reduction.
    Parameters
        larger_diameter: numnber 
        fluid_velocity: number
        reynolds_number: number
        smaller_diameter: number
    Return: number calculated for pressure loss from pipe reduction
  """
  k = (0.1 + 50/reynolds_number) * ((larger_diameter/smaller_diameter)**4 -1)
  return (-k * WATER_DENSITY * fluid_velocity ** 2) / 2000

PVC_SCHED80_INNER_DIAMETER = 0.28687 # (meters)  11.294 inches
PVC_SCHED80_FRICTION_FACTOR = 0.013  # (unitless)
SUPPLY_VELOCITY = 1.65               # (meters / second)
HDPE_SDR11_INNER_DIAMETER = 0.048692 # (meters)  1.917 inches
HDPE_SDR11_FRICTION_FACTOR = 0.018   # (unitless)
HOUSEHOLD_VELOCITY = 1.75            # (meters / second)

def main():
    tower_height = float(input("Height of water tower (meters): "))
    tank_height = float(input("Height of water tank walls (meters): "))
    length1 = float(input("Length of supply pipe from tank to lot (meters): "))
    quantity_angles = int(input("Number of 90° angles in supply pipe: "))
    length2 = float(input("Length of pipe from supply to house (meters): "))

    water_height = water_column_height(tower_height, tank_height)
    pressure = pressure_gain_from_water_height(water_height)
    diameter = PVC_SCHED80_INNER_DIAMETER
    friction = PVC_SCHED80_FRICTION_FACTOR
    velocity = SUPPLY_VELOCITY
    reynolds = reynolds_number(diameter, velocity)
    loss = pressure_loss_from_pipe(diameter, length1, friction, velocity)
    pressure += loss
    loss = pressure_loss_from_fittings(velocity, quantity_angles)
    pressure += loss
    loss = pressure_loss_from_pipe_reduction(diameter, velocity, reynolds, HDPE_SDR11_INNER_DIAMETER)
    pressure += loss
    diameter = HDPE_SDR11_INNER_DIAMETER
    friction = HDPE_SDR11_FRICTION_FACTOR
    velocity = HOUSEHOLD_VELOCITY
    loss = pressure_loss_from_pipe(diameter, length2, friction, velocity)
    pressure += loss

    print(f"Pressure at house: {pressure:.1f} kilopascals")

if __name__ == "__main__":
    main()

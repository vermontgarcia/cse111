'''
Author: Vermont Garcia
Program: chemistry
Purpose: Write a Python program that calculates the molar mass of a molecule and the number of moles in a sample.

Problem Statement

  - In chemistry, a mole is a very large, fixed quantity, specifically 602,214,076,000,000,000,000,000 (usually written
    as 6.02214076 × 1023). The molar mass of a substance is the mass in grams of one mole of the substance (grams / mole).
    A molar mass calculator is a program that computes the molar mass of a substance and the number of moles of a sample
    of that substance. To use a molar mass calculator, a chemist enters two inputs:

      - The formula for a molecule, such as H2O (water) or C6H12O6 (glucose)
      - The mass in grams of a sample of the substance, such as 3.71

    The calculator computes the molar mass of the molecule by doing the following for each element in the formula:

      - Sum the number of atoms of each element in the formula
      - Find the atomic mass of each element
      - Multiply the number of atoms by their atomic mass
      - Add the product into the molar mass of the molecule

    Then the calculator computes the number of moles in the sample with this formula:

      number_of_moles = sample_mass / molar_mass

    Finally, the calculator prints two results for the chemist to see:

      - the molar mass
      - the number of moles

Milestone Requirements:

  - During this prove milestone and the next prove assignment, you will write and test a molar mass calculator named chemistry.py.
    During this milestone, you will complete part of the calculator by writing:
      - A function named make_periodic_table that must create and return a compound list that contains data for all 94 naturally occuring elements.
      - A the main function.

Core Requirements:

  - During this assignment, you will write and test the remaining parts of the molar mass calculator that you started writing in the previous
    lesson’s prove milestone. When you are finished with this prove assignment, your chemistry.py program must contain at least three
    functions named as follows:

      - main
      - make_periodic_table
      - compute_molar_mass

Exceeding the Requirements:

  - Add get_formula_name function
  - Add known_molecules_dict
  - Handle exception for incorrect molecule formula entered
  - Handle exception when no number input on sample mass in grams
'''

from formula import parse_formula

# Indexes for inner lists in the periodic table
# NAME_INDEX = 0 # this is not being used
ATOMIC_MASS_INDEX = 1
# Indexes for inner lists in a symbol_quantity_list
# SYMBOL_INDEX = 0 # this is not being used
# QUANTITY_INDEX = 1 # this is not being used

# Dictionary of known molecules formula names
known_molecules_dict = {
  "Al2O3": "aluminum oxide",
  "CH3OH": "methanol",
  "C2H6O": "ethanol",
  "C2H5OH": "ethanol",
  "C3H8O": "isopropyl alcohol",
  "C3H8": "propane",
  "C4H10": "butane",
  "C6H6": "benzene",
  "C6H14": "hexane",
  "C8H18": "octane",
  "CH3(CH2)6CH3": "octane",
  "C13H18O2": "ibuprofen",
  "C13H16N2O2": "melatonin",
  "Fe2O3": "iron oxide",
  "FeS2": "iron pyrite",
  "H2O": "water"
}

def main():
  periodic_table = make_periodic_table()
  
  chemical_formula = ''
  while True:
    chemical_formula = input('Enter the Chemical Formula: ')
    # Try parsing formula input from user. Retry when user doesn't provide a valid formula format
    try:
      parsed_formula = parse_formula(chemical_formula, periodic_table)
      print()
      break
    except:
      print('Please enter a valid compund formula')
  
  # Finds formula name from known formulas dictionary
  formula_name = get_formula_name(chemical_formula, known_molecules_dict)
  print(formula_name.title())
  print()

  sample_mass_gr = 0
  while True:
    # Try parsing user input into float number. Retry if no number entered
    try:
      sample_mass_gr = float(input('Enter the mass of the Chemical sammple in grams: '))
      print()
      break
    except:
      print('Please enter a valid number in grams')

  molar_mass = round(compute_molar_mass(parsed_formula, periodic_table), 5)
  print(f'{molar_mass} grams/mole')

  number_of_moles = round(compute_number_of_moles(molar_mass, sample_mass_gr), 5)
  print(f'{number_of_moles} moles')

  print()



def make_periodic_table():
  """
  Create a periodic elements table dictionary.
  Parameters
      none
  Return: a dictionary of periodic table
  """
  periodic_table_dict = {
    # symbol: [name, atomic_mass]
    "Ac": ["Actinium", 227],
    "Ag": ["Silver", 107.8682],
    "Al": ["Aluminum", 26.9815386],
    "Ar": ["Argon", 39.948],
    "As": ["Arsenic", 74.9216],
    "At": ["Astatine", 210],
    "Au": ["Gold", 196.966569],
    "B": ["Boron", 10.811],
    "Ba": ["Barium", 137.327],
    "Be": ["Beryllium", 9.012182],
    "Bi": ["Bismuth", 208.9804],
    "Br": ["Bromine", 79.904],
    "C": ["Carbon", 12.0107],
    "Ca": ["Calcium", 40.078],
    "Cd": ["Cadmium", 112.411],
    "Ce": ["Cerium", 140.116],
    "Cl": ["Chlorine", 35.453],
    "Co": ["Cobalt", 58.933195],
    "Cr": ["Chromium", 51.9961],
    "Cs": ["Cesium", 132.9054519],
    "Cu": ["Copper", 63.546],
    "Dy": ["Dysprosium", 162.5],
    "Er": ["Erbium", 167.259],
    "Eu": ["Europium", 151.964],
    "F": ["Fluorine", 18.9984032],
    "Fe": ["Iron", 55.845],
    "Fr": ["Francium", 223],
    "Ga": ["Gallium", 69.723],
    "Gd": ["Gadolinium", 157.25],
    "Ge": ["Germanium", 72.64],
    "H": ["Hydrogen", 1.00794],
    "He": ["Helium", 4.002602],
    "Hf": ["Hafnium", 178.49],
    "Hg": ["Mercury", 200.59],
    "Ho": ["Holmium", 164.93032],
    "I": ["Iodine", 126.90447],
    "In": ["Indium", 114.818],
    "Ir": ["Iridium", 192.217],
    "K": ["Potassium", 39.0983],
    "Kr": ["Krypton", 83.798],
    "La": ["Lanthanum", 138.90547],
    "Li": ["Lithium", 6.941],
    "Lu": ["Lutetium", 174.9668],
    "Mg": ["Magnesium", 24.305],
    "Mn": ["Manganese", 54.938045],
    "Mo": ["Molybdenum", 95.96],
    "N": ["Nitrogen", 14.0067],
    "Na": ["Sodium", 22.98976928],
    "Nb": ["Niobium", 92.90638],
    "Nd": ["Neodymium", 144.242],
    "Ne": ["Neon", 20.1797],
    "Ni": ["Nickel", 58.6934],
    "Np": ["Neptunium", 237],
    "O": ["Oxygen", 15.9994],
    "Os": ["Osmium", 190.23],
    "P": ["Phosphorus", 30.973762],
    "Pa": ["Protactinium", 231.03588],
    "Pb": ["Lead", 207.2],
    "Pd": ["Palladium", 106.42],
    "Pm": ["Promethium", 145],
    "Po": ["Polonium", 209],
    "Pr": ["Praseodymium", 140.90765],
    "Pt": ["Platinum", 195.084],
    "Pu": ["Plutonium", 244],
    "Ra": ["Radium", 226],
    "Rb": ["Rubidium", 85.4678],
    "Re": ["Rhenium", 186.207],
    "Rh": ["Rhodium", 102.9055],
    "Rn": ["Radon", 222],
    "Ru": ["Ruthenium", 101.07],
    "S": ["Sulfur", 32.065],
    "Sb": ["Antimony", 121.76],
    "Sc": ["Scandium", 44.955912],
    "Se": ["Selenium", 78.96],
    "Si": ["Silicon", 28.0855],
    "Sm": ["Samarium", 150.36],
    "Sn": ["Tin", 118.71],
    "Sr": ["Strontium", 87.62],
    "Ta": ["Tantalum", 180.94788],
    "Tb": ["Terbium", 158.92535],
    "Tc": ["Technetium", 98],
    "Te": ["Tellurium", 127.6],
    "Th": ["Thorium", 232.03806],
    "Ti": ["Titanium", 47.867],
    "Tl": ["Thallium", 204.3833],
    "Tm": ["Thulium", 168.93421],
    "U": ["Uranium", 238.02891],
    "V": ["Vanadium", 50.9415],
    "W": ["Tungsten", 183.84],
    "Xe": ["Xenon", 131.293],
    "Y": ["Yttrium", 88.90585],
    "Yb": ["Ytterbium", 173.054],
    "Zn": ["Zinc", 65.38],
    "Zr": ["Zirconium", 91.224],
  }
  return periodic_table_dict

def compute_molar_mass(symbol_quantity_list, periodic_table_dict):
    """Compute and return the total molar mass of all the
    elements listed in symbol_quantity_list.
    Parameters
        symbol_quantity_list is a compound list returned
            from the parse_formula function. Each small
            list in symbol_quantity_list has this form:
            ["symbol", quantity].
        periodic_table_dict is the compound dictionary
            returned from make_periodic_table.
    Return: the total molar mass of all the elements in
        symbol_quantity_list.
    For example, if symbol_quantity_list is [["H", 2], ["O", 1]],
    this function will calculate and return
    atomic_mass("H") * 2 + atomic_mass("O") * 1
    1.00794 * 2 + 15.9994 * 1
    18.01528
    """
    # Do the following for each inner list in the
    # compound symbol_quantity_list:
        # Separate the inner list into symbol and quantity.
        # Get the atomic mass for the symbol from the dictionary.
        # Multiply the atomic mass by the quantity.
        # Add the product into the total molar mass.
    # Return the total molar mass.

    total_molar_mass = 0
    for element in symbol_quantity_list:
      symbol, quantity = element
      atomic_mass = periodic_table_dict[symbol][ATOMIC_MASS_INDEX]
      total_molar_mass += quantity * atomic_mass
    return total_molar_mass

def compute_number_of_moles(molar_mass, sample_mass):
  """
  Compute number of moles in a molecule.
  Parameters
      molar_mass: number representing the molar mass of the molecule
      sample_mass: number that represents the sample mass in grams
  Return: the number of moles
  """
  return sample_mass / molar_mass

def get_formula_name(formula, known_molecules_dict):
    """Try to find formula in the known_molecules_dict.
    If formula is in the known_molecules_dict, return
    the name of the chemical formula; otherwise return
    "unknown compound".
    Parameters
        formula is a string that contains a chemical formula
        known_molecules_dict is a dictionary that contains
            known chemical formulas and their names
    Return: the name of a chemical formula
    """
    formula_name = ''
    try:
      formula_name = known_molecules_dict[formula]
    except:
      formula_name = 'unknown compound'
    return formula_name

if __name__ == '__main__':
  main()
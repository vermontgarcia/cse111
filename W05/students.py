import csv

def read_dictionary(filename, key_column_index):
  """Read the contents of a CSV file into a compound
  dictionary and return the dictionary.
  Parameters
      filename: the name of the CSV file to read.
      key_column_index: the index of the column
          to use as the keys in the dictionary.
  Return: a compound dictionary that contains
      the contents of the CSV file.
  """

  with open(filename, "rt") as csv_file:
      reader = csv.reader(csv_file)
      next(reader)
      students_dic = {}
      for line in reader:
          i_number, name = line
          # i_number = line[0]
          # name = line[1]
          students_dic[i_number] = name
          # print(line)
      return students_dic

def main():
    print('Hello Reading a File')

    i_number = input('Type your I-Number: ')

    students = read_dictionary('students.csv', 1)

    try:
        print(students[i_number])
    except:
        print('No such student')

if __name__ == '__main__':
    main()

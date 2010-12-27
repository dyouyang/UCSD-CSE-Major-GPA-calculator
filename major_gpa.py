#!/usr/bin/python -tt
'''Calculates CSE major gpa given Tritonlink academic history html file as input'''


import sys
import re

def convert_points(classes):
  '''converts units and gap points from string to float and returns new list'''
  fixed = []
  for (dep, num, name, units, points) in classes:
    if float(points) != 0.0 and dep == 'CSE':
      fixed.append( (dep, num, name, float(units), float(points) ) )

  return fixed
def get_classes(filename):
  '''parses academic history html file and returns list of classes'''
  try:
    f = open(filename, 'r')
    text = f.read()
  except:
    sys.stderr.write('could not open: ' + filename + '\n')
    sys.exit(1)

  
  classes = re.findall(r'<tr><td><.+>(\w+)<.+>(\d\d\d+\w?\w?)<.+>(\w[^<]+)<.+>(\d\.\d\d)<.+>(\d+\.\d\d)<.+></td></tr>', text)
  return classes

def main():
  args = sys.argv[1:]
  if len(args) != 1:
    print 'usage: ./major_gpa.py [tritonlink html file]'
    sys.exit(1)

  filename = args[0]

  classes = get_classes(filename)
  classes = convert_points(classes)
  
  my_points = 0
  tot_units = 0
  for (dep, num, name, units, points) in classes:
    print 'Adding class', dep+num, ':', name, '(', str(units), 'units', ',', str(points), 'points', ')'
    my_points += points
    tot_units += units
  
  extra_points = float(raw_input('Add any extra points(0 to skip) :'))
  extra_units = float(raw_input('Add any extra units (0 to skip):'))
  
  my_points += extra_points
  tot_units += extra_units

  print 'my points :', my_points
  print 'total units attempted :', tot_units
  print 'my major gpa :', my_points/tot_units


if __name__ == '__main__':
  main()

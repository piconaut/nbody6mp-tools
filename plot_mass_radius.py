#!/usr/bin/python

import matplotlib.pyplot as plt
from math import ceil
from sys import argv

def plot_mass_radii(input_file,output_type):
  total = []
  pop1 = []
  pop2 = []

  with open(input_file,'r') as f:
    for line in f:
      line_cleaned = line.split(' ')
      for i in range(len(line_cleaned)):
        if '\n' in line_cleaned[i]:
          line_cleaned[i] = line_cleaned[i].strip()
        line_cleaned[i] = float(line_cleaned[i])
      
      if len(line_cleaned) == 1:
        mass_fraction = line_cleaned[0]
      else:
        total.append(line_cleaned[0])
        pop1.append(line_cleaned[1])
        pop2.append(line_cleaned[2])

  plt.plot(total,label='Total')
  plt.plot(pop1,label='Population 1')
  plt.plot(pop2, label='Population 2')
  plt.xlabel('*10 time steps')
  plt.ylabel('R_' + str(mass_fraction))
  plt.axis([0,ceil(len(total)/100.)*100,0,max([max(total),max(pop1),max(pop2)])+0.25])
  plt.legend()
  plt.minorticks_on()
  plt.grid(True,which='major')
  plt.grid(True,which='minor',linewidth='0.125')
#  plt.show()
  out_file = input_file.rsplit('.',1)[0]

  plt.savefig(out_file + '.' + output_type)


plot_mass_radii(argv[1],argv[2])

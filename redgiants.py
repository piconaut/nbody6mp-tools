#!/usr/bin/python

from math import sqrt
from sys import stdout,argv

nbody_Myr = float(argv[1])
target_time = float(argv[2])
out_file = argv[3]

with open('../fort.83','r') as f:
  radii = []
  pops = []
  time = 0.0
  for line in f:
    line_cleaned = line.split(' ')
    for i in reversed(range(len(line_cleaned))):
      if line_cleaned[i] == '':
        del line_cleaned[i]
      elif '\n' in line_cleaned[i]:
        line_cleaned[i] = line_cleaned[i].strip()

    if len(line_cleaned) == 14:

      if line_cleaned[0] == '-1000':
        if time >= target_time:
          with open(out_file,'w') as o:
            for i in range(len(radii)):
              o.write(radii[i] + ' ' + pops[i] + '\n')
          print('')
          break
          break
          break
          break
        time += 10.*nbody_Myr
        stdout.write('\r' + str(time) + ' Myr')
        stdout.flush()

      elif time >= target_time:
        star_type = line_cleaned[1]
          # 3 = red giant
        if star_type == '3':
          position = line_cleaned[5:8]
          population = line_cleaned[13]

          for i in range(len(position)):
            position[i] = float(position[i])

          radius = sqrt(position[0]**2 + position[1]**2 + position[2]**2)
          radii.append(str(radius))
          pops.append(str(population))

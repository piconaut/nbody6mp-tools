#!/usr/bin/python

# Only works for KZ(12) >= 3

from math import sqrt
from sys import stdout, argv

def mass_radii(input_file,fraction,out_name):

  fraction = float(fraction)

  mass_radii = []
  mass_radii_pop1 = []
  mass_radii_pop2 = []

  print('Counting timesteps')
  n_timesteps = 0.
  with open(input_file) as f:
    for line in f:
      if '-1000' in line:
        n_timesteps += 1.

  print(str(int(n_timesteps)) + ' timesteps')

  with open(input_file) as f:

    time_radii = []
    time_masses = []
    time_radii_pop1 = []
    time_masses_pop1 = []
    time_radii_pop2 = []
    time_masses_pop2 = []

    for line in f:
      line_cleaned = line.split(' ')
      for i in reversed(range(len(line_cleaned))):
        if line_cleaned[i] == '':
          del line_cleaned[i]
        elif '\n' in line_cleaned[i]:
          line_cleaned[i] = line_cleaned[i].strip()


      if len(line_cleaned) == 14:

        if line_cleaned[0] == '-1000':
          time_radii, time_masses = zip(*sorted(zip(time_radii, time_masses)))
          total_mass = sum(time_masses)

          current_mass = 0.
          i = 0
          while current_mass < total_mass*fraction:
            current_mass += time_masses[i]
            i += 1
          
          mass_radii.append(time_radii[i])
   #       print('Total R_half: ' + str(time_radii[i]))  

          time_radii = []
          time_masses = []

        
          time_radii_pop1, time_masses_pop1 = zip(*sorted(zip(time_radii_pop1, time_masses_pop1)))
          total_mass_pop1 = sum(time_masses_pop1)

          current_mass_pop1 = 0.
          i=0
          while current_mass_pop1 < total_mass_pop1*fraction:
            current_mass_pop1 += time_masses_pop1[i]
            i += 1

          mass_radii_pop1.append(time_radii_pop1[i])
   #       print('Pop1  R_half: ' + str(time_radii_pop1[i]))

          time_radii_pop1 = []
          time_masses_pop1 = []


          time_radii_pop2, time_masses_pop2 = zip(*sorted(zip(time_radii_pop2, time_masses_pop2)))
          total_mass_pop2 = sum(time_masses_pop2)

          current_mass_pop2 = 0.
          i=0
          while current_mass_pop2 < total_mass_pop2*fraction:
            current_mass_pop2 += time_masses_pop2[i]
            i += 1

          mass_radii_pop2.append(time_radii_pop2[i])
   #       print('Pop2  R_half: ' + str(time_radii_pop2[i]))
  
          time_radii_pop2 = []
          time_masses_pop2 = []
  
          stdout.write('\rProgress: ' + str('{:5.2f}'.format(100*len(mass_radii)/n_timesteps))+'%')
          stdout.flush()
  
        else:
  
          # line_cleaned[2]    mass
          # line_cleaned[5:8]  position
          # line_cleaned[9:12] velocity
  
          position = line_cleaned[5:8]
  
          for i in range(len(position)):
            position[i] = float(position[i])
  
          mass = float(line_cleaned[2])
          radius = sqrt(position[0]**2 + position[1]**2 + position[2]**2)
     
  
          time_masses.append(mass)
          time_radii.append(radius)
  
          if line_cleaned[13] == '1':
            time_masses_pop1.append(mass)
            time_radii_pop1.append(radius)
          elif line_cleaned[13] == '2':
            time_masses_pop2.append(mass)
            time_radii_pop2.append(radius)

  print('')
  
  with open(out_name,'w') as f:
    f.write(str(fraction) + '\n')
    for i in range(len(mass_radii)):
      out_str = str(mass_radii[i]) + ' ' + str(mass_radii_pop1[i]) + ' ' + str(mass_radii_pop2[i]) + '\n'
      f.write(out_str)
  

mass_radii(argv[1],argv[2],argv[3])





def total_mass(input_file,out_name):

  total_mass = []
  total_mass_pop1 = []
  total_mass_pop2 = []

  with open(input_file) as f:

    time_masses = []
    time_masses_pop1 = []
    time_masses_pop2 = []

    has_pop2 = False

    for line in f:
      line_cleaned = line.split(' ')
      for i in reversed(range(len(line_cleaned))):
        if line_cleaned[i] == '': 
          del line_cleaned[i]
        elif '\n' in line_cleaned[i]:
          line_cleaned[i] = line_cleaned[i].strip()


      if len(line_cleaned) == 14: 

        if line_cleaned[0] == '-1000':
          total_mass.append(sum(time_masses))
          total_mass_pop1.append(sum(time_masses_pop1))
 
          if has_pop2:
            total_mass_pop2.append(sum(time_masses_pop2))
            time_masses_pop2 = []

          time_masses = []
          time_masses_pop1 = []

        else:
          time_masses.append(mass)
          if line_cleaned[13] == '1':
            time_masses_pop1.append(mass)
          elif line_cleaned[13] == '2':
            time_masses_pop2.append(mass)
            has_pop2 = True

  with open(out_name,'w') as f:
    for i in range(len(mass_radii)):
      if has_pop2:
        out_str = str(total_mass[i]) + ' ' + str(total_mass_pop1[i]) + ' ' + str(total_mass_pop2[i]) + '\n'
      else:
        out_str = str(total_mass[i]) + '\n'
      f.write(out_str)















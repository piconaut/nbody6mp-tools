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
          mass = float(line_cleaned[2])

          time_masses.append(mass)
          if line_cleaned[13] == '1':
            time_masses_pop1.append(mass)
          elif line_cleaned[13] == '2':
            time_masses_pop2.append(mass)
            has_pop2 = True

  with open(out_name,'w') as f:
    for i in range(len(total_mass)):
      if has_pop2:
        out_str = str(total_mass[i]) + ' ' + str(total_mass_pop1[i]) + ' ' + str(total_mass_pop2[i]) + '\n'
      else:
        out_str = str(total_mass[i]) + '\n'
      f.write(out_str)

def plot_mass(input_file,output_type):
  import matplotlib.pyplot as plt 
  from math import ceil
  from sys import argv

  total = []
  pop1 = []
  pop2 = []

  with open(input_file,'r') as f:
    for index,line in enumerate(f):
      line_cleaned = line.split(' ')
      for i in range(len(line_cleaned)):
        if '\n' in line_cleaned[i]:
          line_cleaned[i] = line_cleaned[i].strip()
        line_cleaned[i] = float(line_cleaned[i])

      if index == 0:
        nbody_Msun = line_cleaned[0]
        nbody_Myr = line_cleaned[1]*10
      else:
        total.append(line_cleaned[0])
        if len(line_cleaned) > 1:
          pop1.append(line_cleaned[1])
          pop2.append(line_cleaned[2])

  if len(pop2) > 1:
    has_pop2 = True
  else:
    has_pop2 = False

  time = []
  for i in range(len(total)):
    time.append(i*nbody_Myr)
    total[i] = total[i]*nbody_Msun
    if has_pop2:
      pop1[i] = pop1[i]*nbody_Msun
      pop2[i] = pop2[i]*nbody_Msun

  plt.plot(time,total,label='Total')
  if has_pop2:
    plt.plot(time,pop1,label='Population 1')
    plt.plot(time,pop2, label='Population 2')
  plt.xlabel('Time (Myr)')
  plt.ylabel('Mass (Msun)')
  if has_pop2:
    plt.axis([0,max(time),0,max([max(total),max(pop1),max(pop2)])+0.25])
  else:
    plt.axis([0,max(time),0,max(total)+0.25])
  plt.legend()
  plt.minorticks_on()
  plt.grid(True,which='major')
  plt.grid(True,which='minor',linewidth='0.125')
  out_file = input_file.rsplit('.',1)[0]

  plt.savefig(out_file + '.' + output_type)
  plt.close()











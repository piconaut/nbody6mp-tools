#!/usr/bin/python

import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
from math import sqrt
from sys import stdout,argv

try:
  nbody_Myr = float(argv[1])
  target_time = float(argv[2])
  target_time_2 = float(argv[3])
  out_file = argv[4]
except:
  print("Use: ")
  print("./redgiants.py [nbody_Myr] [target_time(Myr)] [target_time_2(Myr)] [out_filename]\n")

nbody_Myr = float(argv[1])
target_time = float(argv[2])
target_time_2 = float(argv[3])
out_file = argv[4]


target_times_2 = [1000.,2000.,3000.,4000.,5000.,6000.,7000.,8000.,9000.]


"""
# first, find labelled red giants at the target time
with open('../fort.83','r') as f:
  radii = []
  pops = []
  masses = []
  ids = []
  time = 0.0
  for index,line in enumerate(f):
    line_cleaned = line.split(' ')
    for i in reversed(range(len(line_cleaned))):
      if line_cleaned[i] == '':
        del line_cleaned[i]
      elif '\n' in line_cleaned[i]:
        line_cleaned[i] = line_cleaned[i].strip()

    if len(line_cleaned) == 14:

      if line_cleaned[0] == '-1000':
        if time >= target_time:
          print('Stop at line ' + str(index))
          with open(out_file,'w') as o:
            for i in range(len(radii)):
              o.write(radii[i] + ' ' + pops[i] + '\n')
          print('')
          print(min(masses))
          print(max(masses))
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
          masses.append(float(line_cleaned[2]))
          ids.append(line_cleaned[0])

          for i in range(len(position)):
            position[i] = float(position[i])

          radius = sqrt(position[0]**2 + position[1]**2 + position[2]**2)
          radii.append(str(radius))
          pops.append(str(population))

  f.close()
"""

ids = ['1402', '30595', '2864', '10842', '4780', '6992', '8162', '8297', '10595', '12336', '39565', '13213', '7010', '13656', '15812', '37420', '17419', '17420', '15474', '35474', '19111', '19870', '20029', '21402', '28297', '39870', '22864', '24780', '19630', '39630', '28662', '26992', '27010', '19565', '33656', '32892', '30842', '32336', '39111', '33213', '12892', '35812', '28162', '37419', '8662']
print ids


for target_time_2 in target_times_2:
  print('Working on ' + str(target_time_2))
  with open('../fort.83','r') as f:
    # plot hr diagram at first timestep, highlighting those red giants

    ms_lums = []
    ms_rads = []
    ms_tems = []
    hg_lums = []
    hg_rads = []
    hg_tems = [] 
    rg_lums = []
    rg_rads = []
    rg_tems = []
    che_lums = []
    che_rads = []
    che_tems = []
    agb_lums = []
    agb_rads = []
    agb_tems = []
    hems_lums = []
    hems_rads = []
    hems_tems = []
    hehg_lums = []
    hehg_rads = []
    hehg_tems = []
    hegb_lums = []
    hegb_rads = []
    hegb_tems = []
    wd_lums = []
    wd_rads = []
    wd_tems = []
    ns_lums = []
    ns_rads = []
    ns_tems = []
    bh_lums = []
    bh_rads = []
    bh_tems = []
    sn_lums = []
    sn_rads = []
    sn_tems = []

    saved_rg_lums = []
    saved_rg_rads = []
    saved_rg_tems = []

    radii = []
    pops = []
    masses = []
    time2 = 0.0

    for index,line in enumerate(f):
      line_cleaned = line.split(' ')
      for i in reversed(range(len(line_cleaned))):
        if line_cleaned[i] == '':
          del line_cleaned[i]
        elif '\n' in line_cleaned[i]:
          line_cleaned[i] = line_cleaned[i].strip()

      if len(line_cleaned) == 14:
  
        if line_cleaned[0] == '-1000':
          if time2 >= target_time_2:
            fig = plt.figure(figsize=(7.2,4.8))
            ax = plt.subplot(111)
            plt.plot(ms_tems,ms_lums,'bo',ms=1,label='Main sequence')
            plt.plot(hg_tems,hg_lums,'go',ms=1,label='Hertzsprung gap')
            plt.plot(che_tems,che_lums,'co',ms=1,label='Core helium burning')
            plt.plot(agb_tems,agb_lums,'yo',ms=1,label='AGB')
            plt.plot(hehg_tems,hehg_lums,'ko',ms=1,label='He HG')
            plt.plot(hegb_tems,hegb_lums,'bx',ms=1,label='He GB')
            plt.plot(wd_tems,wd_lums,c='0.5',marker='o',lw=0.0,ms=1,label='White dwarfs')
            plt.plot(ns_tems,ns_lums,'gx',ms=1,label='Neutron stars')
            plt.plot(rg_tems,rg_lums,'ro',ms=1,label='Red giants at '+str(int(time2))+'Myr')
            plt.plot(saved_rg_tems,saved_rg_lums,'mo',ms=1,label='Red giants at '+str(int(target_time))+'Myr')
            plt.axis([2,7,0,2])
            plt.gca().invert_xaxis()
            box = ax.get_position()
            ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])
            ax.legend(loc='center left', bbox_to_anchor=(1, 0.5),fontsize=8)
            plt.xlabel('$\log(T/T_\odot$)')
            plt.ylabel('$\log(L/L_\odot$)')
            plt.title(str(target_time_2))
            plt.savefig('hrdiag_' + str(int(time2)) + 'Myr.png')
            plt.close()
            break
            break
            break
            break
          time2 += 10.*nbody_Myr
          print(time2)
        elif time2 >= target_time_2:
          ident = line_cleaned[0]
          if ident in ids:
            saved_rg_lums.append(float(line_cleaned[2]))
            saved_rg_rads.append(float(line_cleaned[3]))
            saved_rg_tems.append(0.25*(float(line_cleaned[2]) - 2*float(line_cleaned[3])) + 3.7)
          elif line_cleaned[1] == '0' or line_cleaned[1] == '1':
            ms_lums.append(float(line_cleaned[2]))
            ms_rads.append(float(line_cleaned[3]))
            ms_tems.append(0.25*(float(line_cleaned[2]) - 2*float(line_cleaned[3])) + 3.7)
          elif line_cleaned[1] == '2':
            hg_lums.append(float(line_cleaned[2]))
            hg_rads.append(float(line_cleaned[3]))
            hg_tems.append(0.25*(float(line_cleaned[2]) - 2*float(line_cleaned[3])) + 3.7)
          elif line_cleaned[1] == '3':
            rg_lums.append(float(line_cleaned[2]))
            rg_rads.append(float(line_cleaned[3]))
            rg_tems.append(0.25*(float(line_cleaned[2]) - 2*float(line_cleaned[3])) + 3.7)
          elif line_cleaned[1] == '4':
            che_lums.append(float(line_cleaned[2]))
            che_rads.append(float(line_cleaned[3]))
            che_tems.append(0.25*(float(line_cleaned[2]) - 2*float(line_cleaned[3])) + 3.7)
          elif line_cleaned[1] == '5' or line_cleaned[1] == '6':
            agb_lums.append(float(line_cleaned[2]))
            agb_rads.append(float(line_cleaned[3]))
            agb_tems.append(0.25*(float(line_cleaned[2]) - 2*float(line_cleaned[3])) + 3.7)
          elif line_cleaned[1] == '7':
            hems_lums.append(float(line_cleaned[2]))
            hems_rads.append(float(line_cleaned[3]))
            hems_tems.append(0.25*(float(line_cleaned[2]) - 2*float(line_cleaned[3])) + 3.7)
          elif line_cleaned[1] == '8':
            hehg_lums.append(float(line_cleaned[2]))
            hehg_rads.append(float(line_cleaned[3]))
            hehg_tems.append(0.25*(float(line_cleaned[2]) - 2*float(line_cleaned[3])) + 3.7)
          elif line_cleaned[1] == '9':
            hegb_lums.append(float(line_cleaned[2]))
            hegb_rads.append(float(line_cleaned[3]))
            hegb_tems.append(0.25*(float(line_cleaned[2]) - 2*float(line_cleaned[3])) + 3.7)
          elif line_cleaned[1] == '10' or line_cleaned[1] == '11' or line_cleaned[1] == '12':
            wd_lums.append(float(line_cleaned[2]))
            wd_rads.append(float(line_cleaned[3]))
            wd_tems.append(0.25*(float(line_cleaned[2]) - 2*float(line_cleaned[3])) + 3.7)
          elif line_cleaned[1] == '13':
            ns_lums.append(float(line_cleaned[2]))
            ns_rads.append(float(line_cleaned[3]))
            ns_tems.append(0.25*(float(line_cleaned[2]) - 2*float(line_cleaned[3])) + 3.7)
          elif line_cleaned[1] == '14':
            bh_lums.append(float(line_cleaned[2]))
            bh_rads.append(float(line_cleaned[3]))
            bh_tems.append(0.25*(float(line_cleaned[2]) - 2*float(line_cleaned[3])) + 3.7)
          elif line_cleaned[1] == '15':
            sn_lums.append(float(line_cleaned[2]))
            sn_rads.append(float(line_cleaned[3]))
            sn_tems.append(0.25*(float(line_cleaned[2]) - 2*float(line_cleaned[3])) + 3.7)
          else:
            print(line_cleaned[1])

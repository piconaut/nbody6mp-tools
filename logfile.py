#!/usr/bin/python

def count_special(input_files,out_dir,target):

  for input_file in input_files:

    n_nsn = []
    count_next = False

    with open(input_file,'r') as f:
      for i,line in enumerate(f):
        if count_next:
          line_clean = line
          while '  ' in line_clean:
            line_clean = line_clean.replace('  ',' ')
          n_nsn.append(line_clean.strip().split(' ')[7] + '\n')
          count_next = False
        elif target.upper() in line:
          count_next = True

    out_name = out_dir + input_file.split('/')[-2] + '_' + target + '.dat'
    
    with open(out_name,'w') as f:
      f.writelines(n_nsn)

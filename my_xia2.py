#!/usr/bin/python
# -*- coding: utf-8 -*-

#usage:
#python my_xia2.py --directory=native_data
#or
#python my_xia2.py --directory=anomalous_data


################################################################################
#######################     anomalous data    #################################
################################################################################
def anomalous_data_proc(input_dir, output_dir):
  with open(os.path.join(output_dir,
    'anomalous_processing.txt'), 'w') as text_file:
    text_file.write('Creating PDB list for anomalous data \n')
  text_file.close()
  
  anomalous_job_list = os.path.join(output_dir, 'pdb_id_anomalous.txt')
  fh = open(anomalous_job_list, 'w')
  
  anomalous_pdb_list = listdir(input_dir)
  anomalous_pdb_id = []
  for pdb in anomalous_pdb_list:
    if len(pdb) == 4:
      anomalous_pdb_id.append(pdb)
    else:
      pass
  for pdb in anomalous_pdb_id:
    fh.write(pdb)
    fh.write('\n')
  fh.close()

  number_anomalous_pdb = len(anomalous_pdb_id)
  with open(os.path.join(output_dir,
    'anomalous_processing.txt'), 'a') as text_file:
    text_file.write('Total number of anomalous data sets is %s \n'
    %number_anomalous_pdb)
  text_file.close()

  os.chdir(output_dir)
  anomalous_jobs_proc = open('pdb_id_anomalous.txt', 'r+')
  for line in anomalous_jobs_proc:
    line = line.strip()
    pdb_id = line

    with open(os.path.join(output_dir,
      'anomalous_processing.txt'), 'a') as text_file:
      text_file.write('Processing anomalous data for %s \n' %(pdb_id))
	  
    os.mkdir(os.path.join(output_dir,pdb_id))
    os.chdir(os.path.join(output_dir,pdb_id)) #this changes ibto the directory
    #Popen sets indeed xia2 running
      #p = subprocess.Popen(['xia2', 'pipeline=dials'
    #'atom=Se', 'image=/dls/mx-scratch/jcsg-data/anomalous_data/%s' % pdb_id])
    fh = open('dummy.txt', 'w')
    fh.close()

  with open(os.path.join(output_dir,
    'anomalous_processing.txt'), 'a') as text_file:
    text_file.write(
      'Finished processing with xia2 for %s anomalous data sets \n'
      %number_anomalous_pdb)
  text_file.close()
  os.chdir(output_dir)

################################################################################
#########################     native data     ##################################
################################################################################
def native_data_proc(input_dir, output_dir):
  with open(os.path.join(output_dir,
    'native_processing.txt'), 'w') as text_file:
    text_file.write('Creating PDB list for native data \n')
  text_file.close()
  
  native_job_list = os.path.join(output_dir, 'pdb_id_native.txt')
  fh = open(native_job_list, 'w')
  
  native_pdb_list = listdir(input_dir)
  native_pdb_id = []
  for pdb in native_pdb_list:
    if len(pdb) == 4:
      native_pdb_id.append(pdb)
    else:
      pass
  for pdb in native_pdb_id:
    fh.write(pdb)
    fh.write('\n')
  fh.close()

  number_native_pdb = len(native_pdb_id)
  with open(os.path.join(output_dir,
    'native_processing.txt'), 'a') as text_file:
    text_file.write('Total number of native data sets is %s \n'
    %number_native_pdb)
  text_file.close()

  os.chdir(output_dir)
  native_jobs_proc = open('pdb_id_native.txt', 'r+')
  for line in native_jobs_proc:
    line = line.strip()
    pdb_id = line
    with open(os.path.join(output_dir,
      'native_processing.txt'), 'a') as text_file:
      text_file.write('Processing native data for %s \n' %(pdb_id))
	  
    os.mkdir(os.path.join(output_dir,pdb_id))
    os.chdir(os.path.join(output_dir,pdb_id)) #this changes ibto the directory
    #Popen sets indeed xia2 running
      #p = subprocess.Popen(['xia2', 'pipeline=dials'
    #'atom=Se', 'image=/dls/mx-scratch/jcsg-data/MR_data/%s' % pdb_id])
    fh = open('dummy.txt', 'w')
    fh.close()

  with open(os.path.join(output_dir,
    'native_processing.txt'), 'a') as text_file:
    text_file.write(
      'Finished processing with xia2 for %s native data sets \n'
      %number_native_pdb)
  text_file.close()



if __name__ == '__main__':
    
  import os
  from os import listdir
  from os.path import isfile, join 
  import argparse
  import subprocess
  #from libtbx import easy_mp
  import datetime

  parser = argparse.ArgumentParser(description='commnad line argument')
  parser.add_argument(
    '--anomalous_directory', 
    type=str, 
    dest = 'anomalous_directory',
    default='/dls/mx-scratch/jcsg-data/anomalous_data',
    help='anomalous_data_directory')
  parser.add_argument(
    '--native_directory',
    type=str,
    dest = 'native_directory',
    default='/dls/mx-scratch/jcsg-data/MR_data',
    help='native_data_directory')
  parser.add_argument(
    '--directory',
    type=str,
    dest = 'directory',
    default=None,
    choices = ['native_data', 'anomalous_data'],
    help='native_data_directory')
  args = parser.parse_args()


  output_path = '/dls/tmp'

  #this one creates a variable carrying the current date
  date = datetime.datetime.today().strftime('%Y%m%d')

  #this one checks for the exitance of a directory with current date stamp;
  #if it doesn't exist then it gets created
  if not os.path.exists('/dls/tmp/ghp45345/xia2_stresstest/%s' % date):
    os.makedirs(os.path.join(output_path, 'ghp45345', 'xia2_stresstest',
  date))

  #output directory where to do the data processing
  output_dir = '/dls/tmp/ghp45345/xia2_stresstest/%s' % date

  
  if args.directory == 'anomalous_data':
    anomalous_data_proc(args.anomalous_directory, output_dir)
  elif args.directory == 'native_data':
    native_data_proc(args.native_directory, output_dir)
  else:
    raise Error('No data provided')

 



 

#############################################################################

#some James' code to run some processes in parallel; haven't implemented that
#yet but maybe can be done through jenkins anyway 
#from libtbx import easy_mp
#
#def func(x):
#  print x
#
#iterable = list(range(10))
#
#easy_mp.parallel_map(
#func, iterable, processes=2)









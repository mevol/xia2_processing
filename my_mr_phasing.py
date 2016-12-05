# -*- coding: utf-8 -*-
import os
from os import listdir
from os.path import isfile, join 
import argparse
import subprocess
#from libtbx import easy_mp
import datetime
from metrix import simpleMR

#don't forget to source my metrix environment by putting at the beginning of my
#jenkins script
#'source /dls/science/users/ghp45345/dials/dials-dev20160226/dials_env.sh'
#then I can make use of metrix.simpleMR to run MR

#defining some directories and input/output paths

output_path = '/dls/tmp'
input_path = '/dls/tmp/ghp45345/xia2_stresstest/'

proc_dirs = sorted(os.listdir(input_path))
latest_proc_dir = proc_dirs[-1]

date = datetime.datetime.today().strftime('%Y%m%d')

if not os.path.exists('/dls/tmp/ghp45345/MR_phasing/%s' %(date)):
    os.makedirs(os.path.join(output_path, 'ghp45345', 'MR_phasing',
    date))

output_dir = '/dls/tmp/ghp45345/MR_phasing/%s' % date


#changing into output directory and create the job lists
#and directory structure

os.chdir(output_dir)

phasing_job_list = os.path.join(output_dir, 'pdb_id_phasing.txt')
fh = open(phasing_job_list, 'w')
phasing_pdb_list = listdir('/dls/tmp/ghp45345/xia2_stresstest/%s'
		      %latest_proc_dir)
phasing_pdb_id = []
for pdb in phasing_pdb_list:
  if len(pdb) == 4:
    phasing_pdb_id.append(pdb)
  else:
    pass
for pdb in phasing_pdb_id:
  fh.write(pdb)
  fh.write('\n')
fh.close()


number_phasing_pdb = len(phasing_pdb_id)
with open(os.path.join(output_dir,'MR_phasing.txt'), 'w') as text_file:
  text_file.write('Total number of data sets is %s \n'
  %(number_phasing_pdb))
text_file.close()

#setting up environment to run simpleMR
#command = ['bash',
#'-c', '/dls/science/users/ghp45345/dials/dials-dev20160226/dials_env.sh']
#proc = subprocess.Popen(command, stdout = subprocess.PIPE)

#subprocess.Popen('source',
#  '/dls/science/users/ghp45345/dials/dials-dev20160226/dials_env.sh')

mr_phasing_jobs = open('pdb_id_phasing.txt', 'r+')
for line in mr_phasing_jobs:
  line = line.strip()
  pdb_id = line
  with open(os.path.join(output_dir, 'MR_phasing.txt'), 'a') as text_file:
    text_file.write('Run molecular replacement for %s using simpleMR \n'
    %(pdb_id))
  os.mkdir(os.path.join(output_dir,pdb_id))
  os.chdir(os.path.join(output_dir,pdb_id)) #this changes into the directory
  MTZ_dir = '/dls/tmp/ghp45345/xia2_stresstest/%s/%s' %(latest_proc_dir, pdb_id)
  #MTZ_dir = '/dls/tmp/ghp45345/xia2_stresstest/%s/%s' %date, pdb_id
  input_path = os.path.join(MTZ_dir, 'DataFiles', 'AUTOMATIC_DEFAULT_free.mtz')
  
  metrix.simpleMR(
	  --xyzin='/dls/mx-scratch/jcsg-data/MR_search_models/%s' %(pdb),	
	  --hklin=%s %(input_path),	   
	  --seqin='/dls/mx-scratch/jcsg-data/sequence/%s' %(pdb))

  #p = subprocess.Popen(
  #  'metrix.simpleMR',
  #  xyzin='/dls/mx-scratch/jcsg-data/MR_search_models/%s' %(pdb),
  #  hklin=%s %(input_path),
  #  seqin='/dls/mx-scratch/jcsg-data/sequence/%s' %(pdb))

 
  fh = open('dummy.txt', 'w')
  fh.close()
  #create an if statement here to test whether Big_EP produced any results
  #at all;
  with open(os.path.join(output_dir, 'EP_phasing.txt'), 'a') as text_file:
    text_file.write('Finished experimental phasing for %s  \n' %(pdb_id))
  text_file.close()
  os.chdir(output_dir)

with open(os.path.join(output_dir, 'EP_phasing.txt'), 'a') as text_file:
  text_file.write('Finished experimental phasing for %s  PDB IDs\n'
  %(number_phasing_pdb))
text_file.close()

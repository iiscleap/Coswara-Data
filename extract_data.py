import os
import sys
import subprocess
import numpy as np
import glob
import json
import pandas as pd

'''
This script creates a folder "Extracted_data" inside which it extracts all the wav files in the directories date-wise
'''

coswara_data_dir = os.path.abspath('.') # Local Path of iiscleap/Coswara-Data Repo
extracted_data_dir = os.path.join(coswara_data_dir, 'Extracted_data')  

if not os.path.exists(coswara_data_dir):
    raise("Check the Coswara dataset directory!")

if not os.path.exists(extracted_data_dir):
    os.makedirs(extracted_data_dir) # Creates the Extracted_data folder if it doesn't exist

dirs_extracted = set(map(os.path.basename,glob.glob('{}/202*'.format(extracted_data_dir))))
dirs_all = set(map(os.path.basename,glob.glob('{}/202*'.format(coswara_data_dir))))

dirs_to_extract = list(set(dirs_all) - dirs_extracted)

for d in dirs_to_extract:
    p = subprocess.Popen('cat {}/{}/*.tar.gz.* |tar -xvz -C {}/'.format(coswara_data_dir, d, extracted_data_dir), shell=True)
    p.wait()

print("Extraction process complete!")

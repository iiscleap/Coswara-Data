import os
import shutil
import glob
import tarfile

'''
This script creates a folder "Extracted_data" inside which it extracts all the wav files in the directories date-wise
'''

coswara_data_dir = os.path.abspath('.')  # Local Path of iiscleap/Coswara-Data Repo
extracted_data_dir = os.path.join(coswara_data_dir, 'extracted_data')

if not os.path.exists(coswara_data_dir):
    raise ("Check the Coswara dataset directory!")

if not os.path.exists(extracted_data_dir):
    os.makedirs(extracted_data_dir)  # Creates the Extracted_data folder if it doesn't exist

dirs_extracted = set(map(os.path.basename, glob.glob('{}/202*'.format(extracted_data_dir))))
dirs_all = set(map(os.path.basename, glob.glob('{}/202*'.format(coswara_data_dir))))

dirs_to_extract = list(set(dirs_all) - dirs_extracted)
all_file_temp = os.path.join(extracted_data_dir, "temp.tar.gz")


def extract(infile: str):
    # concatenate all the *tar.gz* files
    with open(all_file_temp, 'wb') as wfp:
        for fn in infile:
            with open(fn, 'rb') as rfp:
                shutil.copyfileobj(rfp, wfp)

        # extract the all-in-one file
        tar = tarfile.open(all_file_temp, "r:gz")
        tar.extractall(path=extracted_data_dir)
        tar.close()


for d in dirs_to_extract:
    dir_ = os.listdir(os.path.join(coswara_data_dir, d))
    part_files = [os.path.join(dir_, file) for file in dir_ if 'tar.gz' in file]
    extract(part_files)
    os.remove(os.path.join(extracted_data_dir, "temp.tar.gz"))

print("Extraction process complete!")

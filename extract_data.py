import glob
import json
import logging
import os
import shutil
import tarfile

import pandas as pd

logging.basicConfig(level=logging.INFO)

'''
This script creates a folder "Extracted_data" inside which it extracts all the wav files in the directories date-wise
'''


def unzip_files(infile: list, all_file_temp: str, extracted_data_dir: str) -> bool:
    """
    Extracts the tar.gz files in the list 'infile' into the specified directory 'extracted_data_dir' using
    a temporary file 'all_file_temp' as an intermediate step.

    Args:
        infile: list of tar.gz files
        all_file_temp: temporary file to store the concatenated files
        extracted_data_dir: directory to extract the files

    Returns:
        bool: True if the extraction is successful, False otherwise
    """
    try:
        logging.info(f'Extracting {infile[0].split(".a")[0]}')
        # concatenate all the *tar.gz* files
        with open(all_file_temp, 'wb') as wfp:
            infile.sort()
            for fn in infile:
                with open(fn, 'rb') as rfp:
                    shutil.copyfileobj(rfp, wfp)

        # extract the all-in-one file
        tar = tarfile.open(all_file_temp, "r:gz")
        tar.extractall(path=extracted_data_dir)
        tar.close()
        return True

    except Exception as e:
        logging.error(f"Error occurred: {e}")
        return False


def extract_coswara(
        coswara_dir_path: str = os.path.abspath('.')
) -> bool:
    extracted_data_dir = os.path.join(coswara_dir_path, 'Extracted_data')

    if not os.path.exists(coswara_dir_path):
        logging.error("Check the Coswara dataset directory!")

    if not os.path.exists(extracted_data_dir):
        os.makedirs(extracted_data_dir)  # Creates the Extracted_data folder if it doesn't exist

        dirs_extracted = set(map(os.path.basename, glob.glob(f'{extracted_data_dir}/202*')))
        dirs_all = set(map(os.path.basename, glob.glob(f'{coswara_dir_path}/202*')))

        dirs_to_extract = list(set(dirs_all) - dirs_extracted)
        all_file_temp = os.path.join(extracted_data_dir, "temp.tar.gz")

        for d in dirs_to_extract:
            dir_ = os.path.join(coswara_dir_path, d)
            part_files = [os.path.join(dir_, file) for file in os.listdir(dir_) if 'tar.gz' in file]
            unzip_files(part_files, all_file_temp, extracted_data_dir)
            os.remove(os.path.join(extracted_data_dir, "temp.tar.gz"))

        logging.info("Extraction process complete!")
        return True
    elif os.path.exists(extracted_data_dir) and len(os.listdir(extracted_data_dir)) != 0:
        logging.info("Data already extracted!")
        return True
    else:
        logging.error("Extraction process failed!")
        return False


def create_coswara_df(
        coswara_data_dir: str = os.path.abspath('.'),
) -> pd.DataFrame:
    if not os.path.exists(coswara_data_dir):
        raise "Check the Coswara dataset directory!"

    if not extract_coswara():
        raise RuntimeError("Check the Coswara dataset directory!")

    csv_file_path = os.path.join(coswara_data_dir, 'coswara_metadata.csv')
    extracted_data_dir = os.path.join(coswara_data_dir, 'Extracted_data')

    # Collect metadata and audio file paths
    coswara_data = []
    path_patter_files = f"{extracted_data_dir}/**/metadata.json"
    for metadata_file in glob.glob(path_patter_files, recursive=True):
        with open(metadata_file, 'r') as f:
            metadata = json.load(f)

        audio_files = glob.glob(os.path.join(os.path.dirname(metadata_file), '*.wav'))
        for audio_file in audio_files:
            recorder_data = metadata.copy()
            recorder_data['audio_path'] = audio_file
            recorder_data['audio_type'] = os.path.basename(audio_file).split('.')[0]
            recorder_data['id'] = os.path.dirname(audio_file).split("/")[-1]

            coswara_data.append(recorder_data)

    # Create DataFrame
    raw_coswara_df = pd.DataFrame(coswara_data)
    coswara_mapper_columns = {
        "id": "id",
        "a": "age",
        "g": "gender",
        "l_c": "location_country",
        "l_l": "location_locality",
        "l_s": "location_state",
        "covid_status": "covid_status",
        "audio_path": "audio_path",
        "audio_type": "audio_type",
        "asthma": "asthma",
        "cough": "cough",
        "smoker": "smoker",
        "test_status": "test_status",
        "ht": "hyper_tension",
        "cold": "cold",
        "diabetes": "diabetes",
        "diarrhoea": "diarrhoea",
        "um": "using_mask",
        "ihd": "ischemic_heart_disease",
        "bd": "breathing_difficulty",
        "st": "sore_throat",
        "fever": "fever",
        "ftg": "fatigue",
        "mp": "muscle_pain",
        "loss_of_smell": "loss_of_smell",
        "cld": "chronic_lung_disease",
        "pneumonia": "pneumonia",
        "ctScan": "ct_scan_taken",
        "testType": "test_type",
        "test_date": "test_covid_date",
        "vacc": "vaccination_status",
        "ctDate": "ct_scan_date",
        "ctScore": "ct_score",
        "others_resp": "other_respiratory_illness",
        "others_preexist": "other_preexisting_conditions",
    }
    raw_coswara_df.rename(mapper=coswara_mapper_columns, axis=1, inplace=True)

    # Drop all columns except the ones in mapper_columns
    raw_coswara_df = raw_coswara_df[coswara_mapper_columns.values()]

    # Write to CSV
    raw_coswara_df.to_csv(csv_file_path, index=False)
    print(f"CSV file created at {csv_file_path}")
    return raw_coswara_df


def get_coswara_subset_by_filters(
        dataframe: pd.DataFrame,
        filters: dict,
        output_dir: str = os.path.abspath('.'),
        prefix_name: str = 'coswara_subset'
) -> pd.DataFrame:
    df_, coswara_subset = dataframe.copy(), pd.DataFrame()
    for key, value in filters.items():
        if isinstance(value, list):
            for item in value:
                coswara_subset = pd.concat([coswara_subset, df_[df_[key] == item]])
        else:
            coswara_subset = df_[df_[key] == value]

    coswara_subset.reset_index(drop=True, inplace=True)
    coswara_subset = coswara_subset.drop_duplicates()
    coswara_subset = coswara_subset[['id', 'audio_path', 'covid_status']]

    coswara_subset.rename(columns={'covid_status': 'label', 'audio_path': 'path'}, inplace=True)
    coswara_subset['label'] = coswara_subset['label'].apply(lambda x: 0 if x == 'healthy' else 1)

    coswara_subset.to_csv(os.path.join(output_dir, f'coswara_subset-{prefix_name}.csv'), index=False)
    logging.info(f"Subset saved at {os.path.join(output_dir, f'coswara_subset-{prefix_name}.csv')}")
    return coswara_subset


if __name__ == "__main__":
    coswara_path = os.path.abspath('.')  # Local Path of iiscleap/Coswara-Data Repo
    coswara_df = create_coswara_df()

    # Get all the cough samples {"audio_type": "cough-heavy", "audio_type": "cough-shallow"}
    cough_samples = get_coswara_subset_by_filters(coswara_df,
                                                  {"audio_type": ["cough-heavy", "cough-shallow"]},
                                                  prefix_name="cough_samples")
    vowel_a_samples = get_coswara_subset_by_filters(coswara_df,
                                                    {"audio_type": "vowel-a"},
                                                    prefix_name="vowel_a_samples")

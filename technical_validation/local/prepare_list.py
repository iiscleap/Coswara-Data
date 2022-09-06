# created by DebarpanB
# date 26th August, 2022

import argparse, configparser
import pickle
import pandas as pd
import librosa
import numpy as np
import torchaudio
import torch
from pdb import set_trace as bp

def main(annotation_file, pathfile, outlist, outpath):
    df_annotation = pd.read_csv(annotation_file)
    df_annotation["id"] = df_annotation["FILENAME"].str.split("_", n=1, expand=True)[0]
    df_annotation_drop = df_annotation.drop(columns=["FILENAME"]).iloc[:, [1, 0]]
    df_annotation_drop[(df_annotation_drop[' QUALITY'].isin([1,2]))].to_csv(outlist, header=None, index=False, sep=' ')

    df_path = pd.read_csv(pathfile, header=None, delimiter=' ')
    df_path.columns = ['id', 'path']
    df_path_select = df_path[(df_path.id.isin(df_annotation.FILENAME.values))]
    assert df_annotation.shape[0]==df_path_select.shape[0]
    df_path_select["id"] = df_path_select["id"].str.split("_", n=1, expand=True)[0]
    df_path_select.to_csv(outpath, header=None, index=False, sep=' ')


if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--annotation', '-a', required=True)
    parser.add_argument('--pathfile', '-p', required=True)
    parser.add_argument('--outlist', '-l', required=True)
    parser.add_argument('--outpath', '-s', required=True)
    args = parser.parse_args()

    main(args.annotation, args.pathfile, args.outlist, args.outpath)
# created by DebarpanB
# date 26th August, 2022

import argparse, configparser
from ast import parse
from turtle import pd
import numpy as np
import pandas as pd

def main(featslist, labellist, pathlist):
    df_feats = pd.read_csv(featslist, header=None, delimiter=' ')
    df_feats.columns = ['id', 'feat_path']

    df_labels = pd.read_csv(labellist, header=None, delimiter=' ')
    df_labels.columns = ['id', 'label']

    df_path = pd.read_csv(pathlist, header=None, delimiter=' ')
    df_path.columns = ['id', 'path']

    df_labels[(df_labels.id.isin(df_feats.id.values))].to_csv(labellist, header=None, index=False, sep=' ')
    df_path[(df_path.id.isin(df_feats.id.values))].to_csv(pathlist, header=None, index=False, sep=' ')


if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--featslist', '-f', required=True)
    parser.add_argument('--labellist', '-l', required=True)
    parser.add_argument('--pathlist', '-s', required=True)
    args = parser.parse_args()

    main(args.featslist, args.labellist, args.pathlist)
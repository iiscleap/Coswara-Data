# created by DebarpanB
# date 26th August, 2022

import argparse, configparser
import numpy as np
import pandas as pd
import pickle
import os
import random
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from matplotlib import pyplot as plt
from pdb import set_trace as bp

SEED = 42
random.seed(SEED)
np.random.seed(SEED)

def get_data(file_list,feats_file,labels_file,shuffle=False):
	#bp()
	#%% read the list of files
	file_list = open(file_list).readlines()
	file_list = [line.strip().split() for line in file_list]

	#%% read labels
	temp = open(labels_file).readlines()
	temp = [line.strip().split() for line in temp]
	labels={}
	categories = ['0','1', '2']
	for fil,label in temp:
		labels[fil]=categories.index(label)
	del temp

	#%% read feats.scp
	temp = open(feats_file).readlines()
	temp = [line.strip().split() for line in temp]
	feats={}
	for fil,filpath in temp:
		feats[fil]=filpath
	del temp

	#%% make examples
	egs = []
	for fil,_ in file_list:
		if feats.get(fil,None):
			F = pickle.load(open(feats[fil],'rb'))
			label = labels.get(fil,None)
			if label is not None:
				egs.append( np.concatenate( (F.mean(axis=0).reshape(1,-1),np.array([label]).reshape(1,-1)),axis=1 ) )

	egs = np.vstack(egs)

	if shuffle:
		np.random.shuffle(egs)	
	return egs[:,:-1],egs[:,-1]

def expand(x, y, gap=1e-4):
    add = np.tile([0, gap, np.nan], len(x))
    x1 = np.repeat(x, 3) + add
    y1 = np.repeat(y, 3) + add
    return x1, y1

def main(config, datadir_name, audiocategory, output_dir):
	audio_cats = audiocategory.split(',')
	train_feats_all, train_labels_all = [], []
	for i, audio_cat in enumerate(audio_cats):
		datadir = os.path.join(datadir_name, audio_cat)
		# Training dataset
		train_feats, _ = get_data(datadir+"/all.scp",datadir+"/feats.scp",datadir+"/all", shuffle=True)
		train_labels = np.array([i]*train_feats.shape[0])
		train_feats = train_feats[:, :int(train_feats.shape[1]/3)]
		train_feats_all.append(train_feats)
		train_labels_all.append(train_labels)
	train_feats_all = np.vstack(train_feats_all)
	train_labels_all = np.vstack([i.reshape((-1,1)) for i in train_labels_all]).flatten()
	
	X_train, X_test, y_train, y_test = train_test_split(train_feats_all, train_labels_all, test_size=0.3, random_state=SEED)
	X_train, X_val, y_train, y_val = train_test_split(X_train, y_train, test_size =0.21, random_state=SEED)

	if config['default']['classifier']=='RandomForest':
		scaler = StandardScaler(with_mean=True, with_std=False)
		X_train = scaler.fit_transform(X_train)
		X_test = scaler.transform(X_test)
		clf = RandomForestClassifier(n_estimators=int(config[config['default']['classifier']]['n_estimators']),
									criterion=config[config['default']['classifier']]['criterion'],
									random_state=SEED)
		clf.fit(X_train, y_train)
		val_accuracy = (np.count_nonzero(clf.predict(X_val)==y_val)*100)/y_val.shape[0]
		print(f'Val accuracy: {val_accuracy}')
		test_accuracy = (np.count_nonzero(clf.predict(X_test)==y_test)*100)/y_test.shape[0]
		print(f'Test accuracy: {test_accuracy}')
		op_save_path = os.path.join(output_dir, config['default']['classifier'])
		if not os.path.exists(op_save_path): os.mkdir(op_save_path)
		np.save(os.path.join(op_save_path, 'y_true.npy'), y_test)
		np.save(os.path.join(op_save_path, 'y_pred.npy'), clf.predict(X_test))
		np.save(os.path.join(op_save_path, 'y_pred_proba.npy'), clf.predict_proba(X_test))
	else:
		print('unknown classifier. exiting...')
		exit()

	#plot
	# cdict = {0: 'red', 1: 'blue', 2: 'green'}
	# fig, ax = plt.subplots()
	# for g in np.unique(train_labels):
	# 	ix = np.where(train_labels == g)
	# 	ax.scatter(X_proj[ix][:,0], X_proj[ix][:,1], c = cdict[g], label = g, s = 100, alpha=0.4*(2.1-g))
	# 	#ax.scatter(*expand(X_proj[ix][:,0], X_proj[ix][:,1]), lw=0, c = cdict[g], label = g, s = 100, alpha=0.5)
	# ax.legend()
	# save_plot_dir = outdir+'/'+config['default']['type']
	# if not os.path.exists(save_plot_dir): os.mkdir(save_plot_dir)
	# plt.savefig(save_plot_dir+'/plot.png')


if __name__=='__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('--classification_config', '-c', required=True)
	parser.add_argument('--datadir', '-d', required=True)
	parser.add_argument('--audiocategory', '-a', required=True)
	#parser.add_argument('--featuredir', '-f', required=True)
	parser.add_argument('--output_dir', '-o', required=True)
	args = parser.parse_args()

	config = configparser.ConfigParser()
	config.read(args.classification_config)

	main(config, args.datadir, args.audiocategory, args.output_dir)
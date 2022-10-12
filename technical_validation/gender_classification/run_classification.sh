# created by DebarpanB
# date 1st September, 2022

stage=0

# annotationdir='annotations/LABELS/'
#audiodir='/data1/srikanthr/Coswara/data_preparation/Coswara-Data-Extracted'
# pathfile='path_files/wav.scp'
# metadata_file='metadata_files/combined_data.csv'
audiocategory='counting-normal'

datadir_name='data'
#datadir=$datadir_name/$audiocategory
feature_dir_name='feats'
#feature_dir=$feature_dir_name/$audiocategory
output_dir='results'

classification_config='conf/classification.conf'

. parse_options.sh

mkdir -p $output_dir

if [ $stage -le 0 ]; then

	echo "==== classification ====="
    python local/classification.py -c $classification_config -a $audiocategory -d $datadir_name -o $output_dir
fi

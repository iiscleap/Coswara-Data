# Coswara-Data

<a rel="license" href="https://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://licensebuttons.net/l/by/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="https://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International (CC BY 4.0) License</a>.

Project Coswara by Indian Institute of Science (IISc) Bangalore is an attempt to build a diagnostic tool for COVID-19 detection using the audio recordings such as breathing, cough and speech sounds of an individual. Currently, the project is in the data collection stage through crowdsourcing. To contribute your audio samples, please go to Project Coswara(https://coswara.iisc.ac.in/). The exercise takes 5-7 minutes.

<strong>What am I looking at?</strong>
This github repository contains the raw audio data collected through https://coswara.iisc.ac.in/ . Every participant contributes nine sound samples. You can read the paper: [Coswara - A Database of Breathing, Cough, and Voice Sounds for COVID-19 Diagnosis](https://arxiv.org/abs/2005.10548) to know more about the dataset. Note that the dataset size has increased since this paper came out. We also maintain a (less frequently updated) blog [here](https://iiscleap.github.io/coswara-blog/coswara/2020/11/23/visualize_coswara_data_metadata.html).

<strong>What is the structure of the repository?</strong>
Each folder contains metadata and audio recordings corresponding to contributors. The folder is compressed. To download and extract the data, you can run the script `extract_data.py`

<strong>What are the different sound samples?</strong>
Sound samples collected include breathing sounds (fast and slow), cough sounds (deep and shallow), phonation of sustained vowels (/a/ as in made, /i/,/o/), and counting numbers at slow and fast pace. Metadata information collected includes the participant's age, gender, location (country, state/ province), current health status (healthy/ exposed/ positive/recovered) and the presence of comorbidities (pre-existing medical conditions).

<strong>Can I see the metadata before downloading whole repository?</strong>
Yes. The file `combined_data.csv` contains a summary of metadata. The file `csv_labels_legend.json` contains information about the columns present in `combined_data.csv`.

<strong>Is there any audio quality check?</strong>
Yes. The audio files are manually listened and labeled as one of the three categories: 2(excellent), 1(good), 0(bad). The labels are present in the `annotations` folder.

<strong>How to cite this dataset in your work?</strong>
Great to know you found it useful. You can cite the paper: Coswara - A Database of Breathing, Cough, and Voice Sounds for COVID-19 Diagnosis (https://arxiv.org/abs/2005.10548)

<strong>Is there any web application for COVID-19 screening based on respiratory acoustics?</strong>
Yes! One can record his/her respiratory sounds at [Coswara web application](https://coswara.iisc.ac.in/) and obtain a COVID-19 probability score in few seconds. Demo: [here](https://www.youtube.com/watch?v=9CltKLE_HIs&t=19s&ab_channel=LEAPLabIIScIndianInstituteofScience), paper: [here](https://arxiv.org/pdf/2206.05053.pdf)

<strong>What is the count of participants in each folder?</strong>

- 2020-04-13 contains 76 samples.
- 2020-04-15 contains 161 samples. 
- 2020-04-16 contains 197 samples.
- 2020-04-17 contains 168 samples.
- 2020-04-18 contains 46 samples. 
- 2020-04-19 contains 32 samples.
- 2020-04-24 contains 28 samples.
- 2020-04-30 contains 23 samples.
- 2020-05-02 contains 155 samples.
- 2020-05-04 contains 81 samples.
- 2020-05-05 contains 14 samples.
- 2020-05-25 contains 54 samples.
- 2020-06-04 contains 20 samples.
- 2020-07-07 contains 42 samples.
- 2020-07-20 contains 21 samples.
- 2020-08-03 contains 29 samples.
- 2020-08-14 contains 83 samples.
- 2020-08-20 contains 48 samples.
- 2020-08-24 contains 19 samples.
- 2020-09-01 contains 24 samples.
- 2020-09-11 contains 16 samples.
- 2020-09-19 contains 32 samples.
- 2020-09-30 contains 26 samples.
- 2020-10-12 contains 18 samples.
- 2020-10-31 contains 29 samples.
- 2020-11-30 contains 17 samples.
- 2020-12-21 contains 27 samples.
- 2021-02-06 contains 18 samples.
- 2021-04-06 contains 66 samples.
- 2021-04-19 contains 35 samples.
- 2021-04-26 contains 41 samples.
- 2021-05-07 contains 54 samples.
- 2021-05-23 contains 31 samples.
- 2021-06-03 contains 42 samples.
- 2021-06-18 contains 56 samples.
- 2021-06-30 contains 67 samples.
- 2021-07-14 contains 52 samples.
- 2021-08-16 contains 82 samples.
- 2021-08-30 contains 64 samples. 
- 2021-09-14 contains 37 samples.
- 2021-09-30 contains 103 samples.
- 2022-01-16 contains 141 samples.
- 2022-02-24 contains 372 samples.

Each folder also has a CSV file which contains metadata of each sample (that is, participant).

<strong>Can I know the individuals maintaining this project?</strong>
Yes, we are a team of Professors, PostDocs, Engineers, and Research Scholars affiliated with the Indian Institute of Science, Bangalore (India). [Sriram Ganapathy](http://leap.ee.iisc.ac.in/sriram/), Assistant Professor, Dept. Electrical Engineering, IISc is the Principal Investigator of this project.

Current Members: Debarpan Bhattacharya, Neeraj Kumar Sharma, Prasanta Kumar Ghosh, Srikanth Raj Chetupalli, Sriram Ganapathy

Past Members: Anand Mohan, Ananya Muguli, Debottam Dutta, Prashant Krishnan, Pravin Mote, Rohit Kumar, Shreyas Ramoji

(arranged in alphabetical order)

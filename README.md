# Coswara-Data

Project Coswara by Indian Institute of Science (IISc) Bangalore is an attempt to build a diagnostic tool for Covid-19 based on respiratory, cough and speech sounds. The project is in the data collection stage now. It requires the participants to provide a recording of breathing sounds, cough sounds, sustained phonation of vowel sounds and a counting exercise.

#### NOTE: This repository contains the raw audio data received at https://coswara.iisc.ac.in/ . The annotation process of this is ongoing (https://github.com/iiscleap/Coswara-Exp) and would be delayed compared to the uploaded data here.

#### This is the data repository for Project Coswara. (https://coswara.iisc.ac.in/)

<p>Each folder contains metadata and recordings corresponding to a person. The audio recordings are in wav format (44.1KHz).

Voice samples collected include breathing sounds (fast and slow), cough sounds (deep and shallow), phonation of sustained vowels (/a/ as in made, /i/,/o/), and counting numbers at slow and fast pace. Metadata information collected includes the participant's age, gender, location (country, state/ province), current health status (healthy/ exposed/ cured/ infected) and the presence of comorbidities (pre-existing medical conditions). </p>

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

To download the data, you can merge the split tar files using the command below to obtain a single tar file and then untar it.

`cat *.tar.gz.* > file_name.tar.gz `

`tar -xvzf file_name.tar.gz`

Each folder also has a CSV file which contains metadata of each sample.

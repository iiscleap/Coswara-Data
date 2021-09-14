# Coswara-Data

<a rel="license" href="http://creativecommons.org/licenses/by-nc-nd/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-nd/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-nd/4.0/">Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License</a>.

Project Coswara by Indian Institute of Science (IISc) Bangalore is an attempt to build a diagnostic tool for Covid-19 based on respiratory, cough and speech sounds. The project is in the data collection stage now. It requires the participants to provide a recording of breathing sounds, cough sounds, sustained phonation of vowel sounds and a counting exercise.

#### NOTE: This repository contains the raw audio data received at https://coswara.iisc.ac.in/ . The annotation process of this is ongoing (https://github.com/iiscleap/Coswara-Exp) and would be delayed compared to the uploaded data here.

#### This is the data repository for Project Coswara (https://coswara.iisc.ac.in/). To view more information about the database such as distributions of gender, age, etc. click [here](https://iiscleap.github.io/coswara-blog/coswara/2020/11/23/visualize_coswara_data_metadata.html).
<p>Each folder contains metadata and recordings corresponding to a person.

To download and extract the data, you can run the script `extract_data.py`

Voice samples collected include breathing sounds (fast and slow), cough sounds (deep and shallow), phonation of sustained vowels (/a/ as in made, /i/,/o/), and counting numbers at slow and fast pace. Metadata information collected includes the participant's age, gender, location (country, state/ province), current health status (healthy/ exposed/ positive/recovered) and the presence of comorbidities (pre-existing medical conditions). </p>

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
Each folder also has a CSV file which contains metadata of each sample.

The file `csv_labels_legend.json` contains information about the columns present in `combined_data.csv` 

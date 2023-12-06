#!/bin/bash

# Loop from 1 to 20
for i in {1..20}
do
   echo "Running web.py with subject_num = $i"
   export SUBJECT_NUM=$i
   python3 generation/openaiapi/web.py
   echo "Finished run with subject_num = $i"
   echo "---------------------------------"
done
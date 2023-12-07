#!/bin/bash
# Put the subject num here
# Loop from 1 to 20
<<<<<<< HEAD:run_web.sh
for i in {21..30}
=======
for i in {14..20}
>>>>>>> refs/remotes/origin/main:run_web_2 copy.sh
do
   echo "Running web.py with subject_num = $i"
   export SUBJECT_NUM=$i
   python3 generation/openaiapi/web.py
   echo "Finished run with subject_num = $i"
   echo "---------------------------------"
done
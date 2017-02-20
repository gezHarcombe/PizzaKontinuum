#! /bin/bash

python3 main.py $1 > $1.out
python3 score.py $1

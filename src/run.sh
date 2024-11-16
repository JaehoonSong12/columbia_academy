#!/bin/bash
EXECUTABLE="app"                                #### YOUR DATA HERE
############################################
########## Shell Script (Scripts) ##########
############################################
pip install pipreqs
pipreqs . --force
pip install -r requirements.txt
clear
python "${EXECUTABLE}.py"
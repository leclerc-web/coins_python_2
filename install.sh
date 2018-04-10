#!/bin/bash
# INSTALLATION PACKAGE 

pip install terminaltables
echo -ne '#####                     (33%)\r'
sleep 1

pip install simplejson
echo -ne '#############             (66%)\r'
sleep 1

pip install colorclass
echo -ne '#######################   (100%)\r'
echo -ne '\n'

clear
python coins.py
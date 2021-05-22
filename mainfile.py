#! /usr/bin/python3

from readcsv import readcsv
from readcsv import printline
from scpfile import scpfile
import os
from os import path
import sys
import time

line = printline()

# Check if any transfer file given as input
if len(sys.argv) < 2:
   print("No file input......Please try again and input a file to copy")
   sys.exit()

# Check if the transfer exists 
sourc_file = sys.argv[1]
if not path.exists(sourc_file):
    print("File '{}' does not exists.    Try again.....".format(sourc_file))
    sys.exit()

#getting IP list
ip_list = readcsv()
print("\nPlease, confirm the upload of {} on:".format(sourc_file))

for ip in ip_list:
    print("\n{}".format(ip))
#Getting confirmation to proceed or abort
gett = input("\nProceed? [n]y: ")

if gett == 'n':
   sys.exit()

#Prompting for username and password
print(line)
username = input('''\nPlease enter your username : ''')

passwd = input('''\nAnd your password : ''')

print("\n"+line)

#Starting time count 
start = time.time()

for ip in ip_list:
    username = username
    passwd = passwd
    sourc_file = sourc_file
    scpfile(ip, username, passwd, sourc_file)
    print(line)
#Stoping time count
stop = time.time()

#Getting total time 
consume = stop - start
#Printing the upload time
print("Uploads completed in {} seconds.".format(consume))
print(line)

#!/usr/bin/python3

#Import necessary modules 
import socket, argparse, sys, threading, os
from loguru import logger
from readcsv import readcsv
from scpfile import cisco, arista, juniper

#All functions that organize code go here
def ArgParse_Helper():
    parser = argparse.ArgumentParser(description="SCP file transfer programs")
    parser.add_argument("--filename",action='store', help="Enter the file name containing IP addresses", required=True)
    parser.add_argument("--vendor",action='store', help="Enter the vendor name like cisco, arista or juniper", required=True)
    parser.add_argument("--version", action="version", version='%(progs)s 1.0')
    args=parser.parse_args()
    return args

#At the end, the main function encapsulates the core logic
def main():
    args=ArgParse_Helper()
    sourc_file = args.filename
    vendor = args.vendor

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
    print("*"*120)
    username = input('''\nPlease enter your username : ''')

    passwd = input('''\nAnd your password : ''')
    print("\n"+"*"*120)

    #Starting time count 
    logger.info("Copying started....")

    #if vendor is cisco then proceed or else move to different if-else block
    if vendor == 'cisco':
        while ip_list:
            username = username
            passwd = passwd
            sourc_file = sourc_file
            threading.Thread(target=cisco, args= (ip_list.pop(), username, passwd, sourc_file)).start()
        print("*"*120)
    
    #if vendor is arista then proceed or else move to different if-else block
    elif vendor == 'arista':
        while ip_list:
            username = username
            passwd = passwd
            sourc_file = sourc_file
            threading.Thread(target=arista, args= (ip_list.pop(), username, passwd, sourc_file)).start()
        print("*"*120)

    #if vendor is juniper then proceed or else move to different if-else block
    elif vendor == 'juniper':
        while ip_list:
            username = username
            passwd = passwd
            sourc_file = sourc_file
            threading.Thread(target=juniper, args= (ip_list.pop(), username, passwd, sourc_file)).start()
        print("*"*120)
    
    else:
        print("Invalid vendor input :(")

if __name__ == "__main__":
    main()
#! /usr/bin/python3

import csv
import sys


def readcsv():
    try:
        filename = input("Enter csv file name : ")
        ip_list = []
        with open(filename, 'r') as csv_file:
            read_ip = csv.reader(csv_file)
            for ip in read_ip:
                ip_list.append(ip[0])
    except IOError:
        print("\nFile '{}'  does not exists :(  Try again...".format(filename))
        sys.exit()
    return ip_list




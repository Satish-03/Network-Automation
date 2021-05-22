#! /usr/bin/python3
#Importing necesaary modules to call functions
from netmiko import ConnectHandler, file_transfer
from netmiko.ssh_exception import AuthenticationException
from netmiko.ssh_exception import NetMikoTimeoutException
from readcsv import printline
from time import sleep

#Prompting for username and password
line = printline()
print(line)
def scpfile(ip, username, passwd, sourc_file):
    try:
       global line
       print('\nUpload on: {}\n'.format(ip))
       Device = {'ip':ip,
                      'username':username,
                      'password':passwd,
                      'secret':'cisco', 
                      'device_type':'arista_eos',
                      'global_delay_factor':8
               }
       connection = ConnectHandler(**Device)
       connection.enable()
       transfer_dict = file_transfer(connection,
                                  source_file=sourc_file, 
                                  dest_file=sourc_file,
                                  file_system='/mnt/flash',
                                  socket_timeout=50.0 
                                  )
#Use increased session timeout to transfer larger files
#Printing results of transfer operation
       print("\nResults for {}".format(ip))
       sleep(0.5)
       para1 = transfer_dict['file_exists']
       para2 = transfer_dict['file_transferred']
       para3 = transfer_dict['file_verified']
       print("\nFile exists already:  {}".format(para1))
       sleep(0.5)
       print("\nFile transferred:  {}".format(para2))
       sleep(0.5)
       print("\nMD5 verified:  {}".format(para3))
#Disconnecting from the current device
       connection.disconnect() 
    except (AuthenticationException):
       print("Oops! Authentication fails    Try again....")
    except (NetMikoTimeoutException):
       print("Session timed out....Try again")



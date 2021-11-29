#! /usr/bin/python3
#Importing necesaary modules to call functions
from netmiko import ConnectHandler, file_transfer
from netmiko.ssh_exception import AuthenticationException
from netmiko.ssh_exception import NetMikoTimeoutException
from loguru import logger

class Scpfiletransfer:
    def __init__(self, ip, usern, passwd, filename):
        self.ip = ip
        self.usern = usern
        self.passwd = passwd
        self.filename = filename
        self.device_type = None
        self.file_system= None

    def cisco_ios(self):
        self.device_type = 'cisco_ios'
        self.file_system = 'flash:'

    def arista_eos(self):
        self.device_type = 'arista_eos'
        self.file_system = '/mnt/flash'

    def juniper_junos(self):
        self.device_type = 'juniper_junos'
        self.file_system = '/var/tmp'

    def connection(self):
        return ConnectHandler(ip=self.ip, username=self.usern, password=self.passwd, device_type=self.device_type, session_timeout=60)
    
    def sendfile(self, conn):
        return file_transfer(conn, source_file=self.filename, dest_file=self.filename, file_system=self.file_system)

#Instantiating object for cisco devices
def cisco(ip, usern, passwd, filename):
    try:
        p1 = Scpfiletransfer(ip, usern, passwd, filename)
        p1.cisco_ios()
        conn = p1.connection()
        send = p1.sendfile(conn)
        #print(conn.send_command('show ip int br'))
        logger.info(f"Image successfully uploaded on {ip}")
        conn.disconnect()

    except (AuthenticationException):
        print("Oops! Authentication fails    Try again....")
    except (NetMikoTimeoutException):
        print("Session timed out....Try again")

#Instantiating object for juniper devices
def juniper(ip, usern, passwd, filename):
    try:
        p1 = Scpfiletransfer(ip, usern, passwd, filename)
        p1.juniper_junos()
        conn = p1.connection()
        send = p1.sendfile(conn)
        #print(conn.send_command('sh int terse'))
        logger.info(f"Image successfully uploaded on {ip}")
        conn.disconnect()

    except (AuthenticationException):
        print("Oops! Authentication fails    Try again....")
    except (NetMikoTimeoutException):
        print("Session timed out....Try again")

#Instantiating object for arista devices
def arista(ip, usern, passwd, filename):
    try:
        p1 = Scpfiletransfer(ip, usern, passwd, filename)
        p1.arista_eos()
        conn = p1.connection()
        #print(conn.send_command('show ip int br'))
        send = p1.sendfile(conn)
        logger.info(f"Image successfully uploaded on {ip}")
        conn.disconnect()

    except (AuthenticationException):
        print("Oops! Authentication fails    Try again....")
    except (NetMikoTimeoutException):
        print("Session timed out....Try again")

#At the end, the main function encapsulates the core logic
def main():
    cisco()
    #nothing to mention here
if __name__ == "__main__":
    main()
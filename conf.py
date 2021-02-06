#Automating with Netmiko to verify device status and configs

#This script will connect to the three routers using ssh and will check this command 
#sh run 
#sh ip int br
#sh ip protocols


from typing import Dict, Union

from netmiko import ConnectHandler
import datetime



#hostname = input('Enter the Hostname of IP Address: ')
username = input("Enter username: ")
password = input('Enter the secret password: ')
secret = input('Enter the enable secret password: ')



router1 = {
            "device_type": 'cisco_ios',
            "ip": "192.168.122.254",
            "username": username,
            "password": password,
            "port": '22',
            "secret": secret,
            'verbose': True,
            }

router2 = {
            "device_type": 'cisco_ios',
            "ip": "192.168.122.252",
            "username": 'admin',
            "password": password,
            "port": '22',
            "secret": secret,
            'verbose': True,
            }

router3 = {
            "device_type": 'cisco_ios',
            "ip": "192.168.122.253",
            "username": 'admin',
            "password": password,
            "port": '22',
            "secret": secret,
            'verbose': True,
            }

routers = [router1, router2, router3]

for device in routers:

    net_connect = ConnectHandler(**device)
    prompt = net_connect.find_prompt()
    print(prompt)

    if not net_connect.check_enable_mode():
        net_connect.enable()
    print(prompt)

    output = net_connect.send_command('sh ip int br')
    print("=="*50)
    print(output)
    output = net_connect.send_command('sh ip protocols')
    print("==" * 50)
    print(output)
    output = net_connect.send_command('sh run')
    print("==" * 50)
    print(output)


    output = net_connect.find_prompt()

net_connect.disconnect()

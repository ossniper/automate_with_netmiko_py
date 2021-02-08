# This another method using Netmiko and json to Automate Network Device i.e Cisco_ios

# the routers details are saved in "devices.json". 

from netmiko import ConnectHandler

import json


with open('devices.json') as file:
    routers = json.load(file)

# routers = [router1, router2, router3]

for device in routers:
    net_connect = ConnectHandler(**device)

    net_connect.enable()
    prompt = net_connect.find_prompt()
    print(prompt)

    print("==" * 25)
    print('connecting to device')
    print(net_connect.send_command('sh ip int br'))
    print("==" * 25)
    print('connecting to device')
    print(net_connect.send_command('sh ip protocols'))
    print("==" * 25)
    print('connecting to device')
    print(net_connect.send_command('sh run'))
    print("==" * 50)

net_connect.disconnect()

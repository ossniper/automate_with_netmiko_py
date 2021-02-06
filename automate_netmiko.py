#You can change the details for each routers config . 
#The command was successful on the router and all command was sent and configure but i did get some error on pycharm instead of saying succesful, so i will work on it and give and update


from netmiko import ConnectHandler

from datetime import datetime

#I will be configuring this device.
#It will request for the ip address, username and passwords
# ospf will be configured and interface ip address to neighbouring routers

#device_type = 'cisco_ios'

hostname = input('Enter the Hostname of IP Address: ')  # will request for ip address
username = input('Enter the username: ')               # will request for username
password = input('Enter the secret password: ')       # will request for password
secret = input('Enter the enable secret password: ')

device = ConnectHandler(device_type='cisco_ios', ip=hostname, username=username, password=password, port = '22', secret=secret, verbose = True)
prompt = device.find_prompt()

if not device.check_enable_mode():
    device.enable()

prompt = device.find_prompt()

if not device.check_config_mode():
    device.config_mode()

print(prompt)


output = device.send_config_set("""router ospf 100
router-id 2.2.2.2
network 2.2.2.2
network 172.168.10.0 0.0.0.3
exit

int fastEthernet1/0
ip address 172.168.10.1 255.255.255.252
ip ospf 100 area 0
description P_router
no shut
do copy running-config startup-config
exit                            """)
print(output)
#it will send the config commands and exit config mode

device.exit_config_mode()
output = device.find_prompt()  #check prompt to see if router has exit config mode


output = device.find_prompt() #check prompt to verify mode
print(output)

print('closing connection')
device.disconnect()  # terminate connection

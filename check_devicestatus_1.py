# Automating with Netmiko to verify device status and configs

# This script will connect to the three routers using ssh and will check this commands :

# sh run 
# sh ip int br
# sh ip protocols




from netmiko import ConnectHandler



router1 = {
    "device_type": 'cisco_ios',
    "ip": "192.168.122.254",
    "username": 'root',
    "password": 'cisco',
    "port": '22',
    "secret": 'cisco',
    'verbose': True,
}

router2 = {
    "device_type": 'cisco_ios',
    "ip": "192.168.122.252",
    "username": 'admin',
    "password": 'cisco',
    "port": '22',
    "secret": 'cisco',
    'verbose': True,
}

router3 = {
    "device_type": 'cisco_ios',
    "ip": "192.168.122.253",
    "username": 'admin',
    "password": 'cisco',
    "port": '22',
    "secret": 'cisco',
    'verbose': True,
}

routers = [router1, router2, router3]

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


# in the next check_devicestatus_2.py will import the router details using of json

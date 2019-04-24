from netmiko import ConnectHandler

with open('commandsFile') as cf:
        commands_to_send = cf.read().splitlines()

with open('devicesFile') as df:
        devices_list = df.read().splitlines()

for device in devices_list:
        print 'connecting to device' + device
        ip_address_of_device = device

        ios_r = {
        'device_type':'cisco_ios',
        'ip':ip_address_of_device,
        'username':'cisco',
        'password':'cisco'
        }

        net_connect = ConnectHandler(**ios_r)  
        output = net_connect.send_config_set(commands_to_send)
        print(output)

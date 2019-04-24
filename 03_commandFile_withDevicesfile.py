from netmiko import ConnectHandler

# this file store a list of commands that is going to execute to all 
#devices that listed on the devicesFile
with open('commandsFile') as cf:
        commands_to_send = cf.read().splitlines()
# list of IP address of devices that we are going to run this scripts
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

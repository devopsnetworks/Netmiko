from netmiko import ConnectHandler

#The splitlines() returns a list of lines in the string.
with open('commandsFile') as cf:
	commands_to_send = cf.read().splitlines()

ios_r = {
        'device_type':'cisco_ios',
        'ip':'172.16.0.101',
        'username':'cisco',
        'password':'cisco'
}

net_connect = ConnectHandler(**ios_r)  
output = net_connect.send_config_set(commands_to_send)
print(output)

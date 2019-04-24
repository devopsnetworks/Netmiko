from netmiko import ConnectHandler

ios_r = {
        'device_type':'cisco_ios',
        'ip':'172.16.0.101',
        'username':'cisco',
        'password':'cisco'
}

net_connect = ConnectHandler(**ios_r) 
#send_command  use to send one command
#we can use multiple commands with send_config_set()
output = net_connect.send_command('show version')
print(output)

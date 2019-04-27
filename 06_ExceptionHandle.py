from getpass import getpass
from netmiko import ConnectHandler
from netmiko.ssh_exception import NetMikoTimeoutException # time out
from paramiko.ssh_exception import SSHException # SSH configuration mistake / not enable
from netmiko.ssh_exception import AuthenticationException # credential is not match

username = raw_input ('Enter your SSH username :')
password = getpass()

with open('commandsFile') as cf:
        commands_to_send = cf.read().splitlines()

with open('devicesFile') as df:
        devices_list = df.read().splitlines()

for device in devices_list:
        print 'connecting to device ' + device
        ip_address_of_device = device

        ios_r = {
        'device_type':'cisco_ios',
        'ip':ip_address_of_device,
        'username':username,
        'password':password
        }

        try:
          net_connect = ConnectHandler(**ios_r) 
        except(AuthenticationException): # username / password fail
          print 'Authentication failure ' + ip_address_of_device
          continue
        except(NetMikoTimeoutException): # interface / ip address is not reachable
          print 'Time out to device ' + ip_address_of_device
          continue
        except(EOFError):
          print 'End of file attempting to device ' +ip_address_of_device
          continue
        except(SSHException): # ssh configuration is not correct/ not enable
          print 'is SSH enabled ' + ip_address_of_device
          continue
        except Exception as unknoun_error:
          print 'Other errot' + unknoun_error
          continue

        net_connect = ConnectHandler(**ios_r)  
        output = net_connect.send_config_set(commands_to_send) 
        print(output)

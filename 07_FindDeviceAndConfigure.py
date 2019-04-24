from getpass import getpass
from netmiko import ConnectHandler
from netmiko.ssh_exception import NetMikoTimeoutException
from paramiko.ssh_exception import SSHException
from netmiko.ssh_exception import AuthenticationException

username = raw_input ('Enter your SSH username :')
password = getpass()

with open('commandsSwitch') as cf_s:
        commandsToSwitch = cf_s.read().splitlines()

with open('commandsRouter') as cf_r:
        commandsToRouter = cf_r.read().splitlines()


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


        list_versions = {
        'C7200-ADVENTERPRISEK9-M',
        'vios_l2-ADVENTERPRISEK9-M',
        }

        for software_ver in list_versions:
          print 'checking for version.... ' + software_ver
          output_version =  net_connect.send_command('show version')
          int_version = 0
          int_version = output_version.find(software_ver)

          if int_version > 0:
            print 'Software version is found ' + software_ver
            break
          else:
            print 'Software version is not found ' + software_ver

        if software_ver =='C7200-ADVENTERPRISEK9-M':
          print 'Running ' + software_ver + ' commands'
          output = net_connect.send_config_set(commandsToRouter)
          print(output)

        if software_ver =='vios_l2-ADVENTERPRISEK9-M':
          print 'Running ' + software_ver + ' commands'
          output = net_connect.send_config_set(commandsToSwitch)
          print(output)

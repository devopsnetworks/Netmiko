import json
from netmiko import ConnectHandler

#this file store a list of commands that is going to execute to all 
#devices that listed on the devicesFile
with open('commandsFile') as cf:
        commands_to_send = cf.read().splitlines()

with open('deviecCredential.json', mode="r") as file:
        jsonfile=json.loads(file.read()) # read as python dictioneary
        routers = jsonfile['router']
        switches = jsonfile['switch']
        devices_list = routers + switches
        noOfRouters = len(routers)
        noOfSwitches = len (switches)
        noOfDevices = len(devices_list)
        #print(routers)
        #print(switches)
        #print(devices_list)
        x = 0
        while (x < noOfDevices):
                ipOfDevice = devices_list[x]['ip']
                usernameOfDevice = devices_list[x]['username']
                passwordOfDevice = devices_list[x]['password']
               	print("""################################################################""")                                       
                print("""             CONNECTING TO DEVICE - """ + ipOfDevice )
                print("""################################################################ """)
                
                ios_r = {
                'device_type':'cisco_ios',
                'ip':ipOfDevice,
                'username':usernameOfDevice,
                'password':passwordOfDevice
                }
                net_connect = ConnectHandler(**ios_r)
                output = net_connect.send_config_set(commands_to_send)
                print(output)
                x = x+1

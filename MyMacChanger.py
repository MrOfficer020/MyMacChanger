ifconfig
ifconfig eth0 down
ifconfig eth0 hw ether 00:11:22:33:44:55
ifconfig eth0 up
ifconfig

ifconfig
ifconfig wlan0 down
ifconfig wlan0 hw ether 00:11:22:33:44:55
ifconfig wlan0 up
ifconfig

ifconfig
ifconfig wlan0 down
ifconfig wlan0 hw ether 00:11:22:33:44:55
ifconfig wlan0 up
ifconfig

ifconfig
ifconfig wlan0 down
ifconfig wlan0 hw ether 00:11:22:33:44:55
ifconfig wlan0 up
ifconfig

ifconfig
ifconfig wlan0 down
ifconfig wlan0 hw ether 00:11:22:33:44:55
ifconfig wlan0 up
ifconfig
import subprocess

print("MAC Changer Started")

subprocess.call(["ifconfig","eth0","down"])
subprocess.call(["ifconfig","eth0","hw","ether","00:11:22:33:44:55"])
subprocess.call(["ifconfig","eth0","up"])



import subprocess

print("Mac Changer Started My Baby")

subprocess.call(["ifconfig","eth0","down"])
subprocess.call(["ifconfig","eth0","hw","ether","00:11:22:33:44:55"])
subprocess.call(["ifconfig","eth0","up"])



import subprocess

print("Macchanger is working baby :-)")

subprocess.call(["ifconfig","eth0","down"])
subprocess.call(["ifconfig","eth0","hw","ether","00:11:22:33:44:55"])
subprocess.call(["ifconfig","eth0","up"])

import subprocess

print("Yes Heisenberg")

interface="eth0"
mac_adress="00:11:22:33:44:55:66"

subprocess.call(["ifconfig",interface,"down"])
subprocess.call(["ifconfig",interface,"hw","ether",mac_adress])
subprocess.call(["ifconfig",interface,"down"])












import subprocess
import optparse

parse_object=optparse.OptionParser()
parse_object.add_option("-i","--interface",dest="interface",help="help")
parse_object.add_option("-m","--mac",dest="mac_adress",help="helpp")

(user_inputs,arguments)=parse_object.parse_args()

user_interface=user_inputs.interface
user_mac_address=user_inputs.mac_adress

print("Mac Changer Started")

subprocess.call(["ifconfig",user_interface,"down"])
subprocess.call(["ifconfig",user_interface,"hw","ether",user_mac_address])
subprocess.call(["ifconfig",user_interface,"down"])







import subprocess
import optparse


parse_object=optparse.OptionParser()
parse_object.add_option("-i","--interface",dest="interface",help="Help")
parse_object.add_option("-m","--mac",dest="mac_adress",help="Helpp")

(user_inputs,arguments)=parse_object.parse_args()

me_interface=user_inputs.interface
me_mac_adress=user_inputs.mac_adress


print("Macchanger Started")

subprocess.call(["ifconfig",me_interface,"down"])
subprocess.call(["ifconfig",me_interface,"hw","ether",me_mac_adress])
subprocess.call(["ifconfig",me_interface,"up"])







import subprocess
import optparse

parse_object=optparse.OptionParser()
parse_object.add_option("-i","--interface",dest="interface",help="help")
parse_object.add_option("-m","--mac",dest="mac_adress",help="helpp")

(user_inputs,arguments)=parse_object.parse_args()

user_interface=user_inputs.interface
user_mac_address=user_inputs.mac_adress

print("Mac Changer Started")

subprocess.call(["ifconfig",user_interface,"down"])
subprocess.call(["ifconfig",user_interface,"hw","ether",user_mac_address])
subprocess.call(["ifconfig",user_interface,"down"])














import subprocess
import optparse


parse_object=optparse.OptionParser()
parse_object.add_option("-i","--interface",dest="interface",help="yes")
parse_object.add_option("-m","mac_adress",dest="mac_adress",help="no")

(user_inputs,arguments)=parse_object.parse_args()

interfacee=user_inputs.interface()
mac=user_inputs.mac()

print("Mac Changer Started")
subprocess.call(["ifconfig",interfacee,"down"])
subprocess.call(["ifconfig",interfacee,"hw","ether",mac])
subprocess.call(["ifconfig",interface,"up"])


































































































































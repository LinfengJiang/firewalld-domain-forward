import re
import subprocess

#Domain address
domain = ''
#TODO Check interval(seconds)
interval = 1
#TODO conf location
confLoc = '/'

#Use Ping to got ip address from domain
def getIP(d):
    IPadress = '0.0.0.0'
    subreturn = subprocess.Popen('ping %s -c 1' % (d), shell=True, universal_newlines=True, stdout=subprocess.PIPE)
    # subreturn = subprocess.Popen('ping %s -n 1' % (d), shell=True, universal_newlines=True, stdout=subprocess.PIPE)
    subreturn.wait(2)
    if subreturn.poll() == 0:
        tmp = subreturn.stdout.read()
        IPadress =re.search(r'(([01]{0,1}\d{0,1}\d|2[0-4]\d|25[0-5])\.){3}([01]{0,1}\d{0,1}\d|2[0-4]\d|25[0-5])',tmp)
        IPadress = IPadress.group()
    else:
        print('Error')
    print(IPadress)
    return(IPadress)

IPaddr = getIP(domain)

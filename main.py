import re
import subprocess

#Domain address
domain = 'test.com'
#Port
port = 5000
#TODO Check interval(seconds)
interval = 1
#conf location
confLoc = '/etc/firewalld/zones/public.xml'

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

def replacer(match):
    return re.sub(r'to-addr="[^"]*"', 'to-addr="%s"' % (getIP(domain)), match.group(0))

#Writing to conf file
def confWirting(p):
    with open(confLoc,'r') as f:
        tmp = f.read()
        new_tmp = re.sub(r'<forward-port [^>]*port="%s"[^>]*>' % (p), replacer, tmp)
        print(new_tmp)

    #Rename old file
    subp = subprocess.Popen('mv %s %s -f' % (confLoc,confLoc+'bak'),shell=True)
    subp.wait(2)
    if subp.poll() == 0:
        print(subp.communicate()[1])
    else:
        print("Error by rename File")

    with open(confLoc,'w') as f:
        f.write(new_tmp)

confWirting(port)
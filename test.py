import re

port = 5000

text = '''<forward-port to-addr="222.187.222.78" to-port="10001" protocol="udp" port="25564"/>
<forward-port to-addr="222.187.222.78" to-port="5000" protocol="tcp" port="5000"/>
<forward-port to-addr="222.187.222.78" to-port="5000" protocol="udp" port="5000"/>'''

def replacer(match):
    return re.sub(r'to-addr="[^"]*"', 'to-addr="0.0.0.0"', match.group(0))

new_text = re.sub(r'<forward-port [^>]*port="%s"[^>]*>' % (port), replacer, text)

print(new_text)

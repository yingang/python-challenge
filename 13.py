import urllib.request
import xmlrpc.client

# list available methods
with xmlrpc.client.ServerProxy("http://www.pythonchallenge.com/pc/phonebook.php") as proxy:
    print(proxy.system.listMethods())

# check the 'phone' method in detail
with xmlrpc.client.ServerProxy("http://www.pythonchallenge.com/pc/phonebook.php") as proxy:
    print(proxy.system.methodHelp('phone'))
    print(proxy.system.methodSignature('phone'))

# find out devil name
pwmgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()
pwmgr.add_password(None, "http://www.pythonchallenge.com", "huge", "file")
auth_handler = urllib.request.HTTPBasicAuthHandler(pwmgr)
opener = urllib.request.build_opener(auth_handler)
urllib.request.install_opener(opener)

with urllib.request.urlopen("http://www.pythonchallenge.com/pc/return/evil4.jpg") as f:
    print(f.read().decode("utf-8"))

# phone that devil!
with xmlrpc.client.ServerProxy("http://www.pythonchallenge.com/pc/phonebook.php") as proxy:
    print(proxy.phone("Bert"))

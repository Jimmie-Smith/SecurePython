import subprocess

# Here we're just making the code more secure from hijacking!
# The syntax is correct in either scenario though

def changeMAC(config, address):
    if not config:
        print('please specify the interface you want to connect to')
        return False
    elif not address:
        print('please specify the address you want to change to')
        return False
    else:
        # subprocess.call('ifconfig ' + config + ' down', shell=True)
        subprocess.call(['ifconfig', config, 'down'])
        # subprocess.call('ifconfig ' + config + ' hw ether ' + address, shell=True)
        subprocess.call(['ifconfig', config, 'hw', 'ether', address])
        # subprocess.call('ifconfig ' + config + ' up', shell=True)
        subprocess.call(['ifconfig', config, 'up'])
        # subprocess.call('ifconfig ', shell=True)
        print('Address successfully changed to ' +
        address + ' for ' + config + '!')
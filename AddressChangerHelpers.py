import subprocess
import filter
import updateChecker
# Here we're just making the code more secure from hijacking!
# The syntax is correct in either scenario though


def changeMAC(config, address):
    if not config:
        print('please specify the interface you want to connect to. use --help for more information')
        return False
    elif not address:
        print('please specify the address you want to change to. use --help for more information')
        return False
    else:
        old_mac = subprocess.check_output(
            ['ifconfig', config]).decode('utf8')
        filtered_old_mac = filter.filter_results(old_mac)
        # subprocess.call('ifconfig ' + config + ' down', shell=True)
        subprocess.call(['ifconfig', config, 'down'])
        # subprocess.call('ifconfig ' + config + ' hw ether ' + address, shell=True)
        subprocess.call(['ifconfig', config, 'hw', 'ether', address])
        # subprocess.call('ifconfig ' + config + ' up', shell=True)
        subprocess.call(['ifconfig', config, 'up'])
        # Algorithm starts here to check if the address is changed.
        result = subprocess.check_output(['ifconfig', config]).decode('utf-8')
        # We filter results and error check for no available address
        filtered_new_mac = filter.filter_results(result)
        # check if the address is changed
        updateChecker.update_checker(filtered_old_mac, filtered_new_mac)


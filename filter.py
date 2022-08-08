import re

def filter_results(output):
    filtered_MAC = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", output)

    if filtered_MAC:
        # then we filter the results for just the new MAC address
        # subprocess.call('ifconfig ', shell=True)
        return filtered_MAC.group(0)
    else:
        print("Sorry, the MAC address is not available for this interface")

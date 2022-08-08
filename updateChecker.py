def update_checker(old_mac_address, new_mac_address):
    if old_mac_address == new_mac_address:
        print(f'MAC address failed to change to: {new_mac_address} because you currently have: {old_mac_address}! Please pick a new address')
    else:
        print(f'MAC address successfully changed to: {new_mac_address} from: {old_mac_address}!')

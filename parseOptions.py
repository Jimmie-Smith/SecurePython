import optparse


parser = optparse.OptionParser()

parser.add_option('-c', "--config", dest="config",
                  help="Type in the interface in which you want to change the MAC address. You can see what's running by using the ifconfig command")
parser.add_option("-a", "--address", dest="address",
                  help="Type in the MAC address that you want to change to. \'00:11:22:33:44:55\' for example")

(options, args) = parser.parse_args()

config = options.config
address = options.address
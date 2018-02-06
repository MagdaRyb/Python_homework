import re

# regex patterns for address and mask
address_pattern = re.compile(
    "^((\d|[1-9]\d|1\d{2}|2[0-4]\d|25[0-5])\.){3}(\d|[1-9]\d|1\d{2}|2[0-4]\d|25[0-5])$"
)
mask_pattern = re.compile("^/(\d|[12]\d|3[0-2])$")

# loading address from input
while True:
    address = raw_input("Enter Ip address: ")
    if re.search(address_pattern, address.strip()):
        break
    else:
        print "Invalid IP address format"

# loading mask from input
while True:
    mask = raw_input("Enter subnet mask in decimal format: ")
    if re.search(mask_pattern, mask.strip()):
        break
    else:
        print "Subnet mask is invalid"

# preparing address for printing in decimal and binary format
address_splitted = address.split('.')
print '{0:>10} {1:>10} {2:>10} {3:>10}'.format(address_splitted[0], address_splitted[1],
                                               address_splitted[2], address_splitted[3])
address_binary = ["{0:08b}".format(int(add)) for add in address_splitted]
print '{0:>10} {1:>10} {2:>10} {3:>10}'.format(address_binary[0], address_binary[1],
                                               address_binary[2], address_binary[3])

# calculations for network and broadcast addresses
mask_decimal = int(mask[1:])
mask_binary = '1' * mask_decimal + '0' * (32 - mask_decimal)
mask_binary = [mask_binary[8 * i:8 * (i + 1)] for i in range(4)]

network_address = [int(address_splitted[i]) & int(mask_binary[i], 2) for i in range(4)]

broadcast_address = ''.join(address_binary)[:mask_decimal] + '1' * (32 - mask_decimal)
broadcast_address = [int(broadcast_address[8 * i:8 * (i + 1)], 2) for i in range(4)]

print "network address is: {}.{}.{}.{}{}".format(network_address[0], network_address[1],
                                                 network_address[2], network_address[3], mask)
print "broadcast address is: {}.{}.{}.{}{}".format(broadcast_address[0], broadcast_address[1],
                                                   broadcast_address[2], broadcast_address[3], mask)

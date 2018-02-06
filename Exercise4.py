access_template = ['switchport mode access',
                   'switchport access vlan {}',
                   'switchport nonegotiate',
                   'spanning-tree portfast',
                   'spanning-tree bpduguard enable']

trunk_template = ['switchport trunk encapsulation dot1q',
                  'switchport mode trunk',
                  'switchport trunk allowed vlan {}']

templates = {'access': [access_template, 'Enter VLAN number: '], 'trunk': [trunk_template, 'Enter allowed VLANs: ']}

# collecting information from user
while True:
    mode = raw_input('Enter interface mode (access/trunk):')
    if mode in ['access', 'trunk']:
        break
    else:
        print 'Invalid input'
interface = raw_input('Enter interface type and number: ')
vlan = raw_input(templates[mode][1])

# printing as in corresponding template
print 'Interface ' + interface
for command in templates[mode][0]:
    print command.format(vlan)

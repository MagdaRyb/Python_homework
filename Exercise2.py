import re
from collections import Counter

command_to_search = "switchport trunk allowed vlan"
command_pattern = "(" + command_to_search + ").*"

f = open("commands.txt", "r")
commands = (f.read()).split("\n")
f.close()

# searching for valid lines
valid_commands = [re.match(command_pattern, command).string.strip() for command in commands
                  if re.search(command_pattern, command)]

# separating vlans from the rest of the command statement
vlans = [valid_command[len(command_to_search) + 1:].replace(' ', '').split(',') for valid_command in valid_commands]

List_1 = []
List_2 = []
# splitting to conditions to avoid errors due to vlans list length
if len(vlans) == 1:
    List_1 = sorted(set(vlans[0]), key=int)
    List_2 = sorted(set(vlans[0]), key=int)
elif len(vlans) > 1:
    List_1 = sorted(list(set.intersection(*map(set, vlans))), key=int)
    count = Counter([y for x in vlans for y in x])
    List_2 = sorted([key for key, value in count.iteritems() if value == 1], key=int)

print "List_1={}".format(List_1)
print "List_2={}".format(List_2)

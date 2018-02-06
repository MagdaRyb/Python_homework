import re

f = open("ShowIpRoute.txt", "r")
commands = (f.read()).split("\n")
f.close()

# pattern to search only for dynamic routing protocols
pattern = "^[RDEOINisL].*via"
valid_lines = [re.match(pattern, command).string.strip() for command in commands
               if re.search(pattern, command)]

protocols = {'R': 'RIP', 'D': 'EIGRP', 'EX': 'EIGRP external', 'O': 'OSPF', 'IA': 'OSPF inter area',
             'N1': ' NSSA external type 1', 'N2': ' NSSA external type 2', 'E1': ' external type 1',
             'E2': ' external type 2', 'E': 'EGP', 'i': 'IS-IS', 'su': ' summary', 'L1': ' level-1',
             'L2': ' level-2', 'ia': ' inter area'}

for line in valid_lines:

    # preparing information
    line = line.replace(',', '')
    line_splitted = re.split('\s+', line)
    if line_splitted[-7] == line_splitted[0]:
        protocol = protocols[line_splitted[0]]
    else:
        protocol = protocols[line_splitted[0]] + protocols[line_splitted[1]]
    prefix = line_splitted[-6]
    metric = line_splitted[-5][1:-1]
    next_hop = line_splitted[-3]
    last_update = line_splitted[-2]
    interface = line_splitted[-1]

    # suitable printing
    print('Protocol:            {}\n'
          'Prefix:              {}\n'
          'AD/Metric:           {}\n'
          'Next-Hop:            {}\n'
          'Last Update:         {}\n'
          'Outbound interface:  {}\n').format(protocol, prefix, metric, next_hop, last_update, interface)

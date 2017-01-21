def length(variable):
    return ('00000'+str(len(str(variable))))[-5:]
print('When you are required to enter a list of items with an unidentified amount of items, there will be [L]'
      'next to the request. When you are done entering all items just press enter without typing anything.')
map_name = input('Name of map[1](including the extension): ')
print("Enter the id's of all nodes[L]")
nodes = []
while True:
    Uinput = input()
    if Uinput == '':
        break
    nodes.append(Uinput)
connections = {}
for i in nodes:
    print('Connections with node %s[L]:' % i)
    while True:
        Uinput = input()
        if Uinput == '':
            break
        try:
            connections[i].add(Uinput)
        except KeyError:
            connections[i] = {Uinput}
names = {}
for i in nodes:
    names[i] = input('Enter the name of node %s[1]: ' % i)
content = {}
for i in nodes:
    print('Enter the content of node %s[L](multi line)' % i)
    temp_list = []
    while True:
        Uinput = input()
        if Uinput == '':
            content[i] = '\n'.join(temp_list)
            break
        temp_list.append(Uinput)
end_node = input('End node[1]:')

input('Press enter to make the map into a file.')
file = open(map_name, 'w')
file.write(end_node + '\n')
file.write(length(connections))
file.write(str(connections))
file.write(length(names))
file.write(str(names))
file.write(length(content))
file.write(str(content))
"everything to file"

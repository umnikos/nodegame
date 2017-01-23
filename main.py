import time
import os
import node_system

clearing = False
try:
    file_name = input('Enter name of file map:')
    if '.' not in file_name:
        file_name += '.txt'
    file = open(file_name, 'r')
    end_node = file.read(2)
    file.read(1)
    length = int(file.read(5))
    connections = eval(file.read(length))
    file.read(1)
    length = int(file.read(5))
    names = eval(file.read(length))
    file.read(1)
    length = int(file.read(5))
    content = eval(file.read(length))
    file.read(1)
    length = int(file.read(5))
    connect_points = eval(file.read(length))
    try:
        connections[end_node]
    except KeyError:
        connections[end_node] = set()
    loaded_map = node_system.Nodes(connections, names, content, connect_points)
    last_command = '>>%s\n\n' % file_name
    if not clearing:
        os.system('cls')
    while True:
        if clearing:
            os.system('cls')
            print(last_command, end='')
        loaded_map.print_info('current')
        command = input('>>')
        last_command = ('>>%s\n\n' % command)
        if command == 'exit':
            break
        elif command[:5] == 'link ':
            loaded_map.link(command[5:])
        elif command[:7] == 'unlink ':
            loaded_map.unlink(command[7:])
        else:
            node = command
            if node == end_node:
                if loaded_map.connect(node):
                    end_message = content[end_node].split('\n')
                    for _ in range(10):
                        print('')
                        time.sleep(1)
                    for _ in end_message:
                        print(_)
                        time.sleep(1)
                        print('')
                        time.sleep(1)
                    while True:
                        print('')
                        time.sleep(1.5)
            else:
                loaded_map.connect(node)
except NameError:
    input('The file you entered is invalid. Press enter to continue.')
except FileNotFoundError:
    input("We couldn't find a file with the name you entered. Press enter to continue.")

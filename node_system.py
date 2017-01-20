
class Nodes:
    list_connect_points = {}
    current_node = '00'

    def __init__(self, connections, names, content):
        self.list_connections = connections
        self.list_names = names
        self.list_content = content

    def print_info(self, node_id):
        if node_id == 'current':
            node_id = self.current_node
        node_id = str(node_id)
        print('Node %s:\n' % node_id)
        try:
            print('Connection points: %s' % self.list_connect_points[node_id])
        except KeyError:
            print('Connection points: 0')
        print('Name: %s' % self.list_names[node_id])
        print('Content:\n')
        print(self.list_content[node_id])
        print('\nLinked nodes:\n')
        try:
            for i in self.list_connections[node_id]:
                print('%s : %s' % (i, self.list_names[i]))
        except KeyError:
            print('Something went wrong on the map makers side...')
        print('')

    def connect(self, node_id):
        try:
            int(node_id)
        except ValueError:
            return False
        if not len(node_id) == 2:
            return False
        if (self.current_node[0] == node_id[0]) or (self.current_node[1] == node_id[1]):
            self.current_node = node_id
            return True
        return False

    def link(self):
        pass

    def unlink(self):
        pass

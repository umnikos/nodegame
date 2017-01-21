
class Nodes:
    current_node = '00'

    def __init__(self, connections, names, content, connect_points):
        self.list_connections = connections
        self.list_names = names
        self.list_content = content
        self.list_connect_points = connect_points

    def print_info(self, node_id):
        if node_id == 'current':
            node_id = self.current_node
        node_id = str(node_id)
        print('Node %s:\n' % node_id)
        try:
            print('Open ports: %s' % self.list_connect_points[node_id])
        except KeyError:
            print('Open ports: 0')
        print('Name: %s' % self.list_names[node_id])
        print('Content:\n')
        print(self.list_content[node_id])
        print('\nLinked nodes:\n')
        try:
            for i in self.list_connections[node_id]:
                print('%s : %s' % (str(i), str(self.list_names[i])))
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

    def link(self, node_id):
        node_id = str(node_id)
        try:
            if self.list_connect_points[node_id] >= 1:
                if self.list_connect_points[self.current_node] >= 1:
                    if node_id[0] == self.current_node[0] or node_id[1] == self.current_node[1]:
                        self.list_connections[node_id].add(self.current_node)
                        self.list_connections[self.current_node].add(node_id)
                        self.list_connect_points[node_id] -= 1
                        self.list_connect_points[self.current_node] -= 1
        except KeyError:
            pass

    def unlink(self, node_id):
        node_id = str(node_id)
        try:
            if node_id in self.list_connections[self.current_node]:
                if self.current_node in self.list_connections[node_id]:
                    self.list_connections[node_id].remove(self.current_node)
                    self.list_connections[self.current_node].remove(node_id)
                    self.list_connect_points[node_id] += 1
                    self.list_connect_points[self.current_node] += 1
        except KeyError:
            pass

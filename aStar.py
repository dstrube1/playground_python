import networkx as nx
from explorable_graph import ExplorableGraph
from queue import PriorityQueue
import math

def euclidean_dist_heuristic(graph, v, goal):
    """
    Args:
        graph (ExplorableGraph): Undirected graph to search.
        v (str): Key for the node to calculate from.
        goal (str): Key for the end node to calculate to.

    Returns:
        Euclidean distance between `v` node and `goal` node
    """

    if v == goal:
        return 0

    if v not in graph or goal not in graph:
        return -1

    keys = graph.nodes()[v].keys()

    if 'pos' in keys:
        key = 'pos'
    elif 'position' in keys:
        key = 'position'
    else:
        return 0

    node_1 = graph.nodes()[v][key]
    node_2 = graph.nodes()[goal][key]
    dx = node_2[0] - node_1[0]
    dy = node_2[1] - node_1[1]
    dx = math.pow(dx, 2)
    dy = math.pow(dy, 2)
    return int(math.sqrt(dx + dy))


def a_star(graph, start, goal, heuristic=euclidean_dist_heuristic):
    """
    Args:
        graph (ExplorableGraph): Undirected graph to search.
        start (str): Key for the start node.
        goal (str): Key for the end node.
        heuristic: Function to determine distance heuristic.
            Default: euclidean_dist_heuristic.

    Returns:
        The best path as a list from the start and goal nodes (including both).
    """

    if start == goal:
        return []
    elif start not in graph.nodes:
        pass
        # return []
    elif goal not in graph.nodes:
        return []

    # Would've been nice to know sooner that we're not supposed to reset the graph -_-
    # graph.reset_search()

    node = (heuristic(graph, start, goal), 0, start, None)

    frontier = PriorityQueue()
    explored = set()

    frontier.put(node)

    while not frontier.empty():
        node = frontier.get()
        if node[2] == goal:
            path_list = [node[2]]
            temp_node = node[3]
            while temp_node:
                path_list.append(temp_node[2])
                temp_node = temp_node[3]
            path_list.reverse()
            return path_list

        nodes = graph.nodes()
        # for n in nodes:
        #    print("n: " + str(n))
        children = nodes[node[2]]
        explored.add(node[2])

        for child in children:
            if child not in explored:
                f = (node[1] + children[child]['weight']) + heuristic(graph, child, goal)
                child_node = (f, (node[1] + children[child]['weight']), child, node)
                frontier.put(child_node)
                if child_node == 'Serbankia':
                    print("Added Serbankia")
    # not found
    return []


class City:
    def __init__(self, name):
        self.name = name
        self.coords = (0, 0)

    def __repr__(self):
        return self.name


def get_city_list():
    city_list = []

    temp_city = City('Isbelland')
    temp_city.coords = (220.2, 382.1)
    city_list.append(temp_city)

    temp_city = City('Pandel')
    temp_city.coords = (154.5, 350.4)
    city_list.append(temp_city)

    temp_city = City('Thrunway')
    temp_city.coords = (360.4, 323.2)
    city_list.append(temp_city)

    temp_city = City('Joyneria')
    temp_city.coords = (248.3, 287.1)
    city_list.append(temp_city)

    temp_city = City('Norvigden')
    temp_city.coords = (148.7, 240.5)
    city_list.append(temp_city)

    temp_city = City('Howardan')
    temp_city.coords = (87.5, 300.5)
    city_list.append(temp_city)

    temp_city = City('Littmania')
    temp_city.coords = (63.2, 211.7)
    city_list.append(temp_city)

    temp_city = City('Bobickstan')
    temp_city.coords = (111.3, 132.6)
    city_list.append(temp_city)

    temp_city = City('Essastan')
    temp_city.coords = (182.9, 92.0)
    city_list.append(temp_city)

    temp_city = City('Serbankia')
    temp_city.coords = (206.0, 178.6)
    city_list.append(temp_city)

    temp_city = City('Balchea')
    temp_city.coords = (365.3, 185.6)
    city_list.append(temp_city)

    temp_city = City('Starneria')
    temp_city.coords = (246.4, 49.3)
    city_list.append(temp_city)
    
    return city_list


def get_edge_list():
    edge_list = []
    edge_list.append(('Isbelland', 'Pandel'))
    edge_list.append(('Isbelland', 'Thrunway'))

    edge_list.append(('Pandel', 'Isbelland'))
    edge_list.append(('Pandel', 'Serbankia'))
    edge_list.append(('Pandel', 'Howardan'))

    edge_list.append(('Thrunway', 'Isbelland'))
    edge_list.append(('Thrunway', 'Serbankia'))
    edge_list.append(('Thrunway', 'Balchea'))

    edge_list.append(('Joyneria', 'Balchea'))
    edge_list.append(('Joyneria', 'Starneria'))

    edge_list.append(('Norvigden', 'Serbankia'))
    edge_list.append(('Norvigden', 'Bobickstan'))

    edge_list.append(('Howardan', 'Pandel'))
    edge_list.append(('Howardan', 'Littmania'))

    edge_list.append(('Littmania', 'Howardan'))
    edge_list.append(('Littmania', 'Bobickstan'))

    edge_list.append(('Bobickstan', 'Littmania'))
    edge_list.append(('Bobickstan', 'Norvigden'))
    edge_list.append(('Bobickstan', 'Essastan'))

    edge_list.append(('Essastan', 'Bobickstan'))
    edge_list.append(('Essastan', 'Starneria'))

    edge_list.append(('Serbankia', 'Thrunway'))
    edge_list.append(('Serbankia', 'Pandel'))
    edge_list.append(('Serbankia', 'Norvigden'))

    edge_list.append(('Balchea', 'Thrunway'))
    edge_list.append(('Balchea', 'Joyneria'))

    edge_list.append(('Starneria', 'Essastan'))
    edge_list.append(('Starneria', 'Joyneria'))

    return edge_list


city_list = get_city_list()
edge_list = get_edge_list()
graph = nx.Graph() 
# graph.add_nodes_from(city_list)
graph.add_edges_from(edge_list)
result = a_star(graph, 'Isbelland', 'Starneria')
print(result)

#TODO This is still a work in progress
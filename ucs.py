# Uniform cost search for practice test question

# Starting from here:
# https://gist.github.com/professormahi/cff4bfeaece05966e688658127bf41f3

from queue import PriorityQueue
import networkx
from explorable_graph import ExplorableGraph


def ucs_weight(from_node, to_node, weights=None):
    """
    Returns the UCS weight for a edge between from and to
    Assumption: There is no edge with weight >= float("inf") 
    :param from_node: The node edge starts from
    :param to_node: The node edge ends to
    :param weights: Dictionary of weights; maps `(from, to) -> weight`
    :return: Returns the weight of edge between from and to.
    """
    return weights.get((from_node, to_node), float("inf")) if weights else 1


def ucs(graph, start, end, weights=None):
    """
    Function to compute UCS(Uniform Cost Search) for a graph
    :param graph: The graph to compute UCS for
    :param start: start node
    :param end: end node
    :param weights: A dictionary of weights; maps (start_node, end_node) -> weight
    """
    frontier = PriorityQueue()
    frontier.put((0, start))  # (priority, node)
    explored = []
    budget = 10_000
    #prev_node = "[start]"

    while True:
        if frontier.empty():
            raise Exception("No way Exception")

        ucs_w, current_node = frontier.get()
        toll = budget * ucs_w
        budget -= toll
        budget = round(budget, 6)
        #print()
        #print("Exploring " + prev_node + " -> " + current_node)
        print("Exploring " + current_node + "; weight = " + str(round(ucs_w, 4))) 
        #prev_node = current_node
        explored.append(current_node)

        if current_node == end:
            print("Found goal.")
            path_list = [current_node]
            #temp_node = node[2]
            #while temp_node:
            #    path_list.append(temp_node[1])
            #    temp_node = temp_node[2]
            #path_list.reverse()
            #return path_list
            return

        for node in graph[current_node]:
            if node not in explored:
                print("Adding " + node + " to the frontier")
                frontier.put((
                    ucs_w + ucs_weight(current_node, node, weights),
                    node
                ))


def get_budget_from_goal(budget, goal):
    # print("goal: " + str(goal) + "; budget: " + str(budget))
    if goal[2] is not None:
        budget = get_budget_from_goal(budget, goal[2])
        weight = round(goal[0] - goal[2][0], 4)
        toll = budget * weight
        budget -= toll
        return budget
    else:
        toll = budget * goal[0]
        budget -= toll
        return budget


def uniform_cost_search(graph, start, goal):
    """
    Args:
        graph (ExplorableGraph): Undirected graph to search.
        start (str): Key for the start node.
        goal (str): Key for the end node.

    Returns:
        The best path as a list from the start and goal nodes (including both).
    """

    if start == goal or start not in graph.nodes or goal not in graph.nodes:
        return []

    graph.reset_search()

    node = (0, start, None)
    frontier = PriorityQueue()
    frontier.put(node)
    explored = set()
    budget = 10_000

    while not frontier.empty():
        node = frontier.get()
        
        if node[1] == goal:
            path_list = [node[1]]
            temp_node = node[2]
            
            # print("node[1]: " + node[1] + "; node[0]: " + str(node[0]) + "; node[2]: " + str(node[2]))
            budget = get_budget_from_goal(budget, node[2])
            weight = node[0] - node[2][0]
            toll = budget * weight
            budget -= toll
            
            while temp_node:
                path_list.append(temp_node[1])
                temp_node = temp_node[2]
            # print("path_list[0] before reverse: " + path_list[0])
            path_list.reverse()
            # print("path_list[0] after reverse: " + path_list[0])
            print("budget: " + str(round(budget, 6)))
            return path_list
            
        explored.add(node[1])
        children = graph[node[1]]
        for child in children:
            if child not in explored:
                h = node[0] + children[child]['weight']
                child_node = (h, child, node)
                frontier.put(child_node)
    # not found
    return []


ucs_test_graph = {
     'ISBL': ['STNR', 'INR', 'UGX', 'TRY'],
     'INR': ['ISBL', 'CNY', 'AUD'],
     'UGX': ['ISBL', 'CNY', 'AUD'],
     'TRY': ['ISBL', 'CNY', 'AUD'],
     'CNY': ['INR', 'UGX', 'TRY', 'EUR', 'GBP'],
     'AUD': ['TRY', 'UGX', 'INR', 'GBP', 'EUR', 'BTC'],
     'EUR': ['AUD', 'CNY', 'STNR'],
     'GBP': ['AUD', 'CNY', 'STNR'],
     'BTC': ['AUD', 'STNR'],
     'STNR': ['ISBL', 'GBP', 'EUR', 'BTC']
     
}

ucs_test_weight = {
     ('ISBL', 'STNR'): 0.99,
     ('ISBL', 'INR'): 0.0847, 
     ('ISBL', 'UGX'): 0.01, 
     ('ISBL', 'TRY'): 0.0124,

     ('INR', 'ISBL'): 0.0847, 
     ('INR', 'CNY'): 0.04, 
     ('INR', 'AUD'): 0.026,

     ('UGX', 'ISBL'): 0.01, 
     ('UGX', 'CNY'): 0.0892, 
     ('UGX', 'AUD'): 0.0023,

     ('TRY', 'ISBL'): 0.0124, 
     ('TRY', 'CNY'): 0.017, 
     ('TRY', 'AUD'): 0.0621,

     ('CNY', 'INR'): 0.04, 
     ('CNY', 'UGX'): 0.0892, 
     ('CNY', 'TRY'): 0.017, 
     ('CNY', 'EUR'): 0.012, 
     ('CNY', 'GBP'): 0.0571,

     ('AUD', 'TRY'): 0.0621, 
     ('AUD', 'UGX'): 0.0023, 
     ('AUD', 'INR'): 0.026,
     ('AUD', 'GBP'): 0.0493, 
     ('AUD', 'EUR'): 0.065, 
     ('AUD', 'BTC'): 0.005,

     ('EUR', 'AUD'): 0.065, 
     ('EUR', 'CNY'): 0.012, 
     ('EUR', 'STNR'): 0.0465,

     ('GBP', 'AUD'): 0.0493, 
     ('GBP', 'CNY'): 0.0571, 
     ('GBP', 'STNR'): 0.0645,

     ('BTC', 'AUD'): 0.005, 
     ('BTC', 'STNR'): 0.061,

     ('STNR', 'ISBL'): 0.99, 
     ('STNR', 'GBP'): 0.0645, 
     ('STNR', 'EUR'): 0.0465, 
     ('STNR', 'BTC'): 0.0610
}

weighted_edges = [
     ('ISBL', 'STNR', 0.99),
     ('ISBL', 'INR', 0.0847), 
     ('ISBL', 'UGX', 0.01), 
     ('ISBL', 'TRY', 0.0124),

     ('INR', 'ISBL', 0.0847), 
     ('INR', 'CNY', 0.04), 
     ('INR', 'AUD', 0.026),

     ('UGX', 'ISBL', 0.01), 
     ('UGX', 'CNY', 0.0892), 
     ('UGX', 'AUD', 0.0023),

     ('TRY', 'ISBL', 0.0124), 
     ('TRY', 'CNY', 0.017), 
     ('TRY', 'AUD', 0.0621),

     ('CNY', 'INR', 0.04), 
     ('CNY', 'UGX', 0.0892), 
     ('CNY', 'TRY', 0.017), 
     ('CNY', 'EUR', 0.012), 
     ('CNY', 'GBP', 0.0571),

     ('AUD', 'TRY', 0.0621), 
     ('AUD', 'UGX', 0.0023), 
     ('AUD', 'INR', 0.026),
     ('AUD', 'GBP', 0.0493), 
     ('AUD', 'EUR', 0.065), 
     ('AUD', 'BTC', 0.005),

     ('EUR', 'AUD', 0.065), 
     ('EUR', 'CNY', 0.012), 
     ('EUR', 'STNR', 0.0465),

     ('GBP', 'AUD', 0.0493), 
     ('GBP', 'CNY', 0.0571), 
     ('GBP', 'STNR', 0.0645),

     ('BTC', 'AUD', 0.005), 
     ('BTC', 'STNR', 0.061),

     ('STNR', 'ISBL', 0.99), 
     ('STNR', 'GBP', 0.0645), 
     ('STNR', 'EUR', 0.0465), 
     ('STNR', 'BTC', 0.0610)
]

# ucs(ucs_test_graph, 'ISBL', 'STNR', ucs_test_weight)

graph = networkx.Graph()
# https://networkx.org/documentation/networkx-1.0/tutorial/tutorial.html
graph.add_weighted_edges_from(weighted_edges)
e_graph = ExplorableGraph(graph)
result = uniform_cost_search(e_graph, 'ISBL', 'STNR')
print(result)

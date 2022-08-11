# alphabeta.py

import networkx

# from explorable_graph import ExplorableGraph


def alphabeta(node, parent, depth, alpha=float("-inf"), beta=float("inf"), maximizing=True):
    """Implementation of the alphabeta algorithm.

    Args:
        node: Directed graph
        parent: parent node
        depth: Used to track how deep you are in the search tree
        alpha (float): Alpha for pruning
        beta (float): Beta for pruning
        maximizing (bool): True if you are computing scores during your turn.

    Returns:
        integer value, or None
    """
    children = node[parent]

    # Extracted from Assignment 2 of CS 6601, rewritten from this:
    # https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning#Pseudocode
    if depth == 0:
        numbers = list()
        for child in children:
            # Verbose code is easier to debug
            number = int(child)
            numbers.append(number)
        if maximizing:
            maximum = max(numbers)
            return maximum
        else:
            minimum = min(numbers)
            return minimum
    elif len(children) == 0:
        if node[parent].isnumeric():
            number = int(node[parent])
            return number
        else:
            return None
    if maximizing:
        for child in children:
            temp_val = alphabeta(node, child, depth-1, alpha, beta, not maximizing)
            if temp_val > alpha:
                alpha = temp_val
            if beta <= alpha:
                print("Where children are ")
                print(children)
                print("prune where beta <= " + str(beta) + ", ie, after child " + child)
                break
        return alpha
    else:
        for child in children:
            temp_val = alphabeta(node, child, depth-1, alpha, beta, not maximizing)
            if temp_val < beta:
                beta = temp_val
            if beta <= alpha:
                print("Where children are ")
                print(children)
                print("prune where beta <= " + str(beta) + ", ie, after child " + child)
                break
        return beta
    
def alphabeta_nd(node, parent, depth, alpha=float("-inf"), beta=float("inf"), maximizing=True):
    # Like alphabeta, but non-deterministic
    pass


graph = networkx.DiGraph()
midterm_sample_edges = [  # depth = 4, call alphabeta with 2
    ('a', 'b'), ('a', 'c'), ('a', 'd'),
    ('b', 'e'), ('b', 'f'), ('b', 'g'),
    ('c', 'h'), ('c', 'i'), ('c', 'j'),
    ('d', 'k'), ('d', 'L'), ('d', 'm'),
    ('e', '-2'), ('e', '2'), ('e', '8'),
    ('f', '1'), ('f', '-1'), ('f', '7'),
    ('g', '-6'), ('g', '-2'), ('g', '3'),
    ('h', '2'), ('h', '0'), ('h', '-2'),
    ('i', '7'), ('i', '-6'), ('i', '4'),
    ('j', '-6'), ('j', '-9'), ('j', '-3'),
    ('k', '4'), ('k', '10'), ('k', '3'),
    ('L', '0'), ('L', '-8'), ('L', '-1'),
    ('m', '5'), ('m', '2'), ('m', '-1'),
]
midterm_edges_q1_2 = [  # Q1.2: depth = 5, call alphabeta with 3
    ('a', 'b'), ('a', 'b1'),
    ('b', 'c0'), ('b', 'c-1'),
    ('b1', 'c'), ('b1', 'd'),
    ('c0', 'e0'), ('c0', 'e-15'),
    ('c-1', 'e'), ('c-1', 'f'),
    ('c', 'g1'), ('c', 'g'),
    ('d', 'h12'), ('d', 'h'),
    ('e0', '8'), ('e0', '0'),
    ('e-15', '12'), ('e-15', '-15'),
    ('e', '-1'), ('e', '11'),
    ('f', '-18'), ('f', '-20'),
    ('g1', '8'), ('g1', '1'),
    ('g', '-14'), ('g', '1'),
    ('h12', '12'), ('h12', '13'),
    ('h', '-15'), ('h', '-8')
    ]

midterm_edges_q1_3 = [  # Q1.3:
    ('', ''), ('', '')
]

#graph.add_edges_from(midterm_edges_q1_2)
graph.add_weighted_edges_from(midterm_edges_q1_3)
# e_graph = ExplorableGraph(graph)
# alphabeta(e_graph, 4)  # , float("-inf"), float("inf"), True)
alphabeta(graph, 'a', 3)
# children = graph['a']
# length = len(children)
# print(len(children))
# print(children)


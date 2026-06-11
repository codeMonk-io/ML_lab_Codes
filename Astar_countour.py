import heapq

# Graph with edge costs
graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 3), ('E', 1)],
    'C': [('F', 5)],
    'D': [],
    'E': [('G', 2)],
    'F': [('G', 1)],
    'G': []
}

# Heuristic values
h = {
    'A': 5,
    'B': 4,
    'C': 3,
    'D': 3,
    'E': 2,
    'F': 1,
    'G': 0
}

def astar(start, goal):
    pq = []
    visited = set()
    heapq.heappush(pq, (h[start], 0, start))    # (f, g, node)

    while pq:
        f, g, node = heapq.heappop(pq)
        # Actual cost (g) → Cost from Start → Current Node
        # Heuristic cost (h) → Estimated cost from Current Node → Goal
        # Total cost (f) → f = g + h
        if node in visited:
            continue

        visited.add(node)

        print("Visited:", node)

        if node == goal:
            print("Goal Found")
            print("Cost =", g)
            return

        for neighbor, cost in graph[node]:
            if neighbor not in visited:
                new_g = g + cost
                new_f = new_g + h[neighbor]

                heapq.heappush(
                    pq,
                    (new_f, new_g, neighbor)
                )

    print("Goal Not Found")


astar('A', 'G')
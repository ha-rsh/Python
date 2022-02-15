import heapq


def dijkstra(graph, start):
    distances = {vertex: float('inf') for vertex in graph}
    pq = []
    pq_update = {}
    distances[start] = 0

    for vertex, value in distances.items():
        entry = [vertex, value]
        heapq.heappush(pq, entry)
        pq_update[vertex] = entry

    while pq:

        getmin = heapq.heappop(pq)[0]

        for neighbour, distance_neigh in graph[getmin].items():
            dist = distances[getmin] + distance_neigh
            if dist < distances[neighbour]:
                distances[neighbour] = dist
                pq_update[neighbour][1] = dist  # THIS LINE !!!

    print(distances)
    return distances


if __name__ == '__main__':
    example_graph = {
        'U': {'V': 2, 'W': 5, 'X': 1},
        'V': {'U': 2, 'X': 2, 'W': 3},
        'W': {'V': 3, 'U': 5, 'X': 3, 'Y': 1, 'Z': 5},
        'X': {'U': 1, 'V': 2, 'W': 3, 'Y': 1},
        'Y': {'X': 1, 'W': 1, 'Z': 1},
        'Z': {'W': 5, 'Y': 1},
    }
    dijkstra(example_graph, 'X')

from collections import deque

# Undirected graph for GERALDEZ.
# 1=G, 2=E, 3=R, 4=A, 5=L, 6=D, 7=E, 8=Z
# Neighbor order is fixed for reproducible traversal results.
GRAPH = {
    "1-G": ["2-E", "3-R"],
    "2-E": ["1-G", "4-A", "5-L"],
    "3-R": ["1-G", "6-D", "7-E"],
    "4-A": ["2-E", "8-Z"],
    "5-L": ["2-E", "8-Z"],
    "6-D": ["3-R", "8-Z"],
    "7-E": ["3-R", "8-Z"],
    "8-Z": ["4-A", "5-L", "6-D", "7-E"],
}


def breadth_first_search(graph, start):
    """Visit graph vertices level by level using a queue."""
    visited = {start}
    queue = deque([start])
    result = []

    while queue:
        current = queue.popleft()
        result.append(current)

        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return result


def depth_first_search(graph, start):
    """Explore deeply before backtracking, using recursive DFS."""
    visited = set()
    result = []

    def visit(vertex):
        visited.add(vertex)
        result.append(vertex)

        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visit(neighbor)

    visit(start)
    return result


def main():
    print("GRAPH: GERALDEZ")
    print("Vertices: 1-G, 2-E, 3-R, 4-A, 5-L, 6-D, 7-E, 8-Z")
    print("Undirected edges:")
    edges = [
        ("1-G", "2-E"), ("1-G", "3-R"),
        ("2-E", "4-A"), ("2-E", "5-L"),
        ("3-R", "6-D"), ("3-R", "7-E"),
        ("4-A", "8-Z"), ("5-L", "8-Z"),
        ("6-D", "8-Z"), ("7-E", "8-Z"),
    ]
    for first, second in edges:
        print(f"  {first} -- {second}")

    print()
    print("BFS starting at 1-G:", " -> ".join(breadth_first_search(GRAPH, "1-G")))
    print("DFS starting at 1-G:", " -> ".join(depth_first_search(GRAPH, "1-G")))


if __name__ == "__main__":
    main()

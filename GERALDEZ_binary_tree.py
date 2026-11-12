from collections import deque

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def breadth_first_search(root):
    """Visit nodes level by level, from left to right."""
    if root is None:
        return []

    result = []
    queue = deque([root])

    while queue:
        current = queue.popleft()
        result.append(current.value)

        if current.left is not None:
            queue.append(current.left)
        if current.right is not None:
            queue.append(current.right)

    return result


def depth_first_search(root):
    """Preorder DFS: visit node, left subtree, then right subtree."""
    result = []

    def visit(node):
        if node is None:
            return
        result.append(node.value)
        visit(node.left)
        visit(node.right)

    visit(root)
    return result


def build_geraldez_tree():
    # Numbering: 1=G, 2=E, 3=R, 4=A, 5=L, 6=D, 7=E, 8=Z
    root = Node("1-G")
    root.left = Node("2-E")
    root.right = Node("3-R")
    root.left.left = Node("4-A")
    root.left.right = Node("5-L")
    root.right.left = Node("6-D")
    root.right.right = Node("7-E")
    root.left.left.left = Node("8-Z")
    return root


def main():
    root = build_geraldez_tree()

    print("BINARY TREE: GERALDEZ")
    print("                 1-G")
    print("               /     \\")
    print("             2-E     3-R")
    print("            /   \\   /   \\")
    print("          4-A  5-L 6-D  7-E")
    print("         /")
    print()
    print("BFS:", " -> ".join(breadth_first_search(root)))
    print("DFS:", " -> ".join(depth_first_search(root)))


if __name__ == "__main__":
    main()
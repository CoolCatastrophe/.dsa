from graphviz import Digraph


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def invert_tree(root):
    if root is None:
        return
    root.left, root.right = root.right, root.left
    invert_tree(root.left)
    invert_tree(root.right)


# Create the original tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)


# Create a Graphviz graph
def visualize_tree(root, graph=None):
    if graph is None:
        graph = Digraph(comment="Binary Tree")

    if root:
        graph.node(str(root.val))
        if root.left:
            graph.edge(str(root.val), str(root.left.val))
            visualize_tree(root.left, graph)
        if root.right:
            graph.edge(str(root.val), str(root.right.val))
            visualize_tree(root.right, graph)

    return graph


# Visualize the original tree
original_tree_graph = visualize_tree(root)
original_tree_graph.render("original_tree", format="png", cleanup=True)

# Invert the tree
invert_tree(root)

# Visualize the inverted tree
inverted_tree_graph = visualize_tree(root)
inverted_tree_graph.render("inverted_tree", format="png", cleanup=True)

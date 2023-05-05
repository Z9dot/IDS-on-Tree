import string

class Node:
    def __init__(self, value):
        self.value = value
        self.children = {}

def create_tree(depth):
    root = Node("")
    stack = [root]
    for i in range(depth):
        new_stack = []
        for parent in stack:
            for letter in string.ascii_lowercase:
                value = parent.value + letter
                child = Node(value)
                parent.children[letter] = child
                new_stack.append(child)
            # Add an empty child node for each parent
            empty_child = Node("")
            parent.children[""] = empty_child
            new_stack.append(empty_child)
        stack = new_stack
    return root

def print_tree(node):
    print(node.value)
    for child in node.children.values():
        print_tree(child)

def iterative_deepening_search(node, target_value, max_depth):
    for depth in range(max_depth):
        result = depth_limited_search(node, target_value, depth)
        if result is not None:
            return result
    return None

def depth_limited_search(node, target_value, depth_limit):
    if node.value == target_value:
        return [node.value]
    elif depth_limit == 0:
        return None
    else:
        for child in node.children.values():
            result = depth_limited_search(child, target_value, depth_limit-1)
            if result is not None:
                return [node.value] + result
        return None

# Create the tree
max_depth = 5
root = create_tree(max_depth)

# Print the tree
#print_tree(root)

# Search for the value "cat"
target_value = "poet"
path = iterative_deepening_search(root, target_value, max_depth)

# Print the path
if path is not None:
    print(" -> ".join(path))
else:
    print("Path not found.")

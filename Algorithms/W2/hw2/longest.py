def _longest_and_height(tree):
    if tree == []:
        return -1, -1  # Base case: empty tree has -1 height and -1 longest path
    
    left_tree = tree[0]
    right_tree = tree[2]
    
    # Get longest path and height for both subtrees
    left_longest, left_height = _longest_and_height(left_tree)
    right_longest, right_height = _longest_and_height(right_tree)
    
    # Current height is max of subtree heights plus 1(root)
    height = max(left_height, right_height) + 1
    
    # Longest path could be:
    # 1. Longest path in left subtree
    # 2. Longest path in right subtree
    # 3. Path going through root (left_height + right_height + 2)
    longest = max(left_longest, right_longest, left_height + right_height + 2)
    
    return longest, height

def longest(tree):
    longest_path, _ = _longest_and_height(tree)
    return longest_path

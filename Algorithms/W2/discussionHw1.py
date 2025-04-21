def sorted (tree):
    if tree is None:
        return []
    return sorted(tree.left) + [tree.val] + sorted(tree.right)

def sorted2(tree):
    res = []
    def _sorted(tree):
        if tree is None:
            return
        left,root,right = tree
        _sorted(left)
        res.append(root)
        _sorted(right)
    _sorted(tree)
    return res
    

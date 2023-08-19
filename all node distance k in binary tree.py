class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def findNodesAtDistanceK(root, target, k):
    def dfs(node, parent, target):
        if not node:
            return
        
        if node.val == target:
            targetNode[0] = node
            targetParent[0] = parent
        
        dfs(node.left, node, target)
        dfs(node.right, node, target)
    
    def collectNodes(node, distance, k):
        if not node:
            return
        
        if distance == k:
            result.append(node.val)
            return
        
        collectNodes(node.left, distance + 1, k)
        collectNodes(node.right, distance + 1, k)
    
    targetNode = [None]
    targetParent = [None]
    dfs(root, None, target)
    
    result = []
    collectNodes(targetNode[0], 0, k)
    
    if targetParent[0]:
        collectNodes(targetParent[0], 1, k - 1)
    
    return result

# Example usage
# Constructing a sample binary tree
root = TreeNode(3)
root.left = TreeNode(5)
root.right = TreeNode(1)
root.left.left = TreeNode(6)
root.left.right = TreeNode(2)
root.right.left = TreeNode(0)
root.right.right = TreeNode(8)
root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(4)

target_node = root.left
k_distance = 2
result = findNodesAtDistanceK(root, target_node.val, k_distance)
print(result)  # Output should be [7, 4, 1]

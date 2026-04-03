# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


#recursive solution
# I start from the root, the base case is that there are no child, in such case its a success (valid subtree), if there are child I visit them recursively and check if there is a problem, in that case i simply return False

class Solution:
    def check(node, min, max):
        if(not node):
            return True #base case
        if(not(min < node.val < max)):
            return False 
        return check(node.left, min, node.val) and check(node.right, node.val, max)
    
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return check(root, float('-inf'), float('inf'))
        
            

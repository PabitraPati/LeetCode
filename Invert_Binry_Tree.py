"""
Invert a binary tree.

Example:

Input:

     4
   /   \
  2     7
 / \   / \
1   3 6   9

Output:

     4
   /   \
  7     2
 / \   / \
9   6 3   1


Explanation :- Traverse to the leaf nodes and then traverse back to the root inverting from leaf nodes
For the above the call will proceed as
Invert(4) 
          -->Invert(2)
               -> Invert(1)
                       left = 1
               -> invert(3)  
                       right = 3
                swap(left, right) =  swap(1,3) --> [2,3,1]             2
           left = [2,3,1]                                             / \
                                                                     3   1
          --> invert(7)
               -> Invert(6)
                       left = 6
               -> invert(9)  
                       right = 9
                swap(left, right)  =  swap(6, 9) --> [7,9,6]                 7
           right = [7,9,6]                                                  / \
                                                                           9   6
          swap(left, right)  =  swap([2,3,1], [7,9,6])
        [7,9,6] --- 4 --- [2,3,1] 
           
     4        
   /   \
  7     2
 / \   / \
9   6 3   1
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        
        if root == None:
            return root
        
        left = self.invertTree(root.left)
        right =  self.invertTree(root.right)
        
        # Or in one line
        # left, right = self.invertTree(root.left),self.invertTree(root.right)
        
        root.left, root.right = right, left
        return root

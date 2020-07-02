# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return
        ans=[]
        level=0
        queue=[root]
        while(queue):
            ans.append([])
            for i in range(len(queue)):
                current=queue.pop(0)
                ans[level].append(current.val)
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
            level+=1
        return ans[::-1]
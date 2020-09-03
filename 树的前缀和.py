import collections

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def FindPath(self, root, K):
        if not root:
            return []
        self.ans=[]
        self.find(root,K,[],0)
        return self.ans
    def find(self,root,K,path,sum):
        sum += root.val
        path.append(root.val)
        if sum == K:
            if path not in self.ans:
                self.ans.append(path)
            return
        nextpath=path.copy()
        if root.left:
            self.find(root.left,K,nextpath,sum)
            self.find(root.left,K,[],0)
        nextpath=path.copy()
        if root.right:
            self.find(root.right,K,nextpath,sum)
            self.find(root.right,K,[],0)
        return

a = [5,4,8,11,None,13,4,7,2, None,None,5,1,8,None,7,10,6,None,None,None]

nodes = []
for n in a:
    if n:
        nodes.append(TreeNode(n))
root = nodes[0]
root.left = nodes[1]
root.right = nodes[2]
root.left.left = nodes[3]
root.right.left = nodes[4]
root.right.right = nodes[5]
root.left.left.left = nodes[6]
root.left.left.right = nodes[7]
root.right.right.left = nodes[8]
root.right.right.right = nodes[9]
root.left.left.left.left = nodes[10]
root.left.left.right.left = nodes[11]
root.left.left.right.right = nodes[12]
root.right.right.left.left = nodes[13]




K=35
solution = Solution()
ans = solution.FindPath(root, K)
print(ans)

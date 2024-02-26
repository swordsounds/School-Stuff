class Solution:
    def findMode(self, root):

        self.count = 0  #count of concurrent elements
        self.maxc = 0  #maximum count is stored
        self.val = -999  #value of element
        res = []  #resultant array

        def order(root):
            if not root:
                return
            order(root.left)
            if self.val == root.val:
                self.count += 1
            else:
                self.count = 0
                self.val = root.val
            if self.maxc < self.count:
                res.clear()
                res.append(root.val)
            elif self.maxc == self.count:
                res.append(root.val)
            self.maxc = max(self.maxc, self.count)
            order(root.right)

        order(root)
        return res

root = [1, None, 2, 2]  
sol = Solution()

sol.findMode(root)
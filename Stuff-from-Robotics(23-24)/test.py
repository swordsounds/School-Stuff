nums1 = [1,4,2] #2
nums2 = [1,2,4]

# nums1 =    [2,5,1,2,5] #3
# nums2 = [10,5,2,1,5,2]

# nums1 = [1,3,7,1,7,5] #2
# nums2 = [1,9,2,5,1]

class Solution:
    def maxUncrossedLines(self, nums1, nums2):
        max_lines = 0
        shortest_list = []
        my_dict = {}
        if nums1 >= nums2:
            shortest_list= nums1
        else:
            shortest_list = nums2
        for i in range(len(shortest_list)):
            my_dict[nums1[i]] = i
        print(my_dict)



solve = Solution()
solve.maxUncrossedLines(nums1, nums2)

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        maxLength = 0
        charMap = {}
        left = 0
        
        for right in range(n):
            if s[right] not in charMap or charMap[s[right]] < left:
                charMap[s[right]] = right
                maxLength = max(maxLength, right - left + 1)
            else:
                left = charMap[s[right]] + 1
                charMap[s[right]] = right
            print(f"ML:{maxLength} ", f"L:{left} ", f"R:{right}")
        
        return maxLength
    
solve = Solution()
solve.lengthOfLongestSubstring("pwwkew")
# print(solve.lengthOfLongestSubstring("pwwkew"))

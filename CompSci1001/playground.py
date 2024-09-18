class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        hashset = set()

        for l in s:
            if l not in hashset:
                hashset.add(l)

        for l in t:
            if l not in hashset:
                return False
        return True

      
       
    
s = "jmm"
t = "jam"

x = Solution()

print(x.isAnagram(s, t))

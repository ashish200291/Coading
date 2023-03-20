class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False;
        
        s_map ,t_map = [0]*26, [0]*26
        for i in s:
            s_map[ord(i)- 97] += 1

        for i in t:
            t_map[ord(i)-97] += 1
        
        for i in range(len(s_map)):
            if s_map[i]!= t_map[i]:
                return False

        return True
    
 TC: O(N)
 SC: O(N)
    
###########################################################    
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return countS == countT

 TC: O(N)
 SC: O(N)
############################################################

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        return collections.Counter(s) == collections.Counter(t)

 
TC: O(N)
SC: O(N)
############################################################

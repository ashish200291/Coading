class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_map ,t_map = [0]*26, [0]*26
        for i in s:
            s_map[ord(i)- 97] += 1

        for i in t:
            t_map[ord(i)-97] += 1
        
        for i in range(len(s_map)):
            if s_map[i]!= t_map[i]:
                return False

        return True

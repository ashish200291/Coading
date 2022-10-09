class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        ad_list = [[] for _ in range(n)]
        
        for a,b in edges:
            ad_list[a].append(b)
            ad_list[b].append(a)
            
        seen = set()
        stack = [source]
        
        while stack:
            node = stack.pop()
            
            if node == destination:
                return True
            
            if node in seen:
                continue
            
            seen.add(node)
            for neighbor in ad_list[node]:
                stack.append(neighbor)
        return False
        

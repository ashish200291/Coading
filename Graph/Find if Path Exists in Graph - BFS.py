from collections import deque

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        ad_list = defaultdict(list)
        #ad_list = [[] for _ in range(n)]
        
        for a,b in edges:
            ad_list[a].append(b)
            ad_list[b].append(a)
            
        q = deque([source])
        visited = set()
        
        while q:
            node = q.popleft()
            if node == destination:
                return True
            
            if node in visited:
                continue
            visited.add(node)
            
            for neighbor in ad_list[node]:
                q.append(neighbor)
        return False

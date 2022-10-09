#BI-BIDIRECTIONAL BFS
#Time Complexity:  
#Space Complexity: 

#================================================================================================
#UNION FIND 
#Time Complexity:  
#Space Complexity: 
#================================================================================================
#BFS
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
        
#Time Complexity:  O(V+E)
#Space Complexity: O(V+E)
#================================================================================================


#DFS - itterative
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
        
#Time Complexity:  O(V+E)
#Space Complexity: O(V+E)


#================================================================================================
#DFS - Recursive
class Solution:
def validPath(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:
    neighbors = defaultdict(list)
    for n1, n2 in edges:
        neighbors[n1].append(n2)
        neighbors[n2].append(n1)

    def dfs(node, end, seen):
        if node == end:
            return True
        if node in seen:
            return False

        seen.add(node)
        for n in neighbors[node]:
            if dfs(n, end, seen):
                return True

        return False

    seen = set()    
    return dfs(start, end, seen)

#Time Complexity:  O(V+E)
#Space Complexity: O(V+E)
#================================================================================================

from collections import deque

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        # edge to adjacency list
        adj = defaultdict(list)

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        # BFS
        visited = {source}
        q = deque()
        q.append(source)

        while q:

            top = q.popleft()

            if top == destination:
                return True

            # traverse all neighbours

            for node in adj[top]:

                if node in visited:
                    continue

                elif node not in visited:
                    visited.add(node)
                    q.append(node)

        return False

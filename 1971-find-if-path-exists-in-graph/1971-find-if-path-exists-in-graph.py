from collections import deque

class Solution:

    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        # edge to adjacency list
        adj = defaultdict(list)

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)


        visited = {source}

        def dfs(node):
            
            # Induction case
            if node == destination:
                return True

            # Hypothesis
            for neighbor in adj[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    if dfs(neighbor):
                        return True

            return False

        return dfs(source)

    def validPathDFSOld(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        # edge to adjacency list
        adj = defaultdict(list)

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)


        visited = {source}

        def dfs(node, res):
            
            # base case
            if node == destination:
                res[0] = True

            # base case
            if len(adj[node]) == 0:
                return

            # hypothesis
            for neighbor in adj[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    dfs(neighbor, res)

            return

        res = [False]
        dfs(source, res)

        return res[0]

    def validPathBFS(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
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
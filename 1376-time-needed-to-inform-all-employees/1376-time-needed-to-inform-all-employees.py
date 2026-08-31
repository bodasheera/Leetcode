class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        

        adj = defaultdict(list)

        for i, node in enumerate(manager):
            if i == headID:
                continue
            adj[node].append(i)

        if len(adj) == 0:
            return informTime[headID]

        # DFS
        visited = {headID}

        def solve(node):

            # base case
            if len(adj[node]) == 0:
                return 0

            # induction
            curr = informTime[node]

            neighbour = 0

            
            # hypothesis
            for v in adj[node]:
                neighbour = max(neighbour, solve(v))

            
            # induction
            return curr + neighbour


        return solve(headID)




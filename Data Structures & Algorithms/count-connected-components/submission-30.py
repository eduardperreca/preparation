class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        res = 0
        queue = deque()
        visited = set()
        for node in range(n):
            if node not in visited:
                res += 1
                queue.append(node)
                while queue:
                    u = queue.popleft()
                    if u not in visited:
                        visited.add(u)
                        for v in graph[u]:
                            if v not in visited:
                                queue.append(v)
        return res
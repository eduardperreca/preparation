class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        visited = set()
        queue = deque()
        res = 0
        for i in range(n):
            if i not in visited:
                res += 1 
                queue = deque([i])
                while queue:
                    node = queue.popleft()
                    if node not in visited:
                        visited.add(node)
                    for neigh in graph[node]:
                        if neigh not in visited:
                            queue.append(neigh)
        return res
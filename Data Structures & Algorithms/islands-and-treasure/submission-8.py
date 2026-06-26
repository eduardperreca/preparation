
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        visited = set()
        rows = len(grid)
        cols = len(grid[0])
        q = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r, c))
                    visited.add((r, c))

        dist = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist
                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited and grid[nr][nc] != -1:
                        q.append((nr, nc))
                        visited.add((nr, nc))
            dist += 1
    
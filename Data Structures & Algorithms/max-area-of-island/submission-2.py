class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        queue = deque()
        seen = set()
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        maxarea, localarea = 0, 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and (i, j) not in seen:
                    seen.add((i, j))
                    queue.append((i, j))
                    localarea = 0
                    while queue:
                        col, row = queue.popleft()
                        localarea += 1
                        for dx, dy in dirs:
                            dcols, drows = col + dx, row + dy
                            if 0 <= dcols < len(grid) and 0 <= drows < len(grid[0]) and (dcols, drows) not in seen and grid[dcols][drows] == 1:
                                seen.add((dcols, drows))
                                queue.append((dcols, drows))
                    maxarea = max(maxarea, localarea)
        return maxarea
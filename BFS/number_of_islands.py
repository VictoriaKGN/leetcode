class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        
        islands = 0
        visited = set()
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        
        def bfs(r, c) :
            queue = deque()
            queue.append((r, c))
            visited.add((r, c))

            while queue:
                row, col = queue.popleft()
                for dr, dc in directions:
                    r = row + dr
                    c = col + dc
                    if 0 <= r and r < len(grid) and -0 <= c and c < len(grid[0]) and grid[r][c] == "1" and (r, c) not in visited:
                        queue.append((r, c))
                        visited.add((r, c))

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1" and (r, c) not in visited:
                    islands += 1
                    bfs(r, c)

        return islands
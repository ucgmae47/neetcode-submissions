class Solution {
    public int numIslands(char[][] grid) {
        int count = 0;
        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[0].length; j++) {
                if (grid[i][j] == '1') {
                    count++;
                    grid[i][j] = '0';
                    dfs(grid, i, j);
                }
            }
        }
        return count;
    }
    public void dfs(char[][] grid, int x, int y) {
        int[][] dir =  {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
        for (int[] d : dir) {
            if (x+d[0] < 0 || x+d[0] >= grid.length || y+d[1] < 0 || y+d[1] >= grid[0].length) {
                continue;
            }
            if (grid[x+d[0]][y+d[1]] == '1') {
                grid[x+d[0]][y+d[1]] = '0';
                dfs(grid, x+d[0], y+d[1]);
            }
        }
    }
}

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        ROWS = len(obstacleGrid)
        COLS = len(obstacleGrid[0])

        dp = [[ 0 for _ in range(COLS)] for _ in range(ROWS)]

        for r in range(ROWS):
            if obstacleGrid[r][0] != 1:
                dp[r][0] = 1
            else:
                break

        for c in range(COLS):
            if obstacleGrid[0][c] != 1:
                dp[0][c] = 1
            else:
                break
        
        for r in range(1, ROWS):
            for c in range(1, COLS):
                if obstacleGrid[r][c] == 1 :
                    dp[r][c] = 0
                else:
                    dp[r][c] = dp[r-1][c] + dp[r][c-1]
        
        return dp[-1][-1]
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # Top-Down Approach
        # m, n = len(triangle), len(triangle[-1])
        # dp = [[float('inf')] * n for _ in range(m)]

        # dp[0][0] = triangle[0][0]

        # for i in range(1,m):
        #     dp[i][0] = triangle[i][0] + dp[i-1][0]

        # for i in range(1,m):
        #     for j in range(1,i+1):
        #         dp[i][j] = triangle[i][j] + min(dp[i-1][j], dp[i-1][j-1])
        
        # return min(dp[m-1])

        # Bottom-Up Approach

        # Start from the second-to-last row, and move upwards
        for row in range(len(triangle) - 2, -1, -1):
            for col in range(len(triangle[row])):
                # Update the current cell with the minimum path sum from the two possible next cells
                triangle[row][col] += min(triangle[row + 1][col], triangle[row + 1][col + 1])

        # The top element now contains the minimum path sum
        return triangle[0][0]

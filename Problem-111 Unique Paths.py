# 62. Unique Paths
# https://leetcode.com/problems/unique-paths/

# Logic: As only way to reach a cell is from the top or from the left. 
# We can work on it as DP. The defination of the cell being, ways to 
# reach this cell. So it is the sum from the cell to the right and cell 
# on the top. The first row and column will be 1 as going right will 
# make the entire first row as one and going all down makes column 1 
# as 1. Return the last cell of dp.

# Time Complexity: O(M*N)
# Space Complexity: O(M*N)

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for i in range(n)] for j in range(m)]
        
        for i in range(n):
            dp[0][i] = 1
        
        for j in range(m):
            dp[j][0] = 1
            
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        return dp[m-1][n-1]
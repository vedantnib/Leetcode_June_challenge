#Unique Paths

#Solution
#A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

#The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

#How many possible unique paths are there?


#Above is a 7 x 3 grid. How many possible unique paths are there?

 

#Example 1:

#Input: m = 3, n = 2
#Output: 3
#Explanation:
#From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
#1. Right -> Right -> Down
#2. Right -> Down -> Right
#3. Down -> Right -> Right
#Example 2:

#Input: m = 7, n = 3
#Output: 28
 

#Constraints:

#1 <= m, n <= 100
#It's guaranteed that the answer will be less than or equal to 2 * 10 ^ 9.

#Code:

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo={}
        def rec(memo,curr):
            if curr==(m-1,n-1):return 1
            if curr in memo:return memo[curr]
            m1=n1=0
            if curr[0]+1<m:
                m1=rec(memo,(curr[0]+1,curr[1]))
            if curr[1]+1<n:
                n1=rec(memo,(curr[0],curr[1]+1))
            memo[(curr)]=m1+n1
            return memo[(curr)]
        return rec(memo,(0,0))
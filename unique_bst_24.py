#Unique Binary Search Trees

#Solution
#Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?

#Example:

#Input: 3
#Output: 5
#Explanation:
#Given n = 3, there are a total of 5 unique BST's:

#   1         3     3      2      1
#    \       /     /      / \      \
#     3     2     1      1   3      2
#    /     /       \                 \
#   2     1         2                 3

#Code:

class Solution:
    def numTrees(self, n: int) -> int:
        if n == 1:
            return 1
        dp = [1]*(n+1)
        for number_of_nodes in range(2,n+1):
            number_of_bst = 0
            for root in range(1,number_of_nodes+1):
                number_of_nodes_greater_than_root = number_of_nodes - root
                number_of_nodes_smaller_than_root = root - 1
                number_of_bst += dp[number_of_nodes_greater_than_root]*dp[number_of_nodes_smaller_than_root]
            dp[number_of_nodes] = number_of_bst
        return dp[-1]
#Single Number II

#Solution
#Given a non-empty array of integers, every element appears three times except for one, which appears exactly once. Find that single one.

#Note:

#Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

#Example 1:

#Input: [2,2,3,2]
#Output: 3
#Example 2:

#Input: [0,1,0,1,0,1,99]
#Output: 99

#Code:

from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return Counter(nums).most_common()[-1][0]
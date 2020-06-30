#Permutation Sequence

#Solution
#The set [1,2,3,...,n] contains a total of n! unique permutations.

#By listing and labeling all of the permutations in order, we get the following sequence for n = 3:

#"123"
#"132"
#"213"
#"231"
#"312"
#"321"
#Given n and k, return the kth permutation sequence.

#Note:

#Given n will be between 1 and 9 inclusive.
#Given k will be between 1 and n! inclusive.
#Example 1:

#Input: n = 3, k = 3
#Output: "213"
#Example 2:

#Input: n = 4, k = 9
#Output: "2314"

#Code:

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        levels = []
        nums = [None] * (n+1)
        res = ""
        k -= 1
        for i in range(2, n+1):
            levels.append(k%i)
            k = k // i

        levels.append(0)
        levels.reverse()

        for i in range(0, n):
            nums[i] = i+1

        for i in range(1, n):
            j = levels[i]
            res += str(nums[j])
            nums.pop(j)

        res += str(nums[0])
        return res
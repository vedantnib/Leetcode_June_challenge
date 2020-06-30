#Largest Divisible Subset

#Solution
#Given a set of distinct positive integers, find the largest subset such that every pair (Si, Sj) of elements in this subset satisfies:

#Si % Sj = 0 or Sj % Si = 0.

#If there are multiple solutions, return any subset is fine.

#Example 1:

#Input: [1,2,3]
#Output: [1,2] (of course, [1,3] will also be ok)
#Example 2:

#Input: [1,2,4,8]
#Output: [1,2,4,8]

#Code:

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        def factors(n):
            yield 1
            for i in range(2, int(math.sqrt(n)) + 1):
                if not n % i:
                    yield i
                    if i * i != n:
                        yield n // i
                        
        nums.sort()                        
        d = {}            
        for n in nums:
            for f in factors(n):
                tmp = d.get(f, []) + [n]
                d[n] = tmp if len(d.get(n, [])) < len(tmp) else d.get(n, [])
        return nums and max(d.values(), key=len)
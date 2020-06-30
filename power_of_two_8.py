#Power of Two

#Solution
#Given an integer, write a function to determine if it is a power of two.

#Example 1:

#Input: 1
#Output: true 
#Explanation: 20 = 1
#Example 2:

#Input: 16
#Output: true
#Explanation: 24 = 16
#Example 3:

#Input: 218
#Output: false

#Code:

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        powar=1
        while True:
            if (n-powar)<0 or (n-powar)==1 and n!=2:
                return False
            elif (n-powar)==0:
                return True
            else:
                powar=powar*2
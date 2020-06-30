#Longest Duplicate Substring

#Solution
#Given a string S, consider all duplicated substrings: (contiguous) substrings of S that occur 2 or more times.  (The occurrences may overlap.)

#Return any duplicated substring that has the longest possible length.  (If S does not have a duplicated substring, the answer is "".)

 

#Example 1:

#Input: "banana"
#Output: "ana"
#Example 2:

#Input: "abcd"
#Output: ""
 

#Note:

#2 <= S.length <= 10^5
#S consists of lowercase English letters.

#Code:

class Solution:
    def __init__(self):
        self.M = 1000000000000000003
        self.R = 31
        self.RK = 1

    def hash(self, str, start, length):
        hash = 0
        for i in range(start, length):
            hash = (hash * self.R + (ord(str[i]) - 97)) %self.M
        return hash

    def calculateRM(self, length):
        self.RK = 1
        for i in range(length):
            self.RK = (self.R * self.RK) % self.M

    def calculateHash(self, txt, length):
        self.calculateRM(length)
        hashSet = set()
        substrHash = self.hash(txt, 0, length)
        hashSet.add(substrHash)
        for i in range(1, len(txt) - length + 1):
            curStr = txt[i:i + length]
            newChar = ord(txt[i + length - 1]) - 97
            oldChar = ord(txt[i - 1]) - 97

            substrHash = (substrHash * self.R + newChar - oldChar * self.RK % self.M + self.M) % self.M
            if substrHash in hashSet:
                return curStr
            else:
                hashSet.add(substrHash)
        return ""

    def longestDupSubstring(self, S: str) -> str:
        lo = 0
        hi = len(S)
        result = ""
        
        while lo < hi:
            # print((lo, hi))
            mid = int((lo + hi) / 2)
            cur = self.calculateHash(S, mid)
            if not cur:
                hi = mid
            else:
                lo = mid+1
                result = cur
        return result 
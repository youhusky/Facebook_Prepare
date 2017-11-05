# Given a non-negative integer, you could swap two digits at most once to get the maximum valued number. Return the maximum valued number you could get.

# Example 1:
# Input: 2736
# Output: 7236
# Explanation: Swap the number 2 and the number 7.
# Example 2:
# Input: 9973
# Output: 9973
# Explanation: No swap.
# Note:
# The given number is in the range [0, 108]

#Greedy
class Solution(object):
    def maximumSwap(self, num):
        count = [0 for _ in  range(10)]
        
        num = map(int, str(num))
        #print num
        for n in range(len(num)):
            count[num[n]] =n
            
        for i in range(len(num)):
            for j in range(9,num[i],-1):
                if count[j] > i:
                    num[i], num[count[j]] = num[count[j]], num[i]
                    return int("".join(map(str, num)))
        res = ""
        for i in num:
            res += str(i)
        return int(res)
                
        
        
        
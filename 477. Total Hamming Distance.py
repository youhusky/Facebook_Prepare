# 这道题是之前那道Hamming Distance的拓展，由于有之前那道题的经验，我们知道需要用异或来求每个位上的情况，那么我们需要来找出某种规律来，比如我们看下面这个例子，4，14，2和1：

# 4:     0 1 0 0

# 14:   1 1 1 0

# 2:     0 0 1 0

# 1:     0 0 0 1

# 我们先看最后一列，有三个0和一个1，那么它们之间相互的汉明距离就是3，即1和其他三个0分别的距离累加，然后在看第三列，累加汉明距离为4，因为每个1都会跟两个0产生两个汉明距离，同理第二列也是4，第一列是3。我们仔细观察累计汉明距离和0跟1的个数，我们可以发现其实就是0的个数乘以1的个数，发现了这个重要的规律，那么整道题就迎刃而解了，只要统计出每一位的1的个数即可，参见代码如下：
# Copy other's think which is amazing count[0] * count[1]
class Solution(object):
    def totalHammingDistance(self, nums):
        """
        O(N)
        :type nums: List[int]
        :rtype: int
        """
        
        i = 0
        total_dist = 0
        while i < 32:
            a = 0
            b = 0
            for num in nums:
                x = num >> i
                x = x & 1
                
                if x == 1:
                    a += 1
                else:
                    b += 1
                    
            total_dist += a*b
            i += 1
                
        return total_dist
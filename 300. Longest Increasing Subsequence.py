def lis(nums):
	n = len(nums)
	# m means until this number the maxnumber of LIS
	m = [0] * n
	for i in range(n-2, -1, -1):
		for j in range(n-1, i, -1):
			# if m[i] > m[j] means there is a gap which is not continus 
			if nums[i] < nums[j] and m[i] <= m[j]:
				m[i] += 1
		max_value = max(m)
		res = []
		for k in range(n):
			if m[k] == max_value:
				res.append(nums[k])
				max_value -= 1
	return res
arr = [10, 22, 9, 33, 21, 50, 41, 60, 80]
print (lis(arr))

def lengthOfLIS(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if not nums:
        return 0
    dp = [1] * (len(nums) + 1)
    for i in range(len(nums)):
        for j in range(i):
            if nums[j] < nums[i]:
            	# from j -> i   dp[i]+1
                dp[i] = max(dp[i], dp[j]+1)
    return max(dp)

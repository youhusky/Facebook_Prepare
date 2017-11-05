# Given the running logs of n functions that are executed in a nonpreemptive single threaded CPU, find the exclusive time of these functions.

# Each function has a unique id, start from 0 to n-1. A function may be called recursively or by another function.

# A log is a string has this format : function_id:start_or_end:timestamp. For example, "0:start:0" means function 0 starts from the very beginning of time 0. "0:end:0" means function 0 ends to the very end of time 0.

# Exclusive time of a function is defined as the time spent within this function, the time spent by calling other functions should not be considered as this function's exclusive time. You should return the exclusive time of each function sorted by their function id.

# Example 1:
# Input:
# n = 2
# logs = 
# ["0:start:0",
#  "1:start:2",
#  "1:end:5",
#  "0:end:6"]
# Output:[3, 4]
# Explanation:
# Function 0 starts at time 0, then it executes 2 units of time and reaches the end of time 1. 
# Now function 0 calls function 1, function 1 starts at time 2, executes 4 units of time and end at time 5.
# Function 0 is running again at time 6, and also end at the time 6, thus executes 1 unit of time. 
# So function 0 totally execute 2 + 1 = 3 units of time, and function 1 totally execute 4 units of time.
# Note:
# Input logs will be sorted by timestamp, NOT log id.
# Your output should be sorted by function id, which means the 0th element of your output corresponds to the exclusive time of function 0.
# Two functions won't start or end at the same time.
# Functions could be called recursively, and will always end.
# 1 <= n <= 100

# use stack to store value
# see the discussion and the solution
class Solution(object):
    def exclusiveTime(self, N, logs):
        ans = [0] * N
        stack = []
        prev_time = 0

        for log in logs:
            fn, typ, time = log.split(':')
            fn, time = int(fn), int(time)

            if typ == 'start':
                if stack:
                    ans[stack[-1]] += time - prev_time 
                stack.append(fn)
                prev_time = time
            else:
                ans[stack.pop()] += time - prev_time + 1
                prev_time = time + 1

        return ans

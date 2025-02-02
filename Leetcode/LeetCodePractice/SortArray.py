from collections import deque

class Solution(object):
    def sortArray(self, nums):
        queue = deque([])
        last = -1000000
        for each in nums:
            if each < last:
                queue.appendleft(each)
            else:
                queue.append(each)
        return queue
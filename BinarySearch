import time
from typing import List


## O(log n) - BINARY SEARCH №1

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)

        while True:
            fiveteenProcent = len(nums[left:right]) // 2
            print(fiveteenProcent)
            print("int: ", nums[left:right][fiveteenProcent])

            if nums[left:right][fiveteenProcent] == target:
                return left
            elif nums[left:right][fiveteenProcent] > target:
                right -= fiveteenProcent
            elif nums[left:right][fiveteenProcent] < target:
                left += fiveteenProcent

            if len(nums[left:right]) == 2 and nums[left] != target or nums[right] != target:
                return -1

            time.sleep(2)

    def guessNumber(self, n: int) -> int:
        
        start, end = 0, n
        
        while start <= end:
            midddle = (start + end) // 2
            
            if guess(midddle) < 0:
                end = midddle - 1
            elif guess(midddle) > 0:
                start = midddle + 1
            else:
                return midddle


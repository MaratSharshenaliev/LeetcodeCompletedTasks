class Solution:
    def firstBadVersion(self, n: int) -> int:
        start, end = 0, n
        
        while start <= end:
            mid = start + (end-start) // 2
            if not isBadVersion(mid):
                start = mid + 1
            else:
                end = mid - 1
        return start
    def searchRange(self, nums: List[int], target: int) -> List[int]:
            def binary_search(nums, target, FindMax):
                keyIndex = -1
                start, end = 0, len(nums)-1
                while start <= end:
                    middle = start + (end-start)//2
                    if nums[middle] < target:
                        start = middle + 1
                    elif nums[middle] > target:
                        end = middle - 1
                    else:
                        keyIndex = middle
                        if FindMax:
                            start = middle + 1
                        else:
                            end = middle - 1
                return keyIndex
            result = [-1, -1]
            result[0] = binary_search(nums, target, False)
            if result[0] != -1:
                result[1] = binary_search(nums, target, True)
            return result

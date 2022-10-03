class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)
        if nums[::-1][0] < target:
            return right
        if target <= nums[0]:
            return 0
        while True:
            mid = (left + right) // 2
            print(nums[mid])
            if nums[mid - 1] < target <= nums[mid]:
                return mid
            elif nums[mid] > target:
                right = mid
            elif nums[mid] < target:
                left = mid
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        i, peak = 0, 0
        
        while i < len(arr)-1:
            if arr[i] < arr[i+1]:
                peak += 1
            else:
                return peak
            i += 1

class Solution:
    def isPerfectSquare(self, nums: int, Iter: int = 0) -> bool:
        # print(Iter)
        # 7: 49 = 1 + 3 + 5 + 7 + 9 + 11 + 13
        if Iter**2 == nums:
            return True
        elif Iter**2 > nums:
            return False
        else:
            return self.isPerfectSquare(nums, Iter + 1)
            
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d) -> int:
        arr2 = sorted(arr2)
        count = 0
        for val in arr1: 
            i = 0
            j = len(arr2) - 1
            while i <= j:
                mid = (i+j)//2
                if abs(val - arr2[mid]) <= d:
                    count += 1
                    break
                if arr2[mid] < val:
                    i = mid + 1
                else:
                    j = mid - 1
        return len(arr1) - count

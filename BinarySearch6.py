class Solution:
    def arrangeCoins(self, n: int) -> int:
        left, right = 1, n
        while left <= right:
            mid = (left + right) // 2
            coins = (mid / 2) * (mid + 1)
            if coins > n:
                right = mid - 1
            elif coins < n:
                left = mid + 1
            else:
                return mid
        return right
    
    
    def findKthPositive(self, arr: List[int], k: int) -> int:
        l, r = 0, len(arr)
        while l < r:
            m = (l + r) // 2
            if arr[m] - 1 - m < k:
                l = m + 1
            else:
                r = m
        return l + k

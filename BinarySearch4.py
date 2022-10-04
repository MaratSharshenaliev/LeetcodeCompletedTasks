class Solition:
  def mySqrt(self, x: int) -> int:
    
    if x <= 1: return x
    start = 2
    end = x // 2
    while start <= end:
      mid = start + (end - start)  // 2
      square = mid * mid
      if square == x: return mid
      if square < x: start = mid + 1
      else: end = mid - 1
      return end
    
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        
        st, end = 0, len(letters) - 1
        if letters[-1] <= target or letters[0] > target:
                return letters[0]
        while st<=end:
            mid=st+(end-st)//2
            if letters[mid]>target:
                end=mid-1 
            elif letters[mid]<=target:
                st=mid+1 
        return letters[st] 

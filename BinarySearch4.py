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

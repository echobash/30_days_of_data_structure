from typing import List


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        n = len(arr)
        left, right = 0, n - 1

        while left <= right:
            mid = (left + right) // 2
            if arr[mid] - (mid + 1) < k:
                left = mid + 1
            else:
                right = mid - 1

        """
        When the above Binary Search ends, left and right are interchanged i.e left > right
        no we know that the our missing no lies b/w [a[right], a[left]]
        a[right] - (right + 1) gives missing no of count in left of it.
        say if a[right] - (right + 1) = 3 missing no
        and we want kth missing no where k = 5
        So we need 2 more numbers i.e a[right] + 2
        we got 2 above by subtracting missing no count from k
        i.e kth missing no =  a[right] + [k - {a[right] - (right + 1)} ]
        => a[right] + [k - a[right] + (right + 1) ] 
        => a[right] + k - a[right] + (right + 1) 
        => k + right + 1
        """
        return k + right + 1


sol = Solution()

arr = [2,3,4,7,11]
k = 5
print(f"{arr= } | {k = } {sol.findKthPositive(arr,k)= }")

arr = [1,2,3,4]
k = 2
print(f"{arr= } | {k = } {sol.findKthPositive(arr,k)= }")

arr = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
k = 999
print(f"{arr= } | {k = } {sol.findKthPositive(arr,k)= }")


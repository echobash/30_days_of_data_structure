from typing import List


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        result = [0] * n
        right_max = -1
        result[n-1] = right_max

        # Traverse the array from the reverse side
        for i in range(n-2,-1,-1):
            #compare right_max and next array element
            if  arr[i+1] > right_max:
                result[i] = arr[i+1]
                right_max = arr[i+1]
            else:
                result[i] = right_max
        return result


sol = Solution()

arr = [17,18,5,4,6,1]
print(arr, sol.replaceElements(arr))

arr = [400]
print(arr, sol.replaceElements(arr))

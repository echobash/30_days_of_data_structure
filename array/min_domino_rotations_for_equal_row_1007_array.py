from typing import List


class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        # Check if the situation is possible
        n = len(tops)
        same_element = 0

        # Freq of all the tops element in the freq_arr as it is
        freq_arr = [0] * 7
        for top in tops:
            freq_arr[top] += 1

        # Freq of bottom elements in the freq_arr where bottom != top since their swap is not meaningless
        for i in range(n):
            if tops[i] == bottoms[i]:
                continue
            freq_arr[bottoms[i]] += 1

        # Check which element will be the same either on top or down i.e count>= n
        for i in range(7):
            if freq_arr[i] >= n:
                same_element = i
                break

        # if same_element still is unchanged, it means the current situation is not possible
        if same_element == 0:
            return -1

        """
        We know now that "same_element" will be our required element.
        So we'll count where on top or bottom are there less nos other than "same_element" 
        """
        same_element_in_top = 0
        same_element_in_bottom = 0
        for i in range(n):
            if tops[i] == same_element:
                same_element_in_top += 1

            if bottoms[i] == same_element:
                same_element_in_bottom += 1

        return min(n - same_element_in_top, n - same_element_in_bottom)


solution = Solution()

tops = [2,1,2,4,2,2]
bottoms = [5,2,6,2,3,2]
print(f"{tops = } {bottoms = } {solution.minDominoRotations(tops, bottoms) = }")

tops = [3,5,1,2,3]
bottoms = [3,6,3,3,4]
print(f"{tops = } {bottoms = } {solution.minDominoRotations(tops, bottoms) = }")

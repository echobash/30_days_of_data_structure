from typing import List


class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        """
        001011
        n = 6
        index of 1 -> {2,4,5}
        for i = 0 : {2,4,5}
        for i = 1 : {1,3,4}
        for i = 2 : {0,2,3}
        for i = 3 : {-1,1,2}
        for i = 4 : {-2, 0, 1}
        for i = 5 : {-3, 1, 0}
        """
        ones_index_list = []
        result = []
        for index, box in enumerate(boxes):
            if box == "1":
                ones_index_list.append(index)

        m = len(ones_index_list)
        result.append(sum(ones_index_list))

        for i in range(1, n):
            total_sum = 0
            for j in range(m):
                ones_index_list[j] -= 1
                total_sum += abs(ones_index_list[j])
            result.append(total_sum)

        return result


sol = Solution()

boxes = "110"
print(f"{boxes = } {sol.minOperations(boxes) = }")

boxes = "111"
print(f"{boxes = } {sol.minOperations(boxes) = }")
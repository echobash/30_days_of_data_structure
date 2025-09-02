from typing import List


class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        friends_set = set(friends)
        result = []

        for data in order:
            if data in friends_set:
                result.append(data)

        return result


sol = Solution()

order = [3,1,2,5,4]
friends = [1,3,4]
print(f" {order = }| {friends = }| {sol.recoverOrder(order,friends) = }")

order = [1,4,5,3,2]
friends = [2,5]
print(f" {order = }| {friends = }| {sol.recoverOrder(order,friends) = }")
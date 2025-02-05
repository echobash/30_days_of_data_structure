from typing import List


class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        result = []
        word_index_mapping = dict()
        m, n = len(list1), len(list2)
        min_sum = float('inf')
        current_sum = 0

        # Store all the words of first list in dictionary with its index
        for i in range(m):
            word_index_mapping[list1[i]] = i

        # Iterate on all words in list2 and check its presence if word_index_mapping dictionary
        for j in range(n):
            if list2[j] in word_index_mapping:
                current_sum = j + word_index_mapping[list2[j]]
                if current_sum < min_sum:
                    min_sum = current_sum
                    result = [list2[j]]
                elif current_sum == min_sum:
                    result.append(list2[j])
        return result


sol = Solution()

list1 = ["Shogun","Tapioca Express","Burger King","KFC"]
list2 = ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]
print(f"{list1 = } | {list2 = } | {sol.findRestaurant(list1, list2) = }")

list1 = ["Shogun","Tapioca Express","Burger King","KFC"]
list2 = ["KFC","Shogun","Burger King"]
print(f"{list1 = } | {list2 = } | {sol.findRestaurant(list1, list2) = }")

list1 = ["happy","sad","good"]
list2 = ["sad","happy","good"]
print(f"{list1 = } | {list2 = } | {sol.findRestaurant(list1, list2) = }")

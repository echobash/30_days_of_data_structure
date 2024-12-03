class TwoSum:
    def return_indices(self, nums: [int], target: int) -> [int]:
        element_index_mapping = {}
        n = len(nums)

        # Store all elements in the dictionary
        for i in range(n):
            element_index_mapping[nums[i]] = i

        # Traverse the array and search for target-nums[i] in dict
        for i in range(n):
            no_to_search = target-nums[i]
            if(no_to_search in element_index_mapping and i != element_index_mapping[no_to_search]):
                return [i, element_index_mapping[no_to_search]]



nums = [8,7,12,9]
target = 16
two_sum = TwoSum()
print(two_sum.return_indices(nums, target))
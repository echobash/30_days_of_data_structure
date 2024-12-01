# Given an array nums of size n, return the majority element.
# The majority element is the element that appears more than ⌊n / 2⌋ times.
# You may assume that the majority element always exists in the array.

class MajorityElement:
    def find(self,nums):
        count_dict = {}
        majority_count = len(nums)//2

        # Store count of each element in a dictionary
        for num in nums:
            if num in count_dict:
                count_dict[num] = count_dict[num] + 1
            else:
                count_dict[num] = 1

        # Parse the dictionary and compare with the majority_count
        for element,count in count_dict.items():
            if count > majority_count:
                return element


nums = [2,2,1,1,1,2,2]
majority_element = MajorityElement()
print(majority_element.find(nums))
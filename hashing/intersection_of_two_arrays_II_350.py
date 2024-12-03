from collections import defaultdict

class Intersector:
    def find_intesections(self, nums1: [int], nums2: [int]) ->[int]:
        first_dict = defaultdict(int)
        second_dict = defaultdict(int)

        result = []

        # Store first array elements in first dictionary
        for num in nums1:
            first_dict[num] += 1

        # Store second array elements in second dictionary
        for num in nums2:
            second_dict[num] += 1
        for element in first_dict:
            if (element in second_dict):
                intersection_count = min(first_dict[element], second_dict[element])
                result.extend([element] * intersection_count)
        return result


nums1 = [4,9,5]
nums2 = [9,4,9,8,4]

intesector = Intersector()
print(intesector.find_intesections(nums1, nums2))

nums1 = [4,5,4]
nums2 = [6,4,5]
print(intesector.find_intesections(nums1, nums2))

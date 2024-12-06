class MissingNo:
    def find(self, nums: [int]) -> int:
        number_dict = {}
        n = len(nums)

        for i in nums:
            number_dict[i] = 1

        for i in range(n + 1):
            if i not in number_dict:
                return i


nums = [9,6,4,2,3,5,7,0,1]
missing_no = MissingNo()
print(missing_no.find(nums))
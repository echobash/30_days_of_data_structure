from collections import defaultdict
class SingleNumber:
    def findMissing(self, arr) -> bool:
        freq_dict = defaultdict(int)

        for num in arr:
            freq_dict[num] += 1


        # Iterate ransom_freq_dict and compare frequecy of each char with...
        # ... mag_freq_dict. Count From ransom_freq_dict should not be ...
        # ... greater than Count From mag_freq_dict for any char.

        for num, count in freq_dict.items():
            if count == 1:
                return num


nums = [4,1,2,1,2]
single_number = SingleNumber()
print(single_number.findMissing(nums))
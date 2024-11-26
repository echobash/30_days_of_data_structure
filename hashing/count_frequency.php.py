class FrequencyCounter:
    def count(self, arr):
        frequency_dictionary = {}
        for i in arr:
            if i in frequency_dictionary:
                frequency_dictionary[i] = frequency_dictionary[i] + 1
            else:
                frequency_dictionary[i] = 1
        return frequency_dictionary


arr = [10,5,10,15,10,5]
# arr = [2,2,3,4,4,2]
counter = FrequencyCounter()
print(counter.count(arr))

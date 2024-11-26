class MinMaxFrequencyCounter:
    def find_most_and_least_frequent_element(self, arr):
        frequency_count = self.make_frequency_dict(arr)

        min = float('inf')
        max = float('-inf')

        for j in frequency_count:
            if(frequency_count[j] > max):
                max = frequency_count[j]
                max_key = j

            if (frequency_count[j] < min):
                min = frequency_count[j]
                min_key = j

        return (min_key, max_key)

    def make_frequency_dict(self, arr):
        frequency_count = {}

        for i in arr:
            if i in frequency_count:
                frequency_count[i] = frequency_count[i]+1
            else:
                frequency_count[i] = 1

        return  frequency_count


counter = MinMaxFrequencyCounter()
arr = [10,5,10,15,10,5]
(min_key, max_key) = counter.find_most_and_least_frequent_element(arr)
print("Most Frequent Element is- ", max_key)
print("Least Frequent Element is- ", min_key)
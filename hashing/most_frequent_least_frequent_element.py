class MinMaxFrequencyCounter:
    def find_most_and_least_frequent_element(self, arr):
        if len(arr) == 0:
            return (None, None)

        frequency_count = self.make_frequency_dict(arr)

        min_value = float('inf')
        max_value = float('-inf')

        for key,frequency in frequency_count.items():
            if(frequency > max_value):
                max_value = frequency
                max_key = key

            if (frequency < min_value):
                min_value = frequency
                min_key = key
        print(min_key, max_key)
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
# arr = []
(min_key, max_key) = counter.find_most_and_least_frequent_element(arr)
if(min_key is None and max_key is None):
    print("Empty List Provided")
else:
    print("Most Frequent Element is- ", max_key)
    print("Least Frequent Element is- ", min_key)
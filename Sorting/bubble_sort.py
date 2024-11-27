class BubbleSorter:
    def do_bubble_sort(self, arr):
        n = len(arr)
        for i in range(n):
            for j in range(n-i-1):
                if(arr[j]>arr[j+1]):
                    (arr[j],arr[j+1]) = (arr[j+1],arr[j])
            print(arr)
        return arr


arr = [13,46,24,52,20,9]
# arr = [12,12,12,12,12,9]
bubble_sorter = BubbleSorter()
print("Sorted array- ",bubble_sorter.do_bubble_sort(arr))
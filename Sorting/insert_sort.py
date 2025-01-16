class InsertionSorter:
    def do_bubble_sort(self, a):
        n = len(a)
        position = 0
        for i in range(n):
            changed_position = False
            current_value = a[i]
            for j in range(i, -1, -1):
                if a[j] < a[i]:
                    position = j + 1
                    changed_position = True
                    break
                elif a[i] < a[j] and j == 0:
                    position = 0
                    changed_position = True
                    break

            if changed_position == True:
                for k in range(i, position, -1):
                    a[k] = a[k - 1]
                a[position] = current_value
        return a


a=[161, 547, 321, 634, 426, 65, 504, 293, 279, 561, 515, 418, 489, 195, 986, 382, 240, 891, 872, 111, 874, 634, 426, 506, 280, 812, 339, 228, 920, 491, 726, 734, 726, 272, 168, 91, 426, 433, 387, 926, 291, 909, 562, 838, 434, 803, 882, 696, 303, 1, 321, 833, 853, 551, 767, 134, 679, 575, 743, 612, 522, 260, 383, 801, 526, 400, 230, 618, 42, 526, 145, 306, 607, 852, 198, 283, 777, 783, 826, 774, 60, 869, 81, 940, 309, 774, 74, 611, 573, 30, 199, 780, 677, 531, 945, 779, 712, 46, 927, 115]
insertion_sorter = InsertionSorter()
print("Sorted array- ",insertion_sorter.do_bubble_sort(a))
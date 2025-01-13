class Solution:
    def minimumSum(self, num: int) -> int:
        """
        minimum sum will occur iff digits are split in 2-2 otherwise as soon as it becomes 3-1 or 1-3,
        the hundredth place will increase the sum
        But as per the discussion, we can't just num//100 + num % 100 since the digits can be shuffled..
        to get minimum result
        """

        """
        Now we have to re-think on our approach.
        There will be four digits a,b,c,d
        let's say the no are ab and cd
        so we want that a and c are smallest and c and d are largest.
        This way tens place is smaller and units place is larger.
        So we know that we have to sort the four digits and form the no as

        2934 -> 2349
        first_no =  23 or 29
        second_no = 39 or 32

        Till now we're sure about what will go in tens place of both no i.e sorted_no[0] and sorted_no[1]
        But what will go in units place is yet to be decided.
        The idea is the no with larger tens place should be given smaller units.
        This way the no is smaller and hence the sum in minimum

        first_no = sorted_no[0]sorted_no[2]
        second_no = sorted_no[1]sorted_no[3]

        """
        num = sorted(str(num))
        return int(num[0] + num[2]) + int(num[1] + num[3])


sol = Solution()

num = 2932
print(num,sol.minimumSum(num))

num = 4009
print(num,sol.minimumSum(num))
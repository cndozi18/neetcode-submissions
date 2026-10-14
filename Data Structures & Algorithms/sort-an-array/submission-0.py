class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            while nums[i] < nums[i - 1]:
                if i == 0:
                    break
                temp = nums[i - 1]
                nums[i - 1] = nums[i]
                nums[i] = temp
                i -= 1
        return nums

        
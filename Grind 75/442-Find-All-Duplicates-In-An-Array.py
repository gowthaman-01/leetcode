class Solution:
    def findDuplicates(self, nums):
        res = []
        for i, num in enumerate(nums):
            if not num or i == num - 1: continue
            nums[i] = None
            while True:
                temp = nums[num - 1]
                if temp and temp == num: 
                    res.append(temp)
                    break
                nums[num - 1] = num
                if temp == None: break
                num = temp
        return res
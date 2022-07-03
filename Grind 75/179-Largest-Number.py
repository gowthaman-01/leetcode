class Solution:
    def merge(self, left, right):
        if not left or not right or not left: return right
        if not right: return left
        l, r, sort = 0, 0, []
        while l < len(left) and r < len(right):
            if int(left[l] + right[r]) >= int(right[r] + left[l]):
                sort.append(left[l])
                l += 1
            else:
                sort.append(right[r])
                r += 1
        while l < len(left):
            sort.append(left[l])
            l += 1
        while r < len(right):
            sort.append(right[r])
            r += 1
        return sort           
                    
    def mergeSort(self, strings, l, r):
        if l >= r:
            return strings[l: r + 1]
        mid = (l + r) // 2
        left = self.mergeSort(strings, l, mid)
        right = self.mergeSort(strings, mid + 1, r)
        sort = self.merge(left, right)
        return sort
          
    def largestNumber(self, nums):
        strings = [str(nums[i]) for i in range(len(nums))]
        sort = self.mergeSort(strings, 0, len(strings) - 1)
        res = ""
        for string in sort:
            res += string
        if int(res) == 0:
            return "0"
        return res
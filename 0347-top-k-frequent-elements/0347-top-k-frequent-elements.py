class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        buckets = [[] for _ in range(len(nums) + 1)]
        for num, count in counter.items(): 
            buckets[count].append(num)
        
        res = []
        for i in range(len(nums), 0, -1):
            for num in buckets[i]:
                res.append(num)
                k -= 1
            if k == 0:
                return res
        
        return res
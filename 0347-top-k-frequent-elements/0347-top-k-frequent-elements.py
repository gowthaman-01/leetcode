class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = {}
        for num in nums:
            freq_map[num] = freq_map.get(num, 0) + 1
        
        buckets = [[] for _ in range(len(nums) + 1)]
        print(len(nums) + 1)
        for num, freq in freq_map.items():
            buckets[freq].append(num)
        
        res = []
        for i in range(len(nums), 0, -1):
            if k == 0:
                return res
            
            for num in buckets[i]:
                res.append(num)
                k -= 1
        
        return res
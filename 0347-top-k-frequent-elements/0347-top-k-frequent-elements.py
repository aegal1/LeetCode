class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)] 
        
        for n in nums:
            count[n] = 1 + count.get(n, 0) #counts how many times each value in n occurs. If it doesnt exist we put a default value of 0.
        for n, c in count.items(): #Go through each value we counted.
            freq[c].append(n)
        
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
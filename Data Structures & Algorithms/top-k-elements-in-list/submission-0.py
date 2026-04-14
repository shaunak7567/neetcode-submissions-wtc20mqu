from itertools import count

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countmap={}

        freq=[[] for n in range(len(nums)+ 1)]

        for n in nums:
            countmap[n] = 1 + countmap.get(n,0)
        for n,c in countmap.items():
            freq[c].append(n)
        
        res=[]
        for i in range(len(freq)-1,0,-1):
            for n in freq[i]:
                res.append(n)
            if len(res) == k:
                return res

        
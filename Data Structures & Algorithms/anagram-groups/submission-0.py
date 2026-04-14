from collections import defaultdict
from itertools import count

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        countmap=defaultdict(list)

        for str1 in strs:
            char_counts = [0] * 26
            for char in str1:
               char_counts[ord(char) - ord("a")] += 1
            countmap[tuple(char_counts)].append(str1)
        return list(countmap.values())
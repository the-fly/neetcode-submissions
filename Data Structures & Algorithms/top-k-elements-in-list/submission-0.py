class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        # sortedCounts = dict(sorted(counts.items(), key=lambda item: item[1], reverse=True))
        sortedCounts = dict(sorted(counts.items(), key=lambda item: item[1], reverse=True))

        res = []
        for item in sortedCounts:
            if len(res) == k:
                return res
            else:
                res.append(item)
        return res
        
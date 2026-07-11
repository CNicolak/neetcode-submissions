class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        sorted_counts = {}
        for num in nums:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1

        sorted_counts = sorted(counts.items(), key=lambda pair: pair[1], reverse=True)
        return [pair[0] for pair in sorted_counts[:k]]
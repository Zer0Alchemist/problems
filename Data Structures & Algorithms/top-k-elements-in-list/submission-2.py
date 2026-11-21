class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dct = {}

        for n in nums:
            if n not in dct:
                dct[n] = 1
            else:
                dct[n] += 1

        srted_dct = dict(sorted(dct.items(), key=lambda x: x[1], reverse=True))
        res = []
        for i, key in enumerate(srted_dct.keys()):
            res.append(key)
            if i == k - 1:
                break

        return res
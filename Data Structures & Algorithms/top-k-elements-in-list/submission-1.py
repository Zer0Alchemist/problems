class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dct = {}

        for n in nums:
            if n not in dct.keys():
                dct[n] = 1
            else:
                dct[n] += 1
        
        sorted_dict = {k:v for k, v in sorted(dct.items(), key=lambda x: x[1], reverse=True)}
        i = 0
        lst = []
        for key in sorted_dict.keys():
            if i == k:
                break
            lst.append(key)
            i += 1

        return lst        
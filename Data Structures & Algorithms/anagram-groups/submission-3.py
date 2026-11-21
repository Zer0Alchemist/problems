class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dct = {}

        for n in strs:
            key = "".join(sorted(n))

            if key not in dct:
                dct[key] = [n]
            else:
                dct[key].append(n)

        return list(dct.values()) 
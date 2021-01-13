class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs:
            return [[""]]
        group_dict = collections.defaultdict(list)
        for word in strs:
            group_dict[''.join(sorted(word))].append(word)

        result = []
        for k in group_dict:
            result.append(group_dict[k])

        return result
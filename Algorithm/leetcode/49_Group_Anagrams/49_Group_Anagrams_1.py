class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:        
        group_dict = collections.defaultdict(list)
        for word in strs:
            group_dict[''.join(sorted(word))].append(word)

        return list(group_dict.values())
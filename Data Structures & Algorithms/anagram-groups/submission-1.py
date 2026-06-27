class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        #hashmap of sorted words : [act: [act, cat]
        seen = {}
        for word in strs:
            sorted_word = ''.join(sorted(word))
            if sorted_word in seen:
                seen[sorted_word].append(word)
            else:
                seen[sorted_word] = [word]
        
        return list(seen.values())
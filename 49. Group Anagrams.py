class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) # Make a hash map with alphabet patterns

        for s in strs:
            count = [0] *26 # an empty list of 26 space to store the character patterns

            for c in s:
                count[ord(c) - ord("a")] += 1 # ord is used to get the asci value of the character, here we store the frequecny of the alphabets i.e make pattern for each string - anagrams will same patterns
            
            res[tuple(count)].append(s) # with the pattern as key store different string with same patterns i.e anagrams under the same key. Since a list cannot be a key change that list to a tuple
        
        return res.values() # return just the values i.e the strings and not the keys i.e patterns.
#49. Group Anagrams
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #create a dictionary
        new_d = {}
        #iterate through all words in list
        for word in strs:
            #create keys for hash table (tuple)
            key = tuple(sorted(word))
            #create hash table
            new_d[key] = new_d.get(key,[]) + [word]
        return new_d.values()
        
            
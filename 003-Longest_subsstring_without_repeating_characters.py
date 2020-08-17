class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        #abc abcbb
        start = -1 
        max = 0
        d ={ }
        
        #Traverse through the s
        for i in range(len(s)):                                        
            if s[i] in d and d[s[i]] > start:
                start = d[s[i]] #儲存再次遇到的index
                d[s[i]]=i #更新key再次遇到的index
            else:
                d[s[i]]=i #更新key再次遇到的index
                if i - start > max: #因為index為0時 減去start, max要為1，所以起始值要設為-1
                    max = i - start             
        return max        
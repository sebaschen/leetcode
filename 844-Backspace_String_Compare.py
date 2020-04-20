#844. Backspace String Compare
class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        #create two empty string
        res_S = ""
        res_T = ""
        #if s != 's':
            #append s to string, if s != '', delete last alphabet in the string:
            #else : contatanate String:
        #Same for T:
        #Return if the two original Empty string is matched or not 
        
        for s in S:
            if s =='#':
                if res_S:
                    res_S = res_S[:-1]
            
            else:
                res_S+=s
        for t in T:
            if t =='#':
                if res_T:
                    res_T = res_T[:-1]
            else:
                res_T+=t
        
        return res_S == res_T                    
        
            
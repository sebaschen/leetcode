class Solution:
    def isHappy(self, n: int) -> bool: #n=19
        happy_set = set()
        while n != 1:
            n = sum([int(i) ** 2 for i in str(n)])
            if n in happy_set: #check if the number start repeat
                return False #if repeat --> False
            else:
                happy_set.add(n) #if haven't repeat, Add it to set to check later
        else:
            return True
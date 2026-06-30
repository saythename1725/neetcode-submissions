class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d={}
        if len(s)!=len(t):
            return False
        for ch in s:
            if ch in d:
                d[ch]+=1
            else:
                d[ch]=1
        for ch in t:
            if ch in d:
                d[ch]-=1
            else:
                return False
        for ch in d:
            if d[ch]!=0:
                return False
        return True


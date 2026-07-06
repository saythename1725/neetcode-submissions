class Solution:
    def isPalindrome(self, s: str) -> bool:
        # n=""
        # for ch in s:
        #     if ch.isalnum():
        #         n+=ch.lower()
        # if n==n[::-1]:
        #     return True
        # else:
        #     return False
        i=0
        j=len(s)-1
        while i<j:
            while i<j and not s[i].isalnum():
                i+=1
            while i<j and not s[j].isalnum():
                j-=1
            if s[i].lower()!=s[j].lower():
                    return False
            i+=1
            j-=1
        return True
        
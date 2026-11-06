class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s=[]
        for ch in tokens:
            if ch not in (["+","-","*","/"]):
                s.append(int(ch))
            else:
                b=s.pop()
                a=s.pop()
                if ch=="+":
                    result= a+b
                elif ch=="-":
                    result= a-b
                elif ch=="*":
                    result= a*b
                else:
                    result= int(a/b)
                s.append(result)
        return s[-1]
            
        
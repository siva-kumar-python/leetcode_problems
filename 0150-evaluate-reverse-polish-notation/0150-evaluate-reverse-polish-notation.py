class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens)==1:
            return int(tokens[0])
        res=[]
        print(int(6/-132))
        for i in tokens:
            if i in ["+", "-", "*", '/'] :
                f1=int(res.pop())
                f2=int(res.pop())
                if i=='+':
                    ans=f2+f1
                elif i=='-':
                    ans=f2-f1
                elif i=='*':
                    ans=f2*f1
                else:
                    ans=int(f2/f1)
                res.append(ans)
            else:
                res.append(i)
       
        return int(res[0])
class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
         bs=["electronics", "grocery", "pharmacy", "restaurant"]
        # ans=[]
        # for i in range(len(code)):
            # res=code[i]
            # if '_' in code[i]:
            #     res=code[i].replace('_','')
        #     if (code[i].isalnum() or res.isalnum()) and businessLine[i] in bs and isActive[i] :
        #         ans.append(code[i])
        # ans.sort()
        # return ans
         e=[]
         g=[]
         p=[]
         r=[]
         for i in range(len(code)):
             res=code[i]
             if '_' in code[i]:
                 res=(code[i].upper()).replace('_','')
             if isActive[i] and businessLine[i]=="electronics" and ((code[i].upper()).isalnum() or res.isalnum()or set(code[i])==set('_')):
                 e.append(code[i])
             if isActive[i] and businessLine[i]=="grocery" and ((code[i].upper()).isalnum() or res.isalnum()or set(code[i])== set('_')):
                 g.append(code[i])
             if isActive[i] and businessLine[i]=="pharmacy" and ((code[i].upper()).isalnum() or res.isalnum()or set(code[i])==set('_')):
                 p.append(code[i])
             if isActive[i] and businessLine[i]=="restaurant" and ((code[i].upper()).isalnum() or res.isalnum()or set(code[i])==set('_')):
                 r.append(code[i])
         e.sort()
         g.sort()
         p.sort()
         r.sort()
         return e+g+p+r
            
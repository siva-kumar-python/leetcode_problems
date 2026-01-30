class Solution:
    def partitionString(self, s: str) -> List[str]:
        seen=set()
        temp=''
        ans=[]
        for i in s:
            temp+=i
            if temp not in seen:
                seen.add(temp)
                ans.append(temp)
                temp=''
        return ans 
        
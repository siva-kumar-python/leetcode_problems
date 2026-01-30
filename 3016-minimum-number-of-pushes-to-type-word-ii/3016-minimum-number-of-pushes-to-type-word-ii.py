class Solution:
    def minimumPushes(self, word: str) -> int:
        s=collections.Counter(word)
        count=0
        ans=0
        temp=sorted(s.items() , key=lambda x:(x[1],x[0]), reverse=True)
        for i,j in temp:
            ans+=j*((count//8)+1)
            count+=1
        return ans
class Solution:
    def toggleLightBulbs(self, bulbs: list[int]) -> list[int]:
        b=[]
        for i in bulbs:
            if i not in b:
                b.append(i)
        
        ans=[]
        for i in b:
            c=bulbs.count(i)
            
            if c%2==1:
                ans.append(i)
            ans.sort()
        return ans

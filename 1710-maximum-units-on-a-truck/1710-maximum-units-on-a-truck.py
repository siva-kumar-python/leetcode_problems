class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        s=sorted(boxTypes, reverse=True, key=lambda x : x[1])
        ans=0
        for i in s:
            if truckSize>0:
                if i[0]>truckSize:
                    ans+=truckSize * i[1]
                else:
                    ans += i[0]*i[1]
                truckSize-=i[0]
            else:
                return ans
        return ans
    

          
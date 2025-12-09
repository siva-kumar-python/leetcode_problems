class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        if sum(costs)<=coins:
            return len(costs)
        if min(costs)>coins:
            return 0
        costs.sort()
        count=0
        ans=0
        for i in costs:
            ans+=i
            if ans>coins:
                ans-=i
            else:
                count+=1

           
        return count

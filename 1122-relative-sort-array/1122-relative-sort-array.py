class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        ans=[]
        ans1=[]
        for i in arr2:
            if i in arr1:
                ans+=[i]*arr1.count(i)
            else:
                ans1.append(i)
            
        ans1=[i for i in arr1 if i not in arr2]
        ans1.sort()
        return ans+ans1
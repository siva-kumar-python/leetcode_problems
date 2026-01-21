class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1=nums1
        self.nums2=nums2
        self.di={}
        for i in self.nums2:
            if i not in self.di.keys():
                self.di[i]=1
            else:
                self.di[i]+=1

    def add(self, index: int, val: int) -> None:
        num=self.nums2[index]
        self.di[num]-=1

        if num+val in self.di.keys():
            self.di[num+val]+=1
        else:
            self.di[val+num]=1
        self.nums2[index]+=val

        

    def count(self, tot: int) -> int:
        

        count=0
        for i in self.nums1:
            if tot-i in self.di.keys():
                count+=self.di[tot-i]
        return count
        


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        res=[]
        ans=''
        for i in digits:
            ans+=str(i)
        ans=int(ans)+1
        for i in str(ans):
            res.append(int(i))
        return res
        
        
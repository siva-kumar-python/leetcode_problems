class Solution(object):
    def __init__(self):
        self.ans=[]
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        n=str(n)
        temp=0
        for i in n:
            temp+=int(i)**2
        if temp==1:
            return True
        if temp not in self.ans:
            self.ans.append(temp)
            return Solution.isHappy(self,temp)
        else:
            return False
        
        
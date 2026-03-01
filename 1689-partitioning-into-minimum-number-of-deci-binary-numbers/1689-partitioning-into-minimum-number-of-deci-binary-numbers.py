class Solution:
    def minPartitions(self, n: str) -> int:
        m='9876543210'
        for i in m:
            if i in n:
                return int(i)

        #     m=max(m,int(i))
        # return m
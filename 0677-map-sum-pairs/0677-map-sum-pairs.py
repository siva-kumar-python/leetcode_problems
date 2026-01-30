class MapSum:

    def __init__(self):
        self.di={}
        

    def insert(self, key: str, val: int) -> None:
        self.di[key]=val
        

    def sum(self, prefix: str) -> int:
        ans=0
        for i,j in self.di.items():
            if i.startswith(prefix):
                ans+=j
        return ans

        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
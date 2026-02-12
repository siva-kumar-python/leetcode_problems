class Spreadsheet:

    def __init__(self, rows: int):
        self.di={}
        

    def setCell(self, cell: str, value: int) -> None:
        self.di[cell]=value 
        

    def resetCell(self, cell: str) -> None:
        if cell in self.di.keys():
            del(self.di[cell])

    def getValue(self, formula: str) -> int:
        s=formula[1:].split('+')
        if s[0].isdigit() and s[1].isdigit():
            return int(s[0])+int(s[1])
        if s[0].isdigit():
            return int(s[0])+self.di.get(s[1],0)
        if s[1].isdigit():
            return self.di.get(s[0],0)+int(s[1])
        else:
            return self.di.get(s[0],0)+self.di.get(s[1],0)
        


# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)
class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        di = {}
        min_elm = float('inf')
        for i in range(1, len(arr)):
            temp = arr[i] - arr[i-1]
            if temp not in di.keys():
                di[temp] =[[arr[i-1],arr[i]]]
            else:
                di[temp].append([arr[i-1],arr[i]])
            if temp<min_elm:
                min_elm=temp
        return di[min_elm] if min_elm != float('inf') else []


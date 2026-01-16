class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        
        if len(s) != len(goal):
            return False 

        if s != goal:
            diff = []
            for i in range(len(s)):
                if s[i] != goal[i]:
                    diff.append(i)
                if len(diff) > 2:
                    return False
            
            if len(diff) != 2:
                return False
            
            i, j = diff
            return s[i] == goal[j] and s[j] == goal[i]
        
        
        else:
            seen = set()
            for ch in s:
                if ch in seen:
                    return True
                seen.add(ch)
            return False

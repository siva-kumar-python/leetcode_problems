class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        mod = 10**9 + 7
        n = len(s)

        pref_mod = [0] * n       
        pref_sum = [0] * n       
        pref_cnt = [0] * n       

   
        pow10 = [1] * (n+1)
        for i in range(1, n+1):
            pow10[i] = (pow10[i-1] * 10) % mod

    
        for i, ch in enumerate(s):
            digit = int(ch)
            if ch != '0':
                pref_mod[i] = ((pref_mod[i-1] if i > 0 else 0) * 10 + digit) % mod
                pref_sum[i] = (pref_sum[i-1] if i > 0 else 0) + digit
                pref_cnt[i] = (pref_cnt[i-1] if i > 0 else 0) + 1
            else:
                pref_mod[i] = pref_mod[i-1] if i > 0 else 0
                pref_sum[i] = pref_sum[i-1] if i > 0 else 0
                pref_cnt[i] = pref_cnt[i-1] if i > 0 else 0

        res = []

        for l, r in queries:
          
            cnt = pref_cnt[r] - (pref_cnt[l-1] if l > 0 else 0)

            if cnt == 0:
                res.append(0)
                continue

            
            sum_digits = pref_sum[r] - (pref_sum[l-1] if l > 0 else 0)

            left_part = pref_mod[l-1] if l > 0 else 0
            x_mod = (pref_mod[r] - (left_part * pow10[cnt]) % mod + mod) % mod

            res.append((x_mod * sum_digits) % mod)

        return res

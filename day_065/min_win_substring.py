# https://leetcode.com/problems/minimum-window-substring/

from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t=="": 
            return ""
        
        countT = defaultdict(int)  # empty hash map
        window = defaultdict(int)  # empty hash map
        for c in t:
            countT[c] += 1
        
        have, need = 0, len(countT)
        result, res_len = [-1,-1], float('infinity')
        l = 0

        for r in range(len(s)):
            c = s[r]
            window[c] += 1
            
            if c in countT and window[c]==countT[c]:
                have += 1
            
            while have==need:
                # update our result
                if (r-l+1) < res_len:  # size of our current window
                    res = [l,r]
                    res_len = (r-l+1)

                window[s[l]] -= 1
                if s[l] in countT and window[s[l]]<countT[s[l]]:
                    have -= 1
                l += 1
# https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s):
        left_ptr = 0
        right_ptr = 0
        size = 0
        maximum = 0
        letters = [0]*100
        for i in range(len(s)):
            letters[ord(s[i]) - ord('a')] += 1
            right_ptr += 1
            size += 1
            if letters[ord(s[i]) - ord('a')] == 2:
                while letters[ord(s[i]) - ord('a')] == 2:
                    letters[ord(s[left_ptr]) - ord('a')] -= 1
                    left_ptr += 1
                    size -= 1
            maximum = max(maximum, size)

        return maximum
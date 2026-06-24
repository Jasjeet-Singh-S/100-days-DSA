# https://leetcode.com/problems/group-anagrams/

from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs):
        anagram_map = defaultdict(list)

        for str in strs:
            sorted_str = "".join(sorted(str))  # Sort the string to get the 'signature'
            anagram_map[sorted_str].append(str)  # Use the signature as the key and append the original string
        
        return list(anagram_map.values())


if __name__=="__main__":
    strs = ["eat","tea","tan","ate","nat","bat"]
    actual_output = Solution().groupAnagrams(strs)
    expected_output = [["bat"],["nat","tan"],["ate","eat","tea"]]
    if expected_output==actual_output:
        print("pass")
    else:
        print("fail")
        print(actual_output)
        # this tc fails because i didnt make the code so that the list can be in any order
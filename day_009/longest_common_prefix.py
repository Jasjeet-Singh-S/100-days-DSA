class Solution:
    def longestCommonPrefix(self, strs):
        first=strs[0]
        prefix=[]
        for str in strs[0:]:
            for i in range(min(len(first), len(str))):
                if(first[i]==str[i]):
                    prefix.append(first[i])
                else:
                    break
            first = ''.join(prefix)
            prefix.clear()
        return first

def main():
    strs_1 = ["flower","flow","flight"]
    expected_output_1 = "fl"
    strs_2 = ["dog","racecar","car"]
    expected_output_2 = ""

    solution = Solution()

    actual_output_1 = solution.longestCommonPrefix(strs_1)
    actual_output_2 = solution.longestCommonPrefix(strs_2)

    if(actual_output_1==expected_output_1 and actual_output_2==expected_output_2):
        print("pass")
    else:
        print("fail")
        print(actual_output_1)
        print(actual_output_2)

if __name__=="__main__":
    main()
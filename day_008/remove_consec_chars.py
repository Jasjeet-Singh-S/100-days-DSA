class Solution:
    def removeConsecutiveCharacter(self, s):
        prev = s[0]
        new = []
        new.append(prev)
        for char in s[0:]:
            if char==prev:
                continue
            else:
                prev = char
                new.append(char)
        output = ''.join(new)
        return output
    
def main():
    s_1 = "aabb"
    expected_output_1 = "ab" 
    s_2 = "aabaa"
    expected_output_2 = "aba"
    s_3 = "abcddcba"
    expected_output_3 = "abcdcba"

    solution = Solution()

    actual_output_1 = solution.removeConsecutiveCharacter(s_1)
    actual_output_2 = solution.removeConsecutiveCharacter(s_2)
    actual_output_3 = solution.removeConsecutiveCharacter(s_3)

    if(actual_output_1==expected_output_1 and actual_output_2==expected_output_2 and actual_output_3==expected_output_3):
        print("pass")
    else:
        print("fail")
        print(actual_output_1)
        print(actual_output_2)
        print(actual_output_3)

if __name__=="__main__":
    main()
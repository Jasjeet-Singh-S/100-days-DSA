class Solution:
    valid_letters = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    def digest(self, s):
        s = s.lower()
        result = ''
        for letter in s:
            if letter in self.valid_letters:
                result += letter
        return result

    def isPalindrome(self, s):
        s = self.digest(s)
        flag = True
        for i in range(int(len(s)/2)):
            if(s[i]==s[-i-1]):
                continue
            else:
                return False
        return True


def main():
    s_1 = "A man, a plan, a canal: Panama"
    expected_output_1 = True
    s_2 = "0P"
    expected_output_2 = False
    s_3 = " "
    expected_output_3 = True
    # print(s_1[0], s_1[-1])

    solution = Solution()
    actual_output_1 = solution.isPalindrome(s_1)
    actual_output_2 = solution.isPalindrome(s_2)
    actual_output_3 = solution.isPalindrome(s_3)

    if(actual_output_1==expected_output_1 and actual_output_2==expected_output_2 and actual_output_3==expected_output_3):
        print("pass")
    else:
        print("fail")
        print(actual_output_1, actual_output_2, actual_output_3)

if __name__ == "__main__":
    main()
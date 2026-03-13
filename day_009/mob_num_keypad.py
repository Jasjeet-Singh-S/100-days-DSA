class Solution:

    dict = {"a":"2", "b":"22", "c":"222", "d":"3", "e":"33", "f":"333", "g":"4",
            "h":"44", "i":"444", "j":"5", "k":"55", "l":"555", "m":"6", "n":"66",
            "o":"666", "p":"7", "q":"77", "r":"777", "s":"7777", "t":"8", "u":"88",
            "v":"888", "w":"9", "x":"99", "y":"999", "z":"9999", " ":"0"}

    def printSequence(self,S):
        result = ""
        for letter in S:
            result += self.dict[letter.lower()]
        return result



def main():
    s_1 = "GFG"
    expected_output_1 = 43334
    s_2 = "HEY U"
    expected_output_2 = 4433999088

    solution = Solution()

    actual_output_1 = solution.printSequence(s_1)
    actual_output_2 = solution.printSequence(s_2)

    if(expected_output_1==actual_output_1 and expected_output_2==actual_output_2):
        print("pass")
    else:
        print("fail")
        print(actual_output_1)
        print(actual_output_2)


if __name__=="__main__":
    main()
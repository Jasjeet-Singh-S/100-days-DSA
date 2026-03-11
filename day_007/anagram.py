class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letter_count_s = {letter: 0 for letter in 'abcdefghijklmnopqrstuvwxyz'}
        letter_count_t = {letter: 0 for letter in 'abcdefghijklmnopqrstuvwxyz'}

        for letter in s:
            letter_count_s[letter] += 1
        for letter in t:
            letter_count_t[letter] += 1
        if(letter_count_s==letter_count_t):
            return True
        else:
            return False
        
def main():
    s1 = "hello"
    t1 = "olleh"
    expected_solution_1 = True
    s2 = "anagram"
    t2 = "nagaram"
    expected_solution_2 = True
    s3 = "rat"
    t3 = "car"
    expected_solution_3 = False

    solution = Solution()
    
    actual_solution_1 = solution.isAnagram(s1, t1)
    actual_solution_2 = solution.isAnagram(s2, t2)
    actual_solution_3 = solution.isAnagram(s3, t3)

    if(expected_solution_1==actual_solution_1 and expected_solution_2==actual_solution_2 and expected_solution_3==actual_solution_3):
        print("pass")
    else:
        print("fail")


if __name__ == "__main__":
    main()
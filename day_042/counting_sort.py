# https://www.geeksforgeeks.org/problems/counting-sort/1

class Solution:
    def countSort(self, string):
        if not string:
            return []
        
        count = 26 * [0]
        arr = self.string_to_int(string)
        for i in range(len(arr)):
            count[arr[i]] += 1
        reformat = []
        i = 0
        while i<26:
            if count[i]>0:
                reformat.append(i)
                count[i] -= 1
            else:
                i += 1
        string = self.int_to_string(reformat)
        return string

    def string_to_int(self, string):
        out = []
        for ch in string:
            if 'a' <= ch <= 'z':
                out.append(ord(ch) - ord('a'))
            else:
                raise ValueError(f"Unsupported character: {ch!r}")
        return out
    
    def int_to_string(self, int_array):
        out = []
        for num in int_array:
            if 0 <= num <= 25:
                out.append(chr(num + ord('a')))
            else:
                raise ValueError(f"Unsupported integer: {num}. Must be between 0 and 25 inclusive.")
        return "".join(out)


if __name__=="__main__":
    sol = Solution()
    print(sol.countSort("hello"))
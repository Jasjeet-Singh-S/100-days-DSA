# https://www.geeksforgeeks.org/problems/common-elements1132/1

class Solution:
    def commonElements(self, a, b, c):
        out = []
        i1, i2, i3 = 0, 0, 0
        a_len = len(a)
        b_len = len(b)
        c_len = len(c)
        while i1<a_len and i2<b_len and i3<c_len:
            if a[i1] == b[i2] == c[i3]:
                if not out or out[-1] != a[i1]:
                    out.append(a[i1])
                i1 += 1
                i2 += 1
                i3 += 1
            elif a[i1] < b[i2]:
                i1 += 1
            elif b[i2] < c[i3]:
                i2 += 1
            else:
                i3 += 1

        return out 



if __name__=="__main__":
    arr_1 = [1,2,3,4,5,6]
    arr_2 = [1,3,6,9,12]
    arr_3 = [1,6,12,18]

    sol = Solution()

    result = sol.commonElements(arr_1, arr_2, arr_3)

    print(result)
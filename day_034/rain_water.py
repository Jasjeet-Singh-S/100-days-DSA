class Solution:
    def trap(self, height):
        water = 0 
        seen = [False] * len(height)
        for i in range(len(height)):
            index = self.next_max(height, i)
            minimum = min(height[i], height[index])
            for k in range(i+1, index):
                if seen[k] == False:
                    water += minimum-height[k]
                    seen[k] = True
        return water
            

    def next_max(self, height, curr_index):
        max = 0
        max_index = curr_index
        for i in range(curr_index+1, len(height)):
            if height[i]>max:
                max = height[i]
                max_index = i
            if max>=height[curr_index]:
                return max_index
            
        return max_index
    


def main():
    arr_1 = [0,1,0,2,1,0,1,3,2,1,2,1]
    expected_output_1 = 6
    arr_2 = [4,2,0,3,2,5]
    expected_output_2 = 9 

    sol = Solution()

    actual_answer_1 = sol.trap(arr_1)
    actual_answer_2 = sol.trap(arr_2)

    if(actual_answer_1==expected_output_1 and actual_answer_2==expected_output_2):
        print("pass")
    else:
        print("fail")
        print(actual_answer_1)
        print(expected_output_1)
        print(actual_answer_2)
        print(expected_output_2)


if __name__=="__main__":
    main()
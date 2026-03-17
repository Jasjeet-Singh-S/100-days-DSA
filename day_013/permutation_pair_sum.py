class Solution:
    def isPossible(self, k, arr1, arr2):
        self.quick_sort(arr1, 0, len(arr1)-1)
        self.quick_sort(arr2, 0, len(arr2)-1)
        for i in range(min(len(arr1), len(arr2))):
            if(arr1[i]+arr2[-i-1]<k):
                return False
        return True

    def partition(self, arr, low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if(arr[j]<pivot):
                i+=1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i+1
    
    def quick_sort(self, arr, low, high):
        if low<high:
            p = self.partition(arr, low, high)
            self.quick_sort(arr, low, p-1)
            self.quick_sort(arr, p+1, high)


def main():
    arr_1 = [2, 1, 3]
    arr_2 = [7, 8, 9]
    k_1 = 10
    expected_output_1 = True
    arr_3 = [1, 2, 2, 1]
    arr_4 = [3, 3, 3, 4]
    k_2 = 5
    expected_output_2 = False

    solution = Solution()

    actual_output_1 = solution.isPossible(k_1, arr_1, arr_2)
    actual_output_2 = solution.isPossible(k_2, arr_3, arr_4)

    if(expected_output_1==actual_output_1 and expected_output_2==actual_output_2):
        print("pass")
    else:
        print("fail")
        print(actual_output_1)
        print(actual_output_2)


if __name__=="__main__":
    main()
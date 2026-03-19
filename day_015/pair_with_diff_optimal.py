class Solution:
    def findPair(self, arr, x):
        length = len(arr)
        arr.sort()
        # self.quick_sort(arr, 0, length-1)
        # i though quick sort was the fastest, but apprently pythons built-in timesort is faster which is why this code passes but the commented out code doesnt.
        for i in range(length):
            target = arr[i]+x
            if self.binarySearch(arr, i+1, length-1, target):
                return True
        return False

    # def partition(self, arr, low, high):
    #     pivot = arr[high]
    #     i = low - 1
    #     for j in range(low, high):
    #         if(arr[j]<pivot):
    #             i+=1
    #             arr[i], arr[j] = arr[j], arr[i]
    #     arr[i + 1], arr[high] = arr[high], arr[i + 1]
    #     return i+1
    
    # def quick_sort(self, arr, low, high):
    #     if low<high:
    #         p = self.partition(arr, low, high)
    #         self.quick_sort(arr, low, p-1)
    #         self.quick_sort(arr, p+1, high)
    
    def binarySearch(self, arr, left, right, key):
        while left <= right:
            mid = left + (right - left) // 2
            if arr[mid] == key:
                return True
            elif arr[mid] < key:
                left = mid + 1
            else:
                right = mid - 1
        return False


def main():
    arr_1 = [5, 20, 3, 2, 5, 80]
    x_1 = 78
    expected_output_1 = True
    arr_2 = [90, 70, 20, 80, 50]
    x_2 = 45
    expected_output_2 = False

    solution = Solution()

    actual_output_1 = solution.findPair(arr_1, x_1)
    actual_output_2 = solution.findPair(arr_2, x_2)

    if(expected_output_1==actual_output_1 and expected_output_2==actual_output_2):
        print("pass")
    else:
        print("fail")
        print(actual_output_1)
        print(actual_output_2)


if __name__ == "__main__":
    main()
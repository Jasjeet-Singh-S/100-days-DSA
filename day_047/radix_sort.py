def radixSort(arr, n):
    rad_array = [[], [], [], [], [], [], [], [], [], []]
    for i in range(3):  # since 1<=N<=10^3
        for k in range(n):
            num = arr.pop(0)
            val = (num//pow(10,i))%10  # way to extract the digit we want
            rad_array[val].append(num)
        for sub_list in rad_array:
            while sub_list:
                arr.append(sub_list.pop(0))
    return arr


if __name__=="__main__":
    arr = [170, 45, 75, 90, 802, 24, 2, 66]
    expected_output = [2, 24, 45, 66, 75, 90, 170, 802]
    if expected_output==radixSort(arr, 8):
        print("pass")
    else:
        print(radixSort(arr, 8))
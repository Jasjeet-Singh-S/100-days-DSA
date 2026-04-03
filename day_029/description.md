# repeated and missing value
since we are given an unsorted tuple of integers of 1 to n and we want to find the missing number and the repeated number we can approach this with 2 for loops, one to find the repeated number and the second to find the missing number (i tried to do it in a single for loop but couldnt do it)

ideally this problem needs to be solved with 0 extra space but i couldnt come up with a solution like that, ill have to check youtube for that tomorrow, so what i came up with was; convert the tuple into an array and sort the array since you cant sort the tuple itself
```
arr = list(A)
arr.sort()
```
the the first for loop iterates from position 0 to n-1 and checks if the number is repeated `arr[i+1]!=arr[i]+1` and at the same time the we have to check this condition isnt true due to having encounteres the missing number with `arr[i+1]!=arr[i]+2`
```
for i in range(len(arr)-1):
    if arr[i+1]!=arr[i]+1 and arr[i+1]!=arr[i]+2:
        output.append(arr[i+1])
        break
    i+=1
```
then we use a second for loop to find the missing number 
```
for i in range(len(arr)-1):
    if arr[i+1]==arr[i]+2:
        output.append(arr[i]+1)
```
and then finally we check for edge cases where the first or the last number is missing as our loop will miss that 
```
if arr[0]!=1:
    output.append(1)
if arr[len(arr)-1]!=len(arr):
    output.append(len(arr))
```

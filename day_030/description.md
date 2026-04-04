# Repeated and Missing Number 
ok so the previous approach we used had to linear loops and a sort that makes it O(N*LogN) and we used O(N) space. What we want is O(N) time and O(1) space. For that we will use a clever approach as follows:
## Steps
- let the read only array be `arr_1=[1,2,3,....n]` in some unsorted manner
- let there be some expected array `arr_2=[1,2,3....n]` that is the actual correct array from 1 to n
- let the sum of the given array be `a=sum(arr_1)`
- let the sum of the expected array be `b=sum(arr_2)`
- let the sum of squares of the given array be `a_s=sum(elemwise(square(arr_1)))`
- let the sum of squares of the expected array be `b_s=sum(elemwise(square(arr_2)))`
- let the difference between the two be `diff=a-b`, this isolated the repeated number and missing number in the form of `repeated-missing`
- let the difference between the squares of two be `sq_diff=a_s-b_s`, this isolates the repeated number and missing number in the form of `repeated**2-missing**2`
- we can create a third equation by exploting the existing two equations: `repeated+missing=(repeated**2-missing**2)/(repeated-missing)`
- and then extract the missing and repeated number by solving the set of linear equations `repeated+missing=something` and `repeated-missing=something`
- in the end we return the value `[repeated, missing]`
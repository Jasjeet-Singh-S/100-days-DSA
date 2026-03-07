still sick so not gonna document much. Started out with :
```
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        flag = False
        for i in range(len(nums)):
            for k in range(len(nums)-i):
                if i!=k+i:
                    if nums[i] == nums[k+i]:
                        flag = True
                        return flag
        return flag
```
Got time limit exceeded. Shifted to this. hooray
```
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
```

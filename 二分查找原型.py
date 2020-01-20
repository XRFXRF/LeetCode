class Solution:
    def search(self, nums, target: int) -> int:
        if len(nums)==0:
            return -1
        left=0
        right=len(nums)-1
        while left<=right:#小于等于
            mid=(left+right)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]<=target:
                left=mid+1#记得要移动，不然最后可能原地不动
            else:
                right=mid-1
        return -1

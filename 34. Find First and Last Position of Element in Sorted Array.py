class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def findLeft (nums, target):
            left, right = 0, len(nums) -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return left
        
        def findRight (nums, target):
            left, right = 0, len(nums) -1

            while left <= right:
                mid = (left + right) // 2
                if nums[mid] <= target:
                    left = mid + 1
                else:
                    right = mid - 1
            return right

        left, right = findLeft(nums, target), findRight(nums, target)

        return [left, right] if left <= right else [-1,-1]
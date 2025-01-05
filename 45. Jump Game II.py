class Solution:
    def jump(self, nums: List[int]) -> int:
        # Greedy Approach
        n = len(nums)
        jumps = 0
        current_end = 0
        farthest = 0

        for i in range(n - 1):
            # Update the farthest point reachable
            farthest = max(farthest, i + nums[i])
            
            # If we have reached the end of the current jump
            if i == current_end:
                jumps += 1
                current_end = farthest
                
                # If the current end has reached or passed the last index
                if current_end >= n - 1:
                    break

        return jumps
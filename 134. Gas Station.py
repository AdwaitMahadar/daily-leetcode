class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_gas = total_cost = 0
        start = gas_left = 0
        
        for i in range(len(gas)):
            total_gas += gas[i]
            total_cost += cost[i]
            gas_left += gas[i] - cost[i]
            
            # If gas_left is negative, reset starting point
            if gas_left < 0:
                start = i + 1
                gas_left = 0
        
        # Check if total gas is at least the total cost
        return start if total_gas >= total_cost else -1
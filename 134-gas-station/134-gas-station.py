class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        # Takes more gas to do a revolution than there is in the stations
        if sum(cost) > sum(gas):
            return -1
        
        n = len(gas)
        startingIndex = 0
        while startingIndex < n:
            # Attempts to compelete a trip around the stations
            currentGasLevel = 0
            for i in range(n):
                j = (i + startingIndex) % n
                currentGasLevel += gas[j]   # Fill up at station j
                
                currentGasLevel -= cost[j]  # Cost to get to station (j+1)
                
                # Can the car the make it to the next station
                if currentGasLevel < 0:
                    startingIndex = j + 1
                    break
                    
            else:
                # Only executed if it made a full revolution
                return startingIndex
        
        # Returns if there is no valid index
        return -1
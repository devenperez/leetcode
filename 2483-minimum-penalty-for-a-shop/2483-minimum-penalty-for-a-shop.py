class Solution:
    def bestClosingTime(self, customers: str) -> int:
        penalty = 0
        minPenalty = 0
        bestHour = 0

        for hour, hasCustomers in enumerate(customers):
            if hasCustomers == "Y":
                penalty -= 1
            else:
                penalty += 1

            if penalty < minPenalty:
                minPenalty = penalty
                bestHour = hour + 1

        return bestHour
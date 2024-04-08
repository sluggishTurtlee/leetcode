class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        customers = len(accounts)
        banks = len(accounts[0])
        richest = []
        wealth = 0

        for i in range(customers):
            for j in range(banks):
                wealth += accounts[i][j]
            
            richest.append(wealth)
            wealth = 0
            
        richest.sort()

        return richest[customers -1]

class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        l = len(hours)
        output = 0

        for i in range(l):
            if hours[i] >= target:
                output += 1
            else: continue

        return output

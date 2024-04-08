class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        groups, result = collections.defaultdict(list), []
        
        for i, size in enumerate(groupSizes):
            groups[size].append(i)

            if len(groups[size]) == size:
                result.append(groups.pop(size))

        return result

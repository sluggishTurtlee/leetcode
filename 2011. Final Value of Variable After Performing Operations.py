class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        l = len(operations)
        increments = operations.count("X++") + operations.count("++X")
        decrements = operations.count("X--") + operations.count("--X")

        value = increments*(1) + decrements*(-1)
        
        return value

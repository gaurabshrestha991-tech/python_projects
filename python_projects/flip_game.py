class Solution:
    def generatePossibleNextMoves(self, currentState: str) -> list[str]:
        result = []

        for i in range(len(currentState) - 1):
            if currentState[i:i + 2] == "++":
                new_state = (
                    currentState[:i]
                    + "--"
                    + currentState[i + 2:]
                )
                result.append(new_state)

        return result

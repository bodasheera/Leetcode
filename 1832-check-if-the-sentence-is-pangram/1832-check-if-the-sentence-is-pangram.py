class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        
        counter = [0] * 26

        for c in sentence:

            counter[ord(c) - ord('a')] += 1

        return False if min(counter) == 0 else True


class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        
        max_words = 0

        for sentence in sentences:

            spaces = 0
            for c in sentence:
                if c == ' ':
                    spaces += 1

            max_words = max(max_words, spaces + 1)

        return max_words

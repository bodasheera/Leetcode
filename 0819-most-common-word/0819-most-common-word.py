from collections import Counter

class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        

        cleaned_para = ""
        for c in paragraph:
            if c.isalpha():
                cleaned_para+= c.lower()
            elif cleaned_para and cleaned_para[-1] != " ":
                    cleaned_para += ' '

        para_list = cleaned_para.split(" ")

        freq = Counter(para_list)

        max_f = -1
        res = ""

        for word in freq:

            if word not in banned and freq[word] > max_f:
                max_f = freq[word]
                res = word

        return res
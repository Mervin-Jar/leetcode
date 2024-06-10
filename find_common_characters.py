from typing import List
from collections import Counter
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        min_frequency_words = Counter(words[0])
        print(min_frequency_words)
        for word in words:
            min_frequency_words &= Counter(word)
        return list(min_frequency_words.elements())
    

d= Solution()
d.commonChars(["bella","label","roller"])
d.commonChars(["cool","lock","cook"])
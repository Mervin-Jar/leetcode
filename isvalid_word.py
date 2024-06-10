class Solution:
    def isValid(self, word: str) -> bool:
        vowels = 'aeiou'
        vowels += vowels.upper() 
        consonants = 'qwrtyplkjhgfdszxcvbnm'
        consonants += consonants.upper()
        allowed = vowels + consonants + '0123456789'
        
        if len(word) < 3 : return False
        has_consonants = False
        has_vowels = False
        #else:
        for c in word:
            if c in vowels: 
                has_vowels=True
            if c in consonants:
                has_consonants=True
            elif c not in allowed:
                return False
        return has_vowels and has_consonants
d= Solution()
print(d.isValid("234Adas"))
print(d.isValid("a3$e"))

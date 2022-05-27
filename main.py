# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


from typing import Counter

def find_anagrams(word, anagram):
    #checking if both words have same length
    if len(word) == len(anagram):
        #checking the number of times a letter exist and comparing both agurments
        if(Counter(word) == Counter(anagram)):
            return True
        else:
            return False
    else:
        return False


print(find_anagrams("below", "elbow"))

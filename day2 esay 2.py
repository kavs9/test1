string = input()
vowels = "aeiouAEIOU"
consonants="bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
count = sum(string.count(vowel) for vowel in vowels)
print(count)
count=sum(string.count(consonants)for consonants in consonants)
print(count)

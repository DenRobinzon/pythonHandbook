from sys import stdin

words = stdin.read().split()
palindromes = set(word for word in words if word.lower() == word.lower()[::-1])
print(*sorted(palindromes), sep='\n')

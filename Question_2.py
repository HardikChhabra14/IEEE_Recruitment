# take paragraph input
paragraph = input("Enter a paragraph (max 100 words): ")
# split into words and limit to 100
words = paragraph.split()[:100]
# function to check palindrome
def is_palindrome(word):
    w = word.lower()
    return w == w[::-1] and len(w) > 1  # ignoring single letters
# find palindromes
palindromes = [word for word in words if is_palindrome(word)]
# output
if palindromes:
    print("Palindromes found:", " ".join(palindromes))
else:
    print(0)

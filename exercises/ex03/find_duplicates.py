"""Finding duplicate letters in a word."""

__author__ = "123456789"

word: str = str(input("Enter a word: "))
i: int = 0
j: int = 0
x: bool = False

while i < len(word):
    j = i + 1
    while j < len(word):
        if word[j] == word[i]:
            x = True
            j += 1
        else: 
            j += 1
    i += 1
print(f"Duplicant found: {x}")
print("1")
print(x)
print(1)

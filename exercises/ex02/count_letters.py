"""Counting letters in a string."""

__author__ = "ENTER YOUR 9-DIGIT PID HERE"


# Begin your solution here...
letter: str = input("What letter do you want to search for?: ")
word: str = input("Enter a word: ")
i: int = 0 
count: int = 0


while i < len(word):
    if letter == word[i]:
        count += 1
        i += 1
    else:
        i += 1
print(f"Count: {count}")
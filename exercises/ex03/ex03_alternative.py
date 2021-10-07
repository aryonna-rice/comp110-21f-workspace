word: str = str(input("Enter a word: "))
i: int = 0
j: int = 0
x: bool = False
p: int = 0 


for characters in word:
    i = 0
    for character in characters:
        if character == word[i + 1]:
            x = True
            i += 1
        else: 
            i += 1
print(x)
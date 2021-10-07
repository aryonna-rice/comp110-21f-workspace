"""Drawing forests in a loop."""

__author__ = "123456789"

# The string constant for the pine tree emoji
TREE: str = '\U0001F332'

number: int = int(input("How many trees do you want? :"))
i: int = 0

result: str = ""

if number == 0:
    print('No trees')
else:
    while i < number:
        result = result + TREE
        print(result)
        i += 1 
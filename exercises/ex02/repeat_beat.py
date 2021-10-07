"""Repeating a beat in a loop."""

__author__ = "ENTER YOUR 9-DIGIT PID HERE"


beat: str = input("What beat do you want to repeat?")
time: int = int(input("How many times?: "))
i: int = 0
result: str = ""

if time < i:
    print('No beat...')
else:
    while i < time:
        if i == (time - 1):
            result = result + beat
            i += 1
            print(result)
        else: 
            result = result + (beat + " ")
            i += 1
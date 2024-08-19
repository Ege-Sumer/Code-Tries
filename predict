import random
import time

print("""**************************

Welcome to the Number Prediction Program 
Choose a number between 1 and 70 
Your right to guess is 13

**************************
"""
)
s = random.randint(1,70)

t_h = 13

while True:
    t = int(input("Input a number:"))

    if t < s:
        print("Pick a bigger number")
        t_h -= 1
        time.sleep(0.5)

    elif t > s:
        print("Pick a smaller number")
        t_h -= 1
        time.sleep(0.5)

    else:
        print("Nice Prediction")
        break
    if t_h == 0:
        print("Your Guess Right has run out")

        break

#Remember to use the random module
#Hint: Remember to import the random module here at the top of the file. 🎲
import random
#Write the rest of your code below this line 👇

random_side = random.randint(0, 1)
if random_side == 1:
    print("Heads")
else:
    print("Tails")
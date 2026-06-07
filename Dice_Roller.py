import random

total = 0
def dice_roller():
    print("Rolling the dice...")
    return random.randint(1, 6)
if __name__ == '__main__':
    print("Welcome to the Dice Roller!")
    number = input("How many dice do you want to roll? ")
    for i in range(int(number)):
        result = dice_roller()
        total += result 
        print(f"You rolled a {result}!")
    print("Your total is:", total)
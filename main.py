import random

ans = random.randint(1, 100)
counter = 0
while (True):
    print("Enter a number between 1 and 100: ", end= "")
    value = input()
    try:
        value = int(value)
        if (value < 1 or value > 100):
            print("The number must be between 1 and 100")
            print("try again")
            continue
        
        if value == ans:
            print(f"you guessed correctly in {counter} try")
            break
        elif value > ans:
            print("Too big!")
            counter += 1
        else:
            print("Too Small!")
            counter += 1
    except(ValueError):
        print("invalid input")
        print("try again")


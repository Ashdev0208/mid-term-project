import random 

def guess_number():
    counter = 0
    number = random.randint(1,100)
    result = {}

    while True:
        guess = input("please enter a number from 1 to 100: ")
        if not guess.isdigit():
            print("please enter number only between 1 to 100")
            continue
        
        guess = int(guess)
        counter += 1
        if guess <= 0 or guess > 100:
            print("follow the rules")
            continue
        elif guess < number:
            print("cold")
        elif guess > number :
            print("hot")
        else: 
            print(f"woooww, you have found the Number({number}) in the {counter} attempts")
            result["random_number"] = number
            result["counter"] = counter
            break
    return result
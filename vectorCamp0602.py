#
#
#
def numberguesser():
    import random
    number = random.randint(1, 100)
    guess = 0
    guesses = 5
    while guess != number:
        guess = int(input("Guess a number between 1 and 100:\n"))
        if guess < number:
            print("Too low! Try again.")
            guesses -= 1
            print(f"You have {guesses} guesses left.")
        elif guess > number:
            print("Too high! Try again.")
            guesses -= 1
            print(f"You have {guesses} guesses left.")  
    print("Congratulations! You've guessed the number!")


def heron():
    import math
    domain = int(input("Please enter the number you want to get the square root out of\n"))
    square_root = math.isqrt(domain)
    a = float(input("enter your first side\n"))
    while True:
        b = float(domain / a)
        print(f"the first side is {a}",)
        print(f"the second side would make {b}")
        print(f"{a} times {b} would make {a*b}")
        
        absolute_deviation = abs(a - b)
        print(f"the absolute deviation is {absolute_deviation}")
        relative_deviation = absolute_deviation / a
        print(f"the relative deviation makes {relative_deviation}")
        if relative_deviation <= 0.01 and relative_deviation >= -0.01:
            print(f"congrats! we have gotten the square root of {domain}")
            break
        if relative_deviation > 0.01 or relative_deviation < -0.01:
            print(f"unfortunately, we have not gotten the square root of {domain} yet.")
            a = (a + b) / 2
            continue
        
def lists():
    list = ["hallo", "welt", "python", "ist", "toll"]
    for i in list:
        print(f"länge des wortes {[i]} ist: {len(i)}")
lists()  
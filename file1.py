import random

number = random.randint(1, 100)
print("hey there fellas! your job is to guess the number in 5 attemps! ggs!")
attemps = 5
while attemps > 0:
    guess = int(input("enter your guess: "))
    if guess == number:
        print("congratulations! you guessed the number!")
        break
    elif guess < number:
        print(f"too low! try again! you have {attemps} attempts left.")
        attemps -= 1
    else:
        print(f"too high! try again! you have {attemps} attempts left.")
        attemps -= 1

print("game over! you ran out of attempts!")
print("the number was:", number)


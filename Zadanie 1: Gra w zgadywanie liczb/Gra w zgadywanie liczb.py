from random import randint

computer_number = randint(1, 100)
while True:
    try:
        number = float(input("Guess the number: "))
        if number < computer_number:
            print("Too small!")
        elif number > computer_number:
            print("Too big!")
        else:
            print("You win!")
            break
    except ValueError:
     print("It's not a number!")

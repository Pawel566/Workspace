import random

computer_numbers = random.sample(range(1, 50), 6)
my_numbers = []
while len(my_numbers) < 6:
    try:
        lotto = int(input("Enter your lucky number from 1 to 49: "))
        if lotto > 0 and lotto < 50:
            if lotto not in my_numbers:
                my_numbers.append(lotto)
            else:
                print("This number was given. Select another!")
        else:
            print("Enter your lucky number from 1 to 49: ")
    except ValueError:
        print("It's not a number!")
my_numbers.sort()
print("Your numbers are: ", my_numbers)
computer_numbers.sort()
print("Lucky numbers are: ", computer_numbers)
your_numbers = [lotto for lotto in my_numbers if lotto in computer_numbers]
print("You got the numbers: ",your_numbers)


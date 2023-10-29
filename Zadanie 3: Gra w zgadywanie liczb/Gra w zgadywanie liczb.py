def guess_the_number():
    print("Imagine number for 1 to 1000.")
    print("Press Enter to continue:")
    input()
    test = 1
    min_number = 1
    max_number = 1000
    your_answer = ""
    while your_answer != "You won!" and test < 10:
        computer_number = ((max_number - min_number) // 2) + min_number
        print(f"This number is: {computer_number}")
        your_answer = input("Is it 'Too small', 'Too big', or 'You won!? ")
        if your_answer.lower() == "too small":
            min_number = computer_number + 1
        elif your_answer.lower() == "too big":
            max_number = computer_number - 1
        test += 1
    else:
        your_answer = "You won!"
        print(f"Congratulations! It is {computer_number}")

if __name__ == '__main__':
    guess_the_number()


from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/", methods=['GET'])
def start():
    return render_template('image.html')

@app.route("/game", methods=['GET', 'POST'])
def guess_the_number():
    min_number = 1
    max_number = 1000
    computer_number = ((max_number - min_number) // 2) + min_number
    if request.method == 'POST':
        your_answer = request.form.get('your_answer')
        if your_answer == 'too big':
            computer_number = computer_number - 1
        elif your_answer == 'too small':
            computer_number = computer_number + 1
        else:
            your_answer = 'you win'
            return (f"I won it is {computer_number}!")








if __name__ == '__main__':
    app.run(debug=True)
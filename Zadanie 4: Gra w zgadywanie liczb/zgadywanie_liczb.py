from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/", methods=['GET'])
def start():
    return render_template('image.html')

@app.route("/game", methods=['GET'])
def guess_the_number():
    min_number = 1
    max_number = 1000
    computer_number = ((max_number - min_number) // 2) + min_number
    return  render_template('game.html')


@app.route("/end", methods=['GET'])
def computer_won():
    messeage = f("I won! It is {computer number}")
    return render_template('end.html', messeage=messeage)

if __name__ == '__main__':
    app.run(debug=True)
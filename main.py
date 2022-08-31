from flask import Flask
from random import randint
app = Flask(__name__)
actual_num = randint(0, 9)
@app.route('/')
def guess_number():
    return f'<h1>Guess A Number Between 0 to 9</h1>' \
           '<img src = "https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">'

@app.route('/<int:number>')
def check(number):

    if number == actual_num:
        return '<h2> you got it </h2>' \
               '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif">'
    elif number > actual_num:
        return '<h2> Too High.</h2>' \
               '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif">'
    else:
        return '<h2> Too Low.</h2>' \
               '<img src= "https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif" >'

if __name__ == "__main__":
    app.run(debug=True)



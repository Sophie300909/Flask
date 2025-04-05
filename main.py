import json

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/<word>')
@app.route('/index/<word>')
def index(word):
    return render_template('base.html', title=word)

@app.route('/answer')
@app.route('/auto_answer')
def answer():
    with open("answers.json", "rt", encoding="utf8") as f:
        answers_list = json.loads(f.read())
    print(answers_list)
    return render_template('auto_answer.html', answers=answers_list)

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
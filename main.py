from flask import Flask, render_template

app = Flask(__name__)

@app.route('/<word>')
@app.route('/index/<word>')
def index(word):
    return render_template('base.html', title=word)


@app.route('/training/<prof>')
def training(prof):
    return render_template('training.html', prof=prof)

@app.route('/list_prof/<list>')
def list_prof(list):
    return render_template('list_prof.html', param=list)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
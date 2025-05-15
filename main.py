from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('base.html')


@app.route('/table/<person>/<age>')
def table(person, age):
    age = int(age)
    if age < 21:
        photo = '/static/img/small.jpg'
    else:
        photo = '/static/img/big.png'
    if person == 'male':
        if age < 21:
            color = 'DeepSkyBlue'
        else:
            color = 'LightSkyBlue'
    else:
        if age < 21:
            color = 'MistyRose'
        else:
            color = 'Pink'
    return render_template('astronauts.html', photo=photo, color=color)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
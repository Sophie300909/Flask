from flask import Flask

app = Flask(__name__)


@app.route('/')
def title():
    return "Missiya"

@app.route('/results/<nickname>/<int:level>/<float:rating>')
def choice(nickname, level, rating):
    return f'''<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
                      </head>
                        <title>Результаты</title>
                      </head>
                      <body>
                        <h1>Результаты отбора</h1>
                      <h2>Претендента на участие в миссии {nickname}:</h2>
                        <div class="alert alert-success" role="alert">
                            <h4 class="alert-heading">Поздравляем! Ваш рейтинг после {level} этапа отбора</h4>
                        </div>
                        <div>
                            <strong>составляет {rating}!</strong>
                        </div>
                        <div class="alert alert-warning f" role="alert">
                            <h4 class="alert-heading">Желаем удачи!</h4>
                        </div>
                      </body>
                    </html>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
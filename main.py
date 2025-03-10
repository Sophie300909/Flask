from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def title():
    return "Missiya"

@app.route('/promotion_image')
def choice():
    return f'''<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
                        <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                      </head>
                        <title>Колонизация</title>
                      </head>
                      <body>
                        <h1>Жди нас Марс!</h1>
                        <img src="{url_for('static', filename='img/mars.png')}" 
           alt="здесь должна была быть картинка, но не нашлась">
                         <div class="alert alert-secondary" role="alert">
                            <h4 class="alert-heading">Человечество вырастает из детства.</h4>
                        </div>
                         <div class="alert alert-success" role="alert">
                            <h4 class="alert-heading">Человечеству мала одна планета.</h4>
                        </div>
                        <div class="alert alert-secondary" role="alert">
                            <h4 class="alert-heading">Мы сделаем обитаемыми безжизненные пока планеты<./h4>
                        </div>
                        <div class="alert alert-warning" role="alert">
                            <h4 class="alert-heading">И начнём с Марса!</h4>
                        </div>
                        <div class="alert alert-danger" role="alert">
                            <h4 class="alert-heading">Присоединяйся!</h4>
                        </div>
                      </body>
                    </html>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
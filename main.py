from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def title():
    return "Missiya"

@app.route('/choice/<planet_name>')
def choice(planet_name):
    return f'''<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
                      </head>
                        <title>Варианты выбора</title>
                      </head>
                      <body>
                        <h1>Мое предложение: {planet_name}!</h1>
                      <h2> Эта планета близка к Земле;</h2>
                        <div class="alert alert-success" role="alert">
                            <p>На ней много необходимых ресурсов;</p>
                        </div>
                        <div class="alert alert-secondary" role="alert">
                            <p>На ней есть вода и атмосфера;</p>
                        </div>
                        <div class="alert alert-warning" role="alert">
                            <p>На ней есть небольшое магнитное поле;</p>
                        </div>
                        <div class="alert alert-danger" role="alert">
                            <p>Наконец, она просто красива!</p>
                        </div>
                      </body>
                    </html>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
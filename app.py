from flask import Flask, render_template, request
from game_of_life import GameOfLife
from forms import WHform
from config import Config
app = Flask(__name__)
app.config.update(SECRET_KEY=Config.SECRET_KEY)

width = 15
height = 15
game = GameOfLife(height, width)

@app.route('/', methods=['get', 'post'])
def index():
    global width, height, game
    form = WHform()
    message = "Размер поля будет установлен по умолчанию (15 на 15)"
    if form.validate_on_submit():
        width = form.width.data
        height = form.height.data
        game = GameOfLife(height, width)
        message = f"Размер поля изменен на {width} на {height}"
        return render_template('index.html', form=form, message=message)
    game = GameOfLife(height, width)
    return render_template('index.html', form=form, message=message)

@app.route('/live/')
def live():
    if game.counter:
        game.form_new_generation()
    else:
        game.counter += 1
    cell_counter = sum(sum(i) for i in game.world)
    return render_template('live.html', game=game, counter=game.counter, cell_counter=cell_counter)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)


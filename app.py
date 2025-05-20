from flask import Flask, render_template
from habit_tracker import main_menu_actions

app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template('main_menu.html', actions=main_menu_actions)

@app.route('/new')
def new_habit():
    return render_template('new.html')

@app.route('/view_list')
def view_list():
    return render_template('view_list.html')

@app.route('/log')
def log_habit():
    return render_template('log.html')

@app.route('/delete')
def delete_habit():
    return render_template('delete.html')

@app.route('/stats')
def habit_stats():
    return render_template('stats.html')

if __name__ == "__main__":
    app.run()

from flask import Flask, render_template, request, redirect, url_for
import datetime

app = Flask(__name__)

habits = [
    {
        'habit_name': 'exercise',
        'frequency': 'daily',
        'is_done': False,
        'habit_streak': 0,
        'log_dates': [],
    }
]

@app.route('/')
def home_page():
    main_menu_actions = [
        {"label": "Add New Habit", "endpoint": "new_habit"},
        {"label": "Log a Habit", "endpoint": "log_habit"},
        {"label": "View Habit List", "endpoint": "view_list"},
        {"label": "Delete a Habit", "endpoint": "delete_habit"},
        {"label": "View Habit Stats", "endpoint": "habit_stats"},
        {"label": "Exit", "endpoint": "done"},
    ]
    return render_template('main_menu.html', actions=main_menu_actions)

@app.route('/new', methods=['GET', 'POST'])
def new_habit():
    if request.method == 'POST':
        habit_name = request.form.get("new_habit")
        frequency = request.form.get("frequency")

        new_habit = {
            "habit_name": habit_name,
            "frequency": frequency,
            "is_done": False,
            "habit_streak": 0,
            "log_dates": []
        }
        habits.append(new_habit)

        return redirect(url_for('view_list'))

    return render_template('new.html')

@app.route('/view_list')
def view_list():
    return render_template('view_list.html', habits=habits)

@app.route('/log', methods=['GET', 'POST'])
def log_habit():
    if request.method == 'POST':
        habit_index = int(request.form.get('habit_to_log'))
        habit_logged = habits[habit_index]
        date_logged = datetime.date.today()
        date_logged_str = date_logged.isoformat()
        if habit_logged['log_dates'] and habit_logged['log_dates'][-1] == date_logged_str:
            error_flag = "You already logged this today."

            return render_template('log.html', habits=habits, error_flag=error_flag)

        else:
            habit_index = int(request.form.get('habit_to_log'))
            habit_logged = habits[habit_index]
            date_logged = datetime.date.today()
            date_logged_str = date_logged.isoformat()
            habit_logged['is_done'] = True
            habit_logged['habit_streak'] += 1
            habit_logged['log_dates'].append(date_logged_str)

            return render_template('log.html', habits=habits, habit_logged=habit_logged, date_logged=date_logged_str)
    return render_template('log.html', habits=habits)

@app.route('/delete', methods=['GET', 'POST'])
def delete_habit():
    if request.method == 'POST':
        habit_index = int(request.form.get("habit_to_delete"))
        habits.pop(habit_index)

        return redirect(url_for('view_list'))

    return render_template('delete.html', habits=habits)

@app.route('/stats', methods=['GET', 'POST'])
def habit_stats():
    display_labels = {
        'habit_name': 'Habit Name',
        'frequency': 'Frequency',
        'is_done': 'Completed Today?',
        'habit_streak': 'Current Streak',
        'log_dates': 'Logged Dates'
    }

    if request.method == 'POST':
        habit_to_display_index = int(request.form.get("habit_to_display"))
        habit_to_display = habits[habit_to_display_index]

        return render_template('stats.html', habits=habits, habit_to_display=habit_to_display, labels=display_labels)

    return render_template('stats.html', habits=habits)

@app.route('/done')
def done():
    return render_template('done.html')

if __name__ == "__main__":
    app.run()

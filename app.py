from flask import Flask, render_template, request, redirect, url_for
from habit_tracker import view_list, new_habit, handle_new_habit_input, habits


app = Flask(__name__)

@app.route('/')
def home_page():
    main_menu_actions = [
        {"label": "Add New Habit", "endpoint": "new_habit"},
        {"label": "Log Habit", "endpoint": "log_habit"},
        {"label": "View Habits", "endpoint": "view_list"},
        {"label": "Delete Habit", "endpoint": "delete_habit"},
        {"label": "View Stats", "endpoint": "habit_stats"},
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

@app.route('/log')
def log_habit():
    return render_template('log.html')

@app.route('/delete', methods=['GET', 'POST'])
def delete_habit():
    if request.method == 'POST':
        habit_index = int(request.form.get("habit_to_delete"))
        habits.pop(habit_index)

        return redirect(url_for('view_list'))

    return render_template('delete.html', habits=habits)

@app.route('/stats', methods=['GET', 'POST'])
def habit_stats():
    if request.method == 'POST':
        habit_to_display_index = int(request.form.get("habit_to_display"))

        for habit in habits[habit_to_display_index]:
            habit_to_display = habit
        return render_template('stats.html', habits=habits, habit_to_display=habit_to_display)
# ** START HERE: keep working on the habit_stats button functionality
    return render_template('stats.html', habits=habits)




@app.route('/done')
def done():
    return render_template('done.html')

if __name__ == "__main__":
    app.run()

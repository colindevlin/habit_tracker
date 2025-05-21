from flask import Flask, render_template, request
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
        habit_name = request.form.get("new_habit")  # <-- This gets the user input
        frequency = request.form.get("frequency")   # <-- From dropdown or other input

        # Example: use this data to build a new habit dictionary
        new_habit = {
            "habit_name": habit_name,
            "frequency": frequency,
            "is_done": False,
            "habit_streak": 0,
            "log_dates": []
        }
        habits.append(new_habit)  # ← Assuming you're still using a global list

        return redirect(url_for('view_list'))  # Redirect after form submission

    return render_template('new.html')

@app.route('/view_list')
def view_list():
    return render_template('view_list.html', habits=habits)

@app.route('/log')
def log_habit():
    return render_template('log.html')

@app.route('/delete')
def delete_habit():
    return render_template('delete.html')

@app.route('/stats')
def habit_stats():
    return render_template('stats.html')

@app.route('/done')
def done():
    return render_template('done.html')

if __name__ == "__main__":
    app.run()

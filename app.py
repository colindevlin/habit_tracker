from flask import Flask, render_template, request, redirect, url_for, flash, get_flashed_messages
import datetime
from models import Habit, HabitLog, session

app = Flask(__name__)
app.secret_key = 'dev'

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

        new_habit = Habit(habit_name=habit_name, frequency=frequency, is_done=False, habit_streak=0)
        session.add(new_habit)
        session.commit()

        return redirect(url_for('view_list'))

    return render_template('new.html')

@app.route('/view_list')
def view_list():
    habit_list = session.query(Habit).all()
    return render_template('view_list.html', habit_list=habit_list)

@app.route('/log', methods=['GET', 'POST'])
def log_habit():
    if request.method == 'GET':
        all_habits = session.query(Habit).all()
        return render_template('log.html', habits=all_habits)

    elif request.method == 'POST':
        print(request.form)
        habit_id = int(request.form.get('habit_id_to_log'))
        habit_logged = session.get(Habit, habit_id)

        # check if logged today
        today = datetime.date.today().isoformat()
        existing_log = session.query(HabitLog).filter_by(habit_id=habit_logged.id, date_logged=today).first()
        if existing_log:
            error_flag = "You already logged this today."
            return render_template('log.html', habit=habit_logged, error_flag=error_flag)

        # no log today, update logs
        else:
            habit_id = int(request.form.get('habit_id_to_log'))
            habit_logged = session.get(Habit, habit_id)
            date_logged = datetime.date.today()
            date_logged_str = date_logged.isoformat()
            habit_logged.is_done = True
            habit_logged.habit_streak += 1
            formatted_date = datetime.datetime.strptime(date_logged_str, "%Y-%m-%d").strftime("%B %d, %Y")
            HabitLog(habit_id=habit_logged.id, date_logged=formatted_date)
            new_log = HabitLog(habit_id=habit_logged.id, date_logged=date_logged)
            session.add(new_log)
            session.commit()
            habit_logs = session.query(HabitLog).filter_by(habit_id=habit_logged.id).all()

            return render_template('log.html', habit_logged=habit_logged, date_logged=formatted_date, habit_logs=habit_logs)


@app.route('/delete', methods=['GET', 'POST'])
def delete_habit():
    if request.method == "GET":
        all_habits = session.query(Habit).all()
        return render_template('delete.html', all_habits=all_habits)

    elif request.method == 'POST':
        habit_id = int(request.form.get("habit_id_to_delete"))
        habit_to_delete = session.get(Habit, habit_id)

        if habit_to_delete:
            deleted_name = habit_to_delete.habit_name
            session.delete(habit_to_delete) # need to add functionality to delete HabitLog when Habit deleted
            session.commit()
            flash(f"You deleted '{deleted_name}'") # flash message not working, come back to this
            return redirect(url_for('view_list'))
        else:
            all_habits = session.query(Habit).all()
            error_msg = "Habit not found."
            return render_template('view_list.html', all_habits=all_habits, error=error_msg)
    else:
        return render_template('delete.html')

@app.route('/stats', methods=['GET', 'POST'])
def habit_stats():
    display_labels = {
        'habit_name': 'Habit Name',
        'frequency': 'Frequency',
        'is_done': 'Completed Today',
        'habit_streak': 'Current Streak',
        'log_dates': 'Logged Dates'
    }

    all_habits=session.query(Habit).all()

    if request.method == "GET":
        return render_template('stats.html', all_habits=all_habits)

    elif request.method == 'POST':
        habit_id = int(request.form.get("habit_id_to_display"))
        habit_to_display = session.get(Habit, habit_id)
        print(habit_to_display)
        return render_template('stats.html', habit_to_display=habit_to_display, labels=display_labels, all_habits=all_habits)

    return render_template('stats.html')

@app.route('/done')
def done():
    return render_template('done.html')

@app.template_filter('get_attr')
def get_attr(obj, attr_name):
    return getattr(obj, attr_name)

if __name__ == "__main__":
    app.run()

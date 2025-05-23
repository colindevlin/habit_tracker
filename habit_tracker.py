import sys
import json
import datetime


main_menu_actions =[
    "New habit",
    "View list",
    "Log habit",
    "Delete habit",
    "Habit stats",
    "Quit",
]

habits = [
    {
        'habit_name': 'exercise',
        'frequency': 'daily',
        'is_done': False,
        'habit_streak': 0,
        'log_dates': [],
    }
]

def view_list():
    while True:
        if not habits:
            print("No habits found.")
            break
        else:
            for habit in habits:
                print(f"-- {habit['habit_name'].title()}")
                print(f"\tFrequency: {habit['frequency'].title()}")
                if habit['is_done'] == False:
                    print(f"\tDone Today?: No")
                else: print("\tDone Today?: Yes")
                print(f"\tCurrent Streak: {habit['habit_streak']}")
                for date in habit['log_dates']:
                    print(f"\t{date}")
            print(f"1. Return to Main Menu")
            print(f"2. Quit")

            view_list_select = input(": ")
            if view_list_select == "1":
                break
            elif view_list_select == "2":
                sys.exit()
            else: print("!! Invalid, try again.")

def habit_stats(stats):
    print(f"-- {stats['habit_name'].title()}")
    print(f"\tFrequency: {stats['frequency']}")
    print(f"\tDone today?: {stats['is_done']}")
    print(f"\tCurrent Streak: {stats['habit_streak']}")
    for date in stats['log_dates']:
        print(f"\t{date}")

def handle_habit_stats_input():
    while True:
        if not habits:
            print("No habits found.")
            break
        else:
            for index, habit in enumerate(habits, start=1):
                print(f"{index}. {habit['habit_name'].title()}")
            print(f"{index + 1}: Return to Main Menu")
            print(f"{index + 2}: Quit")

            habit_stats_selection = input("What habit stats?: ")
            stats_selection = int(habit_stats_selection)
            if 1 <= stats_selection <= len(habits):
                stats = habits[stats_selection - 1]
            elif stats_selection == index + 1:
                break
            elif stats_selection == index + 2:
                sys.exit()
            else: print("!! Invalid, try again.")

            habit_stats(stats)

def new_habit(habit_name, frequency):
    habits.append({'habit_name': habit_name.title(),
                   'frequency': frequency,
                   'is_done': False,
                   'habit_streak': 0,
                   'log_dates': [],
                   }
                  )
    save_tasks_to_file()

def handle_new_habit_input():
    habit_name_input = input("Add a habit to track: ")
    while True:
        frequency_input = input("Daily or Weekly habit?: ").casefold()
        if frequency_input not in ["daily", "weekly"]:
            print("Invalid -- we only track daily or weekly habits.")
        else:
            new_habit(habit_name_input, frequency_input)
            break

def log_habit(habit, date):
    habit['is_done'] = True
    habit['habit_streak'] += 1
    habit['log_dates'].append(date)
    save_tasks_to_file()
    print(f"You marked {habit['habit_name'].title()} as done today.")
    print(f"Your {habit['habit_name'].title()} streak is {habit['habit_streak']}!")
    print("Date Log:")
    for date in habit['log_dates']:
        print(date)

def handle_log_habit_input():
    for index, habit in enumerate(habits, start=1):
        print(f"{index}. {habit['habit_name'].title()}")

    habit_to_log = input("Which habit do you want to log?: ")
    habit_selected = int(habit_to_log)
    if 1 <= habit_selected <= len(habits):
        habit = habits[habit_selected - 1]
        date_logged = datetime.date.today()
        date_logged_str = date_logged.isoformat()
        if habit['log_dates'] and habit['log_dates'][-1] == date_logged.isoformat():
            print("You already logged this today.")
            return
    else: print("!! Invalid, try again.")

    log_habit(habit, date_logged_str)

def delete_habit(habit_to_delete):
    habits.remove(habit_to_delete)
    print(f"{habit_to_delete['habit_name'].title()} deleted from your Habit List.")
    save_tasks_to_file()

def handle_delete_habit_input():
    while True:
        for index, habit in enumerate(habits, start=1):
            print(f"{index}. {habit['habit_name'].title()}")
        print(f"{index + 1}. Return to Main Menu")
        print(f"{index + 2}. Quit")

        habit_to_delete = input("Select a habit to remove: ")
        habit_selected = int(habit_to_delete)

        if 1 <= habit_selected <= len(habits):
            habit = habits[habit_selected - 1]
            delete_habit(habit)
            break
        else:
            print("!! Invalid selection, try again.")

functions_dict = {
    "New habit": handle_new_habit_input,
    "View list": view_list,
    "Log habit": handle_log_habit_input,
    "Delete habit": handle_delete_habit_input,
    "Habit stats": handle_habit_stats_input,
    "Quit": sys.exit
}

def save_tasks_to_file(filename="habits.json"):
    with open(filename, "w") as file:
        json.dump(habits, file, indent=4)

def load_tasks_from_file(filename="habits.json"):
    global habits
    with open(filename, "r") as file:
        habits = json.load(file)


def main_menu():
    while True:
        for index, action in enumerate(main_menu_actions, start=1):
            print(f"{index}. {action}") # Print main menu
        main_menu_input = input("Select an action: ")
        if main_menu_input.isdigit():
            main_menu_selection = int(main_menu_input)
            if 1 <= main_menu_selection <= len(main_menu_actions):
                action = main_menu_actions[main_menu_selection - 1]
                functions_dict[action]()
            else:
                print("!! Invalid, try again.")
        else: print("!! Invalid, try again.")

# <----- main loop ----->
if __name__ == "__main__":
    # load_tasks_from_file()
    main_menu()

# to do:

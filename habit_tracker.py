# Core Features for Minimum Viable Product
# User Input – Add and remove habits.
# Tracking – Log habit completions by date.
# Points System – Earn points for each logged habit.
# View Progress – Display current habits, total points, and recent activity.

import sys

main_menu_actions =[
    "New habit",
    "View list",
    "Log habit",
    "Habit stats",
    "Quit",
]

habits = [
    {
        'habit_name': 'exercise',
        'frequency': 'daily',
        'is_done': False,
        'habit_streak': 0,
    }
]

def view_list():
    while True:
        for habit in habits:
            print(f"-- {habit['habit_name'].title()}")
            print(f"\tFrequency: {habit['frequency']}")
            print(f"\tDone Today?: {habit['is_done']}")
            print(f"\tCurrent Streak: {habit['habit_streak']}")
        print(f"1. Return to Main Menu")
        print(f"2. Quit")

        view_list_select = input(": ")
        if view_list_select == "1":
            break
        elif view_list_select == "2":
            sys.exit()
        else: print("!! Invalid, try again.")

def habit_stats(stats):
    print(f"{stats['habit_name']}")
    print(f"{stats['frequency']}")
    print(f"{stats['is_done']}")
    print(f"{stats['habit_streak']}")

def handle_habit_stats_input():
    while True:
        for index, habit in enumerate(habits, start=1):
            print(f"{index}. {habit['habit_name']}")
            print(f"{index + 1}: Return to Main Menu")
            print(f"{index + 2}: Quit")

        habit_stats_selection = input("What habit?: ")
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
                   'habit_streak': 0})

def handle_new_habit_input():
    habit_name_input = input("Add a habit to track: ")
    while True:
        frequency_input = input("Daily or Weekly habit?: ")
        if frequency_input.casefold() not in ["daily", "weekly"]:
            print("Invalid -- we only track daily or weekly habits.")
        else:
            new_habit(habit_name_input, frequency_input)
            break

def log_habit(habit):
    habit['is_done'] = True
    habit['habit_streak'] += 1
    print(f"You marked {habit['habit_name'].title()} as done today.")
    print(f"Your {habit['habit_name'].title()} streak is {habit['habit_streak']}!")

def handle_log_habit_input():
    for index, habit in enumerate(habits, start=1):
        print(f"{index}. {habit['habit_name'].title()}")

        habit_to_log = input("Which habit do you want to log?: ")
        habit_selected = int(habit_to_log)
        if 1 <= habit_selected <= len(habits):
            habit = habits[habit_selected - 1]
        else: print("!! Invalid, try again.")

    log_habit(habit)

functions_dict = {
    "New habit": handle_new_habit_input,
    "View list": view_list,
    "Log habit": handle_log_habit_input,
    "Habit stats": handle_habit_stats_input,
    "Quit": sys.exit
}

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
while True:
    main_menu()

# to do:
#

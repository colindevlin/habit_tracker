# 🧩 Core Features for MVP (Minimum Viable Product)
# User Input – Add and remove habits.
# Tracking – Log habit completions by date.
# Points System – Earn points for each logged habit.
# View Progress – Display current habits, total points, and recent activity.
#
# 🔧 Suggested Tech Stack for MVP
# Language: Python
# Interface: Command-line (to start), with plans to expand to GUI or web.
# Data Storage: JSON or SQLite (start simple, upgrade later)

import sys
import datetime

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

def habit_stats():
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

        print(f"{habit['habit_name']}")
        print(f"{habit['frequency']}")
        print(f"{habit['is_done']}")
        print(f"{habit['habit_streak']}")


def new_habit():
    habit_input = input("Add a habit to track: ")
    frequency_input = input("How often will you do it?: ")
    habits.append({'habit_name': habit_input.title(),
                   'frequency': frequency_input,
                   'is_done': False,
                   'habit_streak': 0})
    return habits

def log_habit():
    for index, habit in enumerate(habits, start=1):
        print(f"{index}. {habit['habit_name'].title()}")
        habit_to_log = input("Which habit do you want to log?: ")

        habit_selected = int(habit_to_log)
        if 1 <= habit_selected <= len(habits):
            habit = habits[habit_selected - 1]

        habit['is_done'] = True
        habit['habit_streak'] += 1
    print(f"You marked {habit['habit_name'].title()} as done today.")
    print(f"Your {habit['habit_name'].title()} streak is {habit['habit_streak']}!")

functions_dict = {
    "New habit": new_habit,
    "View list": view_list,
    "Log habit": log_habit,
    "Habit stats": habit_stats,
    "Quit": sys.exit
}

def main_menu():
    for index, action in enumerate(main_menu_actions, start=1):
        print(f"{index}. {action}") # Print main menu
    main_menu_input = input("Select an action: ")

    main_menu_selection = int(main_menu_input)
    if 1 <= main_menu_selection <= len(main_menu_actions):
        action = main_menu_actions[main_menu_selection - 1]
        functions_dict[action]()
    else:
        print("Invalid, try again.")






# <----- main loop ----->
while True:
    main_menu()
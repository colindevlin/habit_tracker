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
    "Log habit",
    "Habit stats",
    "Quit",
]

habits = [
    {
        "habit_name": "exercise",
        "frequency": "daily",
    }
]


def new_habit():
    habit_input = input("Add a habit to track: ")
    frequency_input = input("How often will you do it?: ")
    habits.append({"habit_name": habit_input, "frequency": frequency_input})
    return habits

functions_dict = {
    "New habit": new_habit,
    # "Habit stats": habit_stats,
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
main_menu()
# Shift Scheduler

## Overview
The Shift Scheduler is a simple Python application built using the Tkinter library for creating graphical user interfaces (GUIs). It enables users to assign shifts to team members based on certain constraints.

## Features
- Displays a list of team members.
- Allows selection of team members to assign shifts.
- Generates a shift timetable for the selected team members.
- Considers constraints such as maximum number of shifts per day and days off.

## Requirements
- Python 3.x
- Tkinter library (usually included in Python installations)
- ttk module from Tkinter for enhanced widget styling

## How to Use
1. Run the program using Python.
2. Select team members from the list.
3. Click on the "Assign Shifts" button.
4. View the generated shift timetable for the selected team members.

## Program Structure
- `ShiftSchedulerApp` class: Main application class responsible for creating the GUI and managing user interactions.
- `create_widgets` method: Initializes GUI elements such as listboxes, labels, buttons, and treeviews.
- `assign_shifts` method: Assigns shifts to selected team members based on constraints.
- `generate_shifts` method: Generates shifts for each team member, considering constraints such as days off and maximum number of shifts per day.
- `if __name__ == "__main__":` block: Entry point of the program. Instantiates the main application class and starts the GUI event loop.

## Dependencies
The program requires the Tkinter library, which is usually included in standard Python installations. No additional dependencies are needed.

# About the Setup

## Overview
This setup script is used to create a standalone executable for the Shift Scheduler Application using cx_Freeze. The Shift Scheduler Application is a Python program that enables users to assign shifts to team members based on certain constraints.

## Setup Details
- **Name:** ShiftSchedulerApp
- **Version:** 1.0
- **Description:** Shift Scheduler Application

## How to Use
1. Ensure that you have Python installed on your system.
2. Install cx_Freeze using `pip install cx-Freeze`.
3. Save the provided setup script in the same directory as your Python script (`time_table_scheduler.py`).
4. Run the setup script using `python setup.py build`.
5. Once the build process is complete, you will find the standalone executable in the `build` directory.

## Executable Details
- **Name:** ShiftSchedulerApp.exe
- **Base:** Win32GUI (Windows GUI application without console window)

## Dependencies
- Python 3.x
- cx_Freeze





import tkinter as tk
from tkinter import ttk
import random

class ShiftSchedulerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Shift Scheduler")

        # Initialize variables
        self.team_members = ["Member1", "Member2", "Member3", "Member4", "Member5"]
        self.days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        self.shifts = ["Day", "Night"]

        # Create GUI elements
        self.create_widgets()

    def create_widgets(self):
        # Team Members Label
        tk.Label(self.root, text="Team Members:").grid(row=0, column=0, sticky="w", padx=10, pady=5)

        # Listbox to display team members
        self.team_listbox = tk.Listbox(self.root, selectmode=tk.MULTIPLE, height=len(self.team_members))
        for member in self.team_members:
            self.team_listbox.insert(tk.END, member)
        self.team_listbox.grid(row=1, column=0, padx=10, pady=5)

        # Shift Timetable Label
        tk.Label(self.root, text="Shift Timetable:").grid(row=0, column=1, sticky="w", padx=10, pady=5)

        # Treeview to display timetable
        self.timetable_treeview = ttk.Treeview(self.root, columns=["Members"] + self.days_of_week, show="headings")
        self.timetable_treeview.heading("Members", text="Members")
        for day in self.days_of_week:
            self.timetable_treeview.heading(day, text=day)
            self.timetable_treeview.column(day, width=80)  # Adjust column width
        self.timetable_treeview.grid(row=1, column=1, padx=10, pady=5)

        # Assign Shifts Button
        assign_button = tk.Button(self.root, text="Assign Shifts", command=self.assign_shifts)
        assign_button.grid(row=2, columnspan=2, pady=10)

    def assign_shifts(self):
        # Clear previous assignments
        for item in self.timetable_treeview.get_children():
            self.timetable_treeview.delete(item)

        # Get selected team members
        selected_members = [self.team_members[i] for i in self.team_listbox.curselection()]

        # Assign shifts while considering the constraints
        for member in selected_members:
            shifts = self.generate_shifts()
            self.timetable_treeview.insert("", "end", values=[member] + shifts)

    def generate_shifts(self):
        # Generate shifts for a member while considering constraints
        shifts = []
        days_off = random.sample(self.days_of_week, 2)

        for day in self.days_of_week:
            if day in days_off:
                shifts.append("Off")
            else:
                available_shifts = [shift for shift in self.shifts if shifts.count(shift) < 5]
                if not available_shifts:
                    shifts.append("Off")
                else:
                    selected_shift = random.choice(available_shifts)
                    shifts.append(selected_shift)

        return shifts

if __name__ == "__main__":
    root = tk.Tk()
    app = ShiftSchedulerApp(root)
    root.mainloop()

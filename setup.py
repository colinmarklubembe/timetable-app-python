from cx_Freeze import setup, Executable

setup(
    name="ShiftSchedulerApp",
    version="1.0",
    description="Shift Scheduler Application",
    executables=[Executable("time_table_scheduler.py", base="Win32GUI")],
)

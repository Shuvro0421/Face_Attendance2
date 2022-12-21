import cx_Freeze
import sys
import os 
base = None

if sys.platform == 'win32':
    base = "Win32GUI"

os.environ['TCL_LIBRARY'] = r"C:\Users\ASUS\.conda\envs\tensorflow-gpu\tcl\tcl8.6"
os.environ['TK_LIBRARY'] = r"C:\Users\ASUS\.conda\envs\tensorflow-gpu\tcl\tk8.6"

executables = [cx_Freeze.Executable("login.py", base=base, icon="face.ico")]


cx_Freeze.setup(
    name = "Face Attendance",
    options = {"build_exe": {"packages":["tkinter","os"], "include_files":["face.ico",'tcl86t.dll','tk86t.dll', 'images','data','database','attendance_report']}},
    version = "1.0",
    description = "Innovation",
    executables = executables
    )
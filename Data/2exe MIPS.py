import sys
from cx_Freeze import setup, Executable

import os

os.environ['TCL_LIBRARY'] = r"C:\Program Files\Anaconda3\tcl\tcl8.6"
os.environ['TK_LIBRARY'] = r"C:\Program Files\Anaconda3\tcl\tk8.6"

# Dependencies are automatically detected, but it might need fine tuning.
options = {
    'build_exe': {
        'include_files':[
            os.path.join('C:\\Program Files\\Anaconda3\\', 'DLLs', 'tk86t.dll'),
            os.path.join('C:\\Program Files\\Anaconda3\\', 'DLLs', 'tcl86t.dll'),
         ],"packages": ["tkinter", "_tkinter"]}}

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(  name = "mips",
        version = "0.1",
        description = "My GUI application!",
        options = options,
        executables = [Executable("mips.py", base=base)])


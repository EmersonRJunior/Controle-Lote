#python .\setup.py build

import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["os"], "includes": ["tkinter", 'pandas', 'tkcalendar']}

# GUI applications require a different base on Windows (the default is for
# a console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="Controle Romaneios",
    version="0.1",
    description="Um projeto pra controle de serviço",
    options={"build_exe": build_exe_options},
    executables=[Executable("Main.py", base=base)]
)
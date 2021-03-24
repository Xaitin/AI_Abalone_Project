import cx_Freeze

executables = [cx_Freeze.Executable("main.py")]

cx_Freeze.setup(
    name="Abalone",
    options={"build_exe": {"packages":["pygame"],
                           "include_files":["abalone.png"]}},
    executables = executables
    )
from cx_Freeze import setup, Executable

build_exe_options = {
    "packages": ["pygame"],
    "include_files": [
        "assets",
        "code"
    ]
}
setup(
    name="CosmicWar",
    version="1.0",
    description="jogo simples",
    options={"build_exe": build_exe_options},
    executables=[Executable("main.py", base=None)]
)
# Python_Game
A totally sweet game made in python

The goal of this game is to run down the field as the running back, while avoiding the defenders.
You will have 4 downs, to get as far as possible. The downs reset every touchdown.
Control the running back using the WASD keys.
In addition, you can control Pistol Pete at the bottom of the screen using your mouse.
Pistol Pete can shoot at the defenders to clear a path for the running back.


To run the game from the source code:
    -clone the repo into a directory on your computer
    -open a terminal in the cloned directory
    -type "cd ./Source_Code"
    -type "python ./main.py"

To package the game into an excecutable from source code,
    -clone the repo into a directory on your computer
    -open a terminal in the cloned directory
    -type "pyinstaller .\Source_Code\main.py --onefile --noconsole --name RunAndGun
    -the excecutable will be in .\dist directory
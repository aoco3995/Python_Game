# Python_Game
A totally sweet game made in python

The goal of this game is to run down the field as the running back, while avoiding the defenders.
You will have 4 downs, to get as far as possible. The downs reset every touchdown.
Control the running back using the WASD keys.
In addition, you can control Pistol Pete at the bottom of the screen using your mouse.
Pistol Pete can shoot at the defenders to clear a path for the running back. Pistol Pete obtains a temporary power up whenenver he shoots four defenders. To activate the power up, hold down the right mouse button first and then click and hold the left mouse button as well. This will activate a temporary machine gun mode.


To run the game from the source code:  
&emsp;-clone the repo into a directory on your computer  
&emsp;-open a terminal in the cloned directory  
&emsp;-type "cd ./Source_Code"  
&emsp;-type "python ./main.py"  
    
To package the game into an excecutable from source code:  
&emsp;-clone the repo into a directory on your computer  
&emsp;-open a terminal in the cloned directory  
&emsp;-type "pyinstaller .\Source_Code\main.py --onefile --noconsole --name RunAndGun"  
&emsp;-the excecutable will be in .\dist directory  

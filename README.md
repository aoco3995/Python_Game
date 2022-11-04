# Github Link
https://github.com/aoco3995/Python_Game/settings

# Introduction
Run and Gun

A totally sweet game made in python.

This game was devoloped using the pygame libary in python. The purpose of this game project is to satisfy a course team project for Oklahoma State Universtiy course ECEN 4273 (Software Engineering)

## Developers
Dylan Cook, Joey Stolfa, Adam O'Connor

# Requirements

Video game shall have a graphical element.

Video game shall be controllable from a standard keyboard and/or mouse

Video game shall have a start screen with start and quit commands/buttons.

Video game shall have an end condition.

# Installation

### Run from compiled executable:
&emsp;-Download the RunandGun_Demo2_Release.zip folder.  
&emsp;-Right click and select extract.  
&emsp;-Navigate to the exctracted directory.  
&emsp;-Under the "dist" directory, double click "RunAndGun.exe"  


### To run the game from the source code:  
&emsp;-clone the repo into a directory on your computer  
&emsp;-open a terminal in the cloned directory  
&emsp;-type "cd ./Source_Code"  
&emsp;-type "python ./main.py"  
    
# Configuration

### To package the game into an excecutable from source code:  
&emsp;-clone the repo into a directory on your computer  
&emsp;-open a terminal in the cloned directory  
&emsp;-type "pyinstaller .\Source_Code\main.py --onefile --noconsole --name RunAndGun"  
&emsp;-the excecutable will be in .\dist directory  


# Troubleshooting 

### Game scores not saving
The highscrores.txt database file must retain it's relative location to the main executable file. If the file get's deleted or moved on disk, it must be restored to it's original location for proper operation.

# Game Play Instructions

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
    

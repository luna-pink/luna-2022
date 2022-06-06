@echo off
cls
pyarmor pack --clean -e "--onefile  --icon C:/Users/%USERNAME%/Documents/GitHub/Luna-SelfBot/Images/Luna_Logo.ico --noconsole --noconfirm --hidden-import clint.textui --hidden-import discum --key=5QXapyTDbrRwW4ZBnUgPGAs9CeVSdiLk --add-data C:/Users/%USERNAME%/Documents/GitHub/Luna-SelfBot/Luna/cogs;cogs/" -x " --advanced 2" --output "C:/Users/%USERNAME%/Documents/GitHub/Luna-SelfBot/Scripts" --name "Luna.exe" C:/Users/%USERNAME%/Documents/GitHub/Luna-SelfBot/Luna/gui.py
pause
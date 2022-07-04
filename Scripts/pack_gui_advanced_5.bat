@echo off
cls
pyarmor pack --clean -e "--onefile  --icon C:/Users/%USERNAME%/Documents/GitHub/Luna-SelfBot/Images/Luna_Logo.ico --console --noconfirm --hidden-import clint.textui --hidden-import discum --key=5QXapyTDbrRwW4ZBnUgPGAs9CeVSdiLk --add-data C:/Users/%USERNAME%/Documents/GitHub/Luna-SelfBot/Luna/cogs;cogs/" -x "--advanced 5 --restrict=1 --enable-suffix --wrap-mode=1 --obf-code=2 --obf-mod=2 --recursive" --output "C:/Users/%USERNAME%/Documents/GitHub/Luna-SelfBot/Scripts" --name "Luna.exe" C:/Users/%USERNAME%/Documents/GitHub/Luna-SelfBot/Luna/luna_platinum.py
pause
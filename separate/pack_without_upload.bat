@echo off
cls
pyarmor pack --clean -e "--onefile  --icon C:/Users/%USERNAME%/Documents/GitHub/Luna-SelfBot/Images/Luna_Logo.ico --console --noconfirm --hidden-import clint.textui --hidden-import discum --key=5QXapyTDbrRwW4ZBnUgPGAs9CeVSdiLk --add-data C:/Users/%USERNAME%/Documents/GitHub/Luna-SelfBot/separate/cogs;cogs/" -x "--advanced 5 --recursive --enable-suffix --restrict=5 --obf-code=2 --obf-mod=2 --plugin=cogs/help.py" --output "C:/Users/%USERNAME%/Documents/GitHub/Luna-SelfBot/separate" --name "Luna.exe" C:/Users/%USERNAME%/Documents/GitHub/Luna-SelfBot/separate/main.py
pause
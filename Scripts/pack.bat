@echo off
cls
pyarmor pack --clean -e "--onefile  --icon C:/Users/%USERNAME%/Documents/GitHub/Luna-SelfBot/Images/Luna_Logo.ico --console --noconfirm --hidden-import clint.textui --add-data C:/Users/%USERNAME%/Documents/GitHub/Luna-SelfBot/Src/cogs;cogs/" --output "C:/Users/%USERNAME%/Documents/GitHub/Luna-SelfBot/Scripts" --name "Luna.exe" C:/Users/%USERNAME%/Documents/GitHub/Luna-SelfBot/Src/main.py
py upload.py
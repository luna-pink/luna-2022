from ctypes import windll
from sys import executable, argv, exit
windll.shell32.ShellExecuteW(None, "runas", executable, " ".join(argv), None, 1)
exit()
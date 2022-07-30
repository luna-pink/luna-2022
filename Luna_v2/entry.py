import ctypes
import sys

import main


if __name__ == '__main__':
    if main.check_if_debug() is None and not main.check_if_admin():
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
        sys.exit()
    main.initialize_luna()

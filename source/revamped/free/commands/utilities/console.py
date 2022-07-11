from .dependencies.variables import *
from .prints import *


class luna:
    def console(self, clear=False):
        """
        It prints the logo

        :param clear: If True, clears the console before printing the logo, defaults to False (optional)
        """
        if clear:
            os.system("cls")
        try:
            logo_variable = files.json(
                "data/console/console.json", "logo", documents=False
            )
            if logo_variable in ["luna", "luna.txt"]:
                logo_variable = logo
            else:
                ending = "" if ".txt" in logo_variable else ".txt"
                if not files.file_exist(
                        f"data/console/{logo_variable}{ending}",
                        documents=False
                ):
                    logo_variable = logo
                if files.json(
                        "data/console/console.json",
                        "center",
                        documents=False
                ):
                    logo_text = ""
                    for line in files.read_file(
                            f"data/console/{logo_variable}{ending}",
                            documents=False
                    ).splitlines():
                        logo_text += line.center(
                            os.get_terminal_size().columns
                        ) + "\n"
                        logo_variable = logo_text
                else:
                    logo_variable = files.read_file(
                        f"data/console/{logo_variable}{ending}", documents=False
                    )
        except Exception as e:
            prints.error(e)
            prints.message("Running a file check in 5 seconds")
            time.sleep(5)
            file_check()
        print(color.logo_gradient(f"""{logo_variable}"""))

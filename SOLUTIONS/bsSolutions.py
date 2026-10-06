# _____________________________________ bsSolutions _____________________________________
# _____________________________________ Professional Terminal-Based Technical Solutions Tool _____________________________________

# _____________________________________ Standard Library Imports _____________________________________
import os
import sys
import time

# _____________________________________ Third-Party Library Imports _____________________________________
from pyfiglet import Figlet
from rich.align import Align
from rich.console import Console
from rich.panel import Panel
from rich.text import Text

# _____________________________________ Console Configuration _____________________________________

# _____________________________________ Rich console is used for professional terminal output _____________________________________
console = Console()

# _____________________________________ Lambda Functions _____________________________________

# _____________________________________ Clears the terminal screen _____________________________________

# _____________________________________
# Windows:
#     cls

# Linux / macOS:
#     clear
# _____________________________________
__clear_screen__ = lambda: os.system("cls" if os.name == "nt" else "clear")


# _____________________________________ Pauses the program for 3 seconds _____________________________________
SL = lambda: time.sleep(3)


# _____________________________________ Application Banner _____________________________________
def __banner__():
    """
    Displays the professional bsSolutions banner.
    """

    # _____________________________________ Create the ASCII logo using PyFiglet _____________________________________
    fig = Figlet(font="slant")

    logo = fig.renderText("bsSolutions")

    # _____________________________________ Create the banner text _____________________________________
    banner_text = Text()

    banner_text.append(logo, style="bold green")

    banner_text.append("\n")

    banner_text.append("─" * 72, style="bright_black")

    banner_text.append("\n")

    banner_text.append("⚡ ", style="bold yellow")

    banner_text.append(
        "TECHNICAL SOLUTIONS • SOFTWARE • TOOLS • AUTOMATION", style="bold white"
    )

    banner_text.append(" ⚡", style="bold yellow")

    # _____________________________________ Put the banner inside a Rich panel _____________________________________
    banner_panel = Panel(
        Align.center(banner_text),
        title="[bold yellow]⚡ bsSolutions ⚡[/bold yellow]",
        subtitle="[dim]Professional Technical Solutions[/dim]",
        border_style="green",
        padding=(1, 2),
    )

    # _____________________________________ Display the final banner _____________________________________
    console.print(banner_panel)


# _____________________________________ Main bsSolutions Function _____________________________________
def __bsSolutions__():
    """
    Starts the main bsSolutions application.

    This function is currently the starting point for
    the actual solution/tool modules that will be added
    to the application later.
    """

    console.print(
        "\n[bold green][+][/bold green] "
        "[bold white]bsSolutions is running...[/bold white]"
    )

    console.print(
        "[dim]This tool is made for technical solutions "
        "and utility purposes.[/dim]\n"
    )


# _____________________________________ Main Menu Options _____________________________________
def __options__():
    """
    Returns the available commands for the application.
    """

    return """
[bold cyan]OPTIONS[/bold cyan]

[green][+][/green] PRESS [bold]ENTER[/bold] / [bold]1[/bold]  → Start
[green][+][/green] [bold]RMTMP[/bold]              → Open User TEMP
[green][+][/green] [bold]SRMTP[/bold]              → Open System TEMP
[green][+][/green] [bold]EXIT[/bold] / [bold]QUIT[/bold] / [bold]0[/bold] → Exit
"""


# _____________________________________ Main Menu _____________________________________
def __main_menu__():
    """
    Displays the application menu.
    """

    # _____________________________________ Rich markup is used here, so print through Rich Console _____________________________________
    console.print(
        Panel(
            __options__(),
            title="[bold cyan]Main Menu[/bold cyan]",
            border_style="cyan",
            padding=(1, 2),
        )
    )


# _____________________________________ User TEMP Folder _____________________________________
def __temp_remover__():
    """
    Opens the current user's TEMP directory.

    Command:
        RMTMP

    Note:
        This function only opens the TEMP directory.
        It does not delete temporary files.
    """

    console.print(
        "\n[cyan][~][/cyan] " "[bold]RMTMP[/bold] → Opening user TEMP folder..."
    )

    # _____________________________________ TEMP contains the current user's temporary directory _____________________________________
    temp_path = os.environ.get("TEMP")

    # _____________________________________ Make sure the TEMP variable exists _____________________________________
    if not temp_path:

        console.print("[bold red][!][/bold red] " "TEMP directory could not be found.")

        return

    # _____________________________________ Windows uses os.startfile() to open folders _____________________________________
    if os.name == "nt":

        try:
            os.startfile(temp_path)

            console.print("[bold green][+][/bold green] " f"Opened: {temp_path}")

        except OSError as error:

            console.print(
                "[bold red][!][/bold red] " f"Unable to open TEMP folder: {error}"
            )

        return

    # _____________________________________ Linux/macOS support _____________________________________
    if sys.platform == "darwin":

        os.system(f'open "{temp_path}"')

    else:

        os.system(f'xdg-open "{temp_path}"')


# _____________________________________ System TEMP Folder _____________________________________
def __system_temp_remover__():
    """
    Opens the Windows system TEMP directory.

    Command:
        SRMTP

    Note:
        This function opens the directory only.
        It does not remove files.
    """

    console.print(
        "\n[cyan][~][/cyan] " "[bold]SRMTP[/bold] → Opening system TEMP folder..."
    )

    # _____________________________________ The Windows system directory normally contains a Temp folder _____________________________________
    system_root = os.environ.get("SystemRoot", r"C:\Windows")

    system_temp_path = os.path.join(system_root, "Temp")

    # _____________________________________ Only Windows has this specific system TEMP location _____________________________________
    if os.name != "nt":

        console.print(
            "[bold yellow][!][/bold yellow] " "SRMTP is currently designed for Windows."
        )

        return

    try:

        os.startfile(system_temp_path)

        console.print("[bold green][+][/bold green] " f"Opened: {system_temp_path}")

    except OSError as error:

        console.print(
            "[bold red][!][/bold red] " f"Unable to open system TEMP folder: {error}"
        )


# _____________________________________ Program Terminator _____________________________________
def __program_terminator__():
    """
    Safely terminates the application.
    """

    console.print("\n[bold yellow][+][/bold yellow] " "bsSolutions Program Teminated Successfully...")

    SL()

    # _____________________________________ Exit status 0 means the application ended normally _____________________________________
    sys.exit(0)

# _____________________________________ Future Solution Fetching Function _____________________________________
# def get_bs_solution(problem_id):
#     """
#     Fetches a solution using a problem ID.

#     Args:
#         problem_id (str):
#             Unique ID of the requested problem.

#     Returns:
#         str:
#             The requested solution.
#     """

#     # Future implementation will be added here.
#     pass


# _____________________________________ Main Application Loop _____________________________________
def __main__():
    """
    Main entry point of bsSolutions.

    The application continues running until the user
    selects EXIT, QUIT, or 0.
    """

    while True:

        # _____________________________________ Clear the previous screen _____________________________________
        __clear_screen__()

        # _____________________________________ Display the application banner _____________________________________
        __banner__()

        # _____________________________________ Display the main menu _____________________________________
        __main_menu__()

        # _____________________________________ Read and normalize user input _____________________________________
        user_input = input("\nCHOOSE: ").strip().lower()

        # _____________________________________ START _____________________________________

        # _____________________________________ Empty input means ENTER _____________________________________

        # _____________________________________
        # Therefore:
        # ENTER or 1 → Start the application.
        # _____________________________________
        if user_input in ("", "1"):

            __bsSolutions__()

            # _____________________________________ Give the user time to read the output _____________________________________
            SL()

            continue

        # _____________________________________ USER TEMP _____________________________________
        elif user_input == "rmtmp":

            __temp_remover__()

            SL()

            continue

        # _____________________________________ SYSTEM TEMP _____________________________________
        elif user_input == "srmtp":

            __system_temp_remover__()

            SL()

            continue

        # _____________________________________ EXIT _____________________________________
        elif user_input in (
            "exit",
            "quit",
            "0",
        ):

            __program_terminator__()

        # _____________________________________ INVALID INPUT _____________________________________
        else:

            console.print(
                "\n"
                "[bold red][!][/bold red] "
                "\n"
                "[bold red][!][/bold red] "
                "[bold]Invalid option.[/bold]\n"
                "\n"
                "[+] ENTER / 1          → Start"
                "\n"
                "[+] RMTMP              → Open User TEMP"
                "\n"
                "[+] SRMTP              → Open System TEMP"
                "\n"
                "[+] EXIT / QUIT / 0    → Exit"
            )

            SL()


if __name__ == "__main__":
    __main__()

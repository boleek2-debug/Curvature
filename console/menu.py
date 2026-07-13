from core.diagnostics import workshop_status
from core.workflow import WorkflowManager

from .diagnostics import run_diagnostics
from .runtime import show_ai_runtime
from .status import show_status
from .ui import (
    clear_screen,
    draw_error,
    draw_header,
    draw_menu,
    draw_message,
)


MENU_OPTIONS = [
    ("1", "System Status"),
    ("2", "Diagnostics"),
    ("3", "Workshop Status"),
    ("4", "Workflow Engine"),
    ("5", "AI Runtime"),
    ("0", "Exit Console"),
]


def show_workshop_status() -> None:
    clear_screen()
    draw_header("WORKSHOP STATUS")

    for indicator in workshop_status():
        print(f"{indicator.name:<22} [{indicator.state}]")

    print()
    input("Press ENTER to continue...")


def show_workflows() -> None:
    clear_screen()
    draw_header("WORKFLOW ENGINE")

    manager = WorkflowManager()

    for workflow in manager.all():
        print(f"{workflow.name:<25} [{workflow.state}]")

    print()
    input("Press ENTER to continue...")


def main_menu() -> None:
    while True:
        clear_screen()
        draw_header()
        draw_menu(MENU_OPTIONS)

        choice = input("Select operation: ").strip()

        if choice == "1":
            show_status()
        elif choice == "2":
            run_diagnostics()
        elif choice == "3":
            show_workshop_status()
        elif choice == "4":
            show_workflows()
        elif choice == "5":
            show_ai_runtime()
        elif choice == "0":
            clear_screen()
            draw_header("CONSOLE SHUTDOWN")
            draw_message("Console session terminated.")
            break
        else:
            draw_error("Unknown operation.")
            input("Press ENTER to continue...")

from core.indicators import telemetry_indicator

from .menu import main_menu
from .ui import clear_screen, draw_header, draw_indicator


def main() -> None:
    clear_screen()
    draw_header("INITIALIZING CONSOLE")
    draw_indicator(telemetry_indicator())

    main_menu()


if __name__ == "__main__":
    main()

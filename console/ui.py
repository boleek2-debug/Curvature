import os

from core.indicators.indicator import Indicator


CONSOLE_WIDTH = 48


def clear_screen() -> None:
    os.system("clear")


def draw_header(title: str = "OPERATIONS CONSOLE") -> None:
    print()
    print("═" * CONSOLE_WIDTH)
    print(" CURVATURE")
    print(f" {title}")
    print("═" * CONSOLE_WIDTH)
    print()


def draw_indicator(indicator: Indicator) -> None:
    print(f"{indicator.name:<20} [{indicator.state}]")

    if indicator.details:
        print(f"  {indicator.details}")

    print()


def draw_menu(options: list[tuple[str, str]]) -> None:
    for key, label in options:
        print(f"[{key}] {label}")

    print()


def draw_message(message: str) -> None:
    print(message)
    print()


def draw_error(message: str) -> None:
    print(f"ATTENTION: {message}")
    print()


def pause() -> None:
    input("Press ENTER to continue...")

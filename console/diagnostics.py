import subprocess

from .ui import clear_screen, draw_header, draw_message, pause


def run_diagnostics() -> None:
    clear_screen()
    draw_header("SYSTEM DIAGNOSTICS")
    draw_message("Running Core diagnostic checks...")

    result = subprocess.run(
        ["python", "-m", "pytest", "-v"],
        check=False,
    )

    print()

    if result.returncode == 0:
        draw_message("Diagnostic state: READY")
    else:
        draw_message("Diagnostic state: ATTENTION")

    pause()

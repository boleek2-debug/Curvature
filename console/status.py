from core.telemetry import Telemetry

from .ui import clear_screen, draw_header, pause


def show_status() -> None:
    telemetry = Telemetry()

    cpu = telemetry.cpu()
    memory = telemetry.memory()
    gpu = telemetry.gpu()
    disk = telemetry.disk()

    clear_screen()
    draw_header("SYSTEM STATUS")

    print(f"CPU usage           {cpu:>8.1f} %")
    print(
        f"Memory              "
        f"{memory['used_gb']:>6.2f} / "
        f"{memory['total_gb']:.2f} GB"
    )
    print(f"Memory load         {memory['percent']:>8.1f} %")
    print()
    print(f"GPU                 {gpu['name']}")
    print(f"GPU usage           {gpu['usage_percent']:>8} %")
    print(f"GPU temperature     {gpu['temperature_c']:>8} °C")
    print(
        f"GPU memory          "
        f"{gpu['memory_used_mb']:>4} / "
        f"{gpu['memory_total_mb']} MB"
    )
    print()
    print(
        f"Disk usage          "
        f"{disk['used_gb']:>6.2f} / "
        f"{disk['total_gb']:.2f} GB"
    )
    print(f"Disk free           {disk['free_gb']:>8.2f} GB")
    print()

    pause()

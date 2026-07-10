from .telemetry import Telemetry


def main():
    telemetry = Telemetry()

    print("Curvature Core starting...\n")

    print(f"CPU Usage: {telemetry.cpu()}%")

    ram = telemetry.memory()
    print(
        f"RAM: {ram['used_gb']} GB / "
        f"{ram['total_gb']} GB "
        f"({ram['percent']}%)"
    )

    gpu = telemetry.gpu()
    print(
        f"GPU: {gpu['name']} | "
        f"{gpu['usage_percent']}% | "
        f"{gpu['temperature_c']}°C | "
        f"{gpu['memory_used_mb']} / "
        f"{gpu['memory_total_mb']} MB"
    )

    disk = telemetry.disk()
    print(
        f"Disk: {disk['used_gb']} / "
        f"{disk['total_gb']} GB "
        f"({disk['percent']}%) | "
        f"Free: {disk['free_gb']} GB"
    )


if __name__ == "__main__":
    main()
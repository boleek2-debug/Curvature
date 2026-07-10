import subprocess


def info() -> dict:
    result = subprocess.run(
        [
            "nvidia-smi",
            "--query-gpu=name,temperature.gpu,utilization.gpu,memory.used,memory.total",
            "--format=csv,noheader,nounits",
        ],
        capture_output=True,
        text=True,
        check=True,
    )

    name, temp, usage, memory_used, memory_total = [
        value.strip() for value in result.stdout.strip().split(",")
    ]

    return {
        "name": name,
        "temperature_c": int(temp),
        "usage_percent": int(usage),
        "memory_used_mb": int(memory_used),
        "memory_total_mb": int(memory_total),
    }
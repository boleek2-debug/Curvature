import psutil


def info() -> dict:
    memory = psutil.virtual_memory()

    return {
        "used_gb": round(memory.used / (1024 ** 3), 2),
        "total_gb": round(memory.total / (1024 ** 3), 2),
        "percent": memory.percent,
    }
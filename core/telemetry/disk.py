import psutil


def info(path: str = "/") -> dict:
    disk = psutil.disk_usage(path)

    return {
        "path": path,
        "used_gb": round(disk.used / (1024 ** 3), 2),
        "total_gb": round(disk.total / (1024 ** 3), 2),
        "free_gb": round(disk.free / (1024 ** 3), 2),
        "percent": disk.percent,
    }
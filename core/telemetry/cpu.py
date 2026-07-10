import psutil


def usage() -> float:
    return psutil.cpu_percent(interval=0.5)

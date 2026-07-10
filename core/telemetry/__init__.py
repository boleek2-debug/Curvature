from .cpu import usage as cpu_usage
from .memory import info as memory_info
from .gpu import info as gpu_info
from .disk import info as disk_info


class Telemetry:
    def cpu(self):
        return cpu_usage()

    def memory(self):
        return memory_info()

    def gpu(self):
        return gpu_info()

    def disk(self):
        return disk_info()
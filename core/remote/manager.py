from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any

from .workstation import Workstation


@dataclass(frozen=True)
class RemoteHeartbeatInfo:
    endpoint_resolvable: bool
    service_available: bool
    api_available: bool
    checked_at: datetime
    last_successful_at: datetime | None

    @property
    def state(self) -> str:
        if self.api_available:
            return "READY"

        if self.service_available:
            return "ATTENTION"

        return "OFFLINE"


@dataclass(frozen=True)
class RemoteGpuInfo:
    name: str
    vram_total_bytes: int
    vram_free_bytes: int

    @property
    def vram_used_bytes(self) -> int:
        return max(0, self.vram_total_bytes - self.vram_free_bytes)

    @property
    def vram_usage_percent(self) -> float:
        if self.vram_total_bytes <= 0:
            return 0.0

        return self.vram_used_bytes / self.vram_total_bytes * 100.0


@dataclass(frozen=True)
class RemoteQueueInfo:
    running: int
    pending: int

    @property
    def total(self) -> int:
        return self.running + self.pending


@dataclass(frozen=True)
class RemoteRuntimeInfo:
    operating_system: str
    ram_total_bytes: int
    ram_free_bytes: int
    comfyui_version: str
    python_version: str
    pytorch_version: str

    @property
    def ram_used_bytes(self) -> int:
        return max(0, self.ram_total_bytes - self.ram_free_bytes)

    @property
    def ram_usage_percent(self) -> float:
        if self.ram_total_bytes <= 0:
            return 0.0

        return self.ram_used_bytes / self.ram_total_bytes * 100.0


class RemoteManager:
    _last_successful_verification: datetime | None = None
    COMFYUI_PORT = 8188
    COMFYUI_SYSTEM_STATS_PATH = "/system_stats"
    COMFYUI_QUEUE_PATH = "/queue"

    def __init__(self):
        self.workstation = Workstation(
            name="Main Workstation",
            role="AI Runtime",
            endpoint="thing",
        )

    def heartbeat(self) -> RemoteHeartbeatInfo:
        checked_at = datetime.now(timezone.utc)
        endpoint_resolvable = self.workstation.endpoint_resolvable()
        service_available = self.comfyui_available()
        api_available = self.comfyui_system_stats() is not None

        if api_available:
            RemoteManager._last_successful_verification = checked_at

        return RemoteHeartbeatInfo(
            endpoint_resolvable=endpoint_resolvable,
            service_available=service_available,
            api_available=api_available,
            checked_at=checked_at,
            last_successful_at=RemoteManager._last_successful_verification,
        )

    def comfyui_available(self) -> bool:
        return self.workstation.service_available(
            port=self.COMFYUI_PORT,
        )

    def comfyui_system_stats(self) -> dict[str, Any] | None:
        return self.workstation.get_json(
            port=self.COMFYUI_PORT,
            path=self.COMFYUI_SYSTEM_STATS_PATH,
        )

    def comfyui_queue(self) -> dict[str, Any] | None:
        return self.workstation.get_json(
            port=self.COMFYUI_PORT,
            path=self.COMFYUI_QUEUE_PATH,
        )

    def primary_gpu_info(
        self,
        system_stats: dict[str, Any],
    ) -> RemoteGpuInfo | None:
        devices = system_stats.get("devices")

        if not isinstance(devices, list) or not devices:
            return None

        primary_device = devices[0]

        if not isinstance(primary_device, dict):
            return None

        name = primary_device.get("name")
        vram_total = primary_device.get("vram_total")
        vram_free = primary_device.get("vram_free")

        if not isinstance(name, str) or not name.strip():
            return None

        if not isinstance(vram_total, int) or isinstance(vram_total, bool):
            return None

        if not isinstance(vram_free, int) or isinstance(vram_free, bool):
            return None

        if vram_total < 0 or vram_free < 0:
            return None

        return RemoteGpuInfo(
            name=name,
            vram_total_bytes=vram_total,
            vram_free_bytes=vram_free,
        )

    def queue_info(
        self,
        queue_data: dict[str, Any],
    ) -> RemoteQueueInfo | None:
        running = queue_data.get("queue_running")
        pending = queue_data.get("queue_pending")

        if not isinstance(running, list):
            return None

        if not isinstance(pending, list):
            return None

        return RemoteQueueInfo(
            running=len(running),
            pending=len(pending),
        )

    def runtime_info(
        self,
        system_stats: dict[str, Any],
    ) -> RemoteRuntimeInfo | None:
        system = system_stats.get("system")

        if not isinstance(system, dict):
            return None

        operating_system = system.get("os")
        ram_total = system.get("ram_total")
        ram_free = system.get("ram_free")
        comfyui_version = system.get("comfyui_version")
        python_version = system.get("python_version")
        pytorch_version = system.get("pytorch_version")

        if not isinstance(operating_system, str) or not operating_system:
            return None

        if not isinstance(ram_total, int) or isinstance(ram_total, bool):
            return None

        if not isinstance(ram_free, int) or isinstance(ram_free, bool):
            return None

        if ram_total < 0 or ram_free < 0:
            return None

        if not isinstance(comfyui_version, str):
            return None

        if not isinstance(python_version, str):
            return None

        if not isinstance(pytorch_version, str):
            return None

        return RemoteRuntimeInfo(
            operating_system=operating_system,
            ram_total_bytes=ram_total,
            ram_free_bytes=ram_free,
            comfyui_version=comfyui_version,
            python_version=python_version,
            pytorch_version=pytorch_version,
        )

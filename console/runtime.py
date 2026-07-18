from datetime import datetime

from core.remote import (
    RemoteGpuInfo,
    RemoteHeartbeatInfo,
    RemoteManager,
    RemoteQueueInfo,
    RemoteRuntimeInfo,
)

from .ui import clear_screen, draw_header, pause


GIBIBYTE = 1024**3


def format_gibibytes(value_bytes: int) -> str:
    return f"{value_bytes / GIBIBYTE:.2f} GB"


def format_timestamp(value: datetime | None) -> str:
    if value is None:
        return "Never"

    return value.astimezone().strftime("%Y-%m-%d %H:%M:%S %Z")


def draw_heartbeat(heartbeat: RemoteHeartbeatInfo) -> None:
    endpoint_state = "RESOLVED" if heartbeat.endpoint_resolvable else "UNRESOLVED"
    service_state = "ONLINE" if heartbeat.service_available else "OFFLINE"
    api_state = "READY" if heartbeat.api_available else "UNAVAILABLE"

    print(f"Heartbeat  [{heartbeat.state}]")
    print(f"Endpoint   [{endpoint_state}]")
    print(f"Port 8188  [{service_state}]")
    print(f"API        [{api_state}]")
    print(f"Checked    {format_timestamp(heartbeat.checked_at)}")
    print(f"Last good  {format_timestamp(heartbeat.last_successful_at)}")


def draw_gpu_info(gpu: RemoteGpuInfo) -> None:
    print(f"GPU        {gpu.name}")
    print(
        "VRAM       "
        f"{format_gibibytes(gpu.vram_used_bytes)} / "
        f"{format_gibibytes(gpu.vram_total_bytes)}"
    )
    print(f"VRAM load  {gpu.vram_usage_percent:.1f} %")


def draw_queue_info(queue: RemoteQueueInfo) -> None:
    print(f"Running    {queue.running}")
    print(f"Pending    {queue.pending}")
    print(f"Queue      {queue.total}")


def draw_runtime_info(runtime: RemoteRuntimeInfo) -> None:
    print(f"OS         {runtime.operating_system}")
    print(
        "RAM        "
        f"{format_gibibytes(runtime.ram_used_bytes)} / "
        f"{format_gibibytes(runtime.ram_total_bytes)}"
    )
    print(f"RAM load   {runtime.ram_usage_percent:.1f} %")
    print(f"ComfyUI    {runtime.comfyui_version}")
    print(f"Python     {runtime.python_version}")
    print(f"PyTorch    {runtime.pytorch_version}")


def show_ai_runtime() -> None:
    remote = RemoteManager()
    workstation = remote.workstation

    heartbeat = remote.heartbeat()
    system_stats = remote.comfyui_system_stats() if heartbeat.api_available else None
    queue_data = remote.comfyui_queue() if heartbeat.api_available else None

    gpu = (
        remote.primary_gpu_info(system_stats)
        if system_stats is not None
        else None
    )
    runtime = (
        remote.runtime_info(system_stats)
        if system_stats is not None
        else None
    )
    queue = (
        remote.queue_info(queue_data)
        if queue_data is not None
        else None
    )

    clear_screen()
    draw_header("AI RUNTIME")

    print(f"Name       {workstation.name}")
    print(f"Role       {workstation.role}")
    print(f"Host       {workstation.endpoint}")
    print()
    draw_heartbeat(heartbeat)

    if gpu is not None:
        print()
        draw_gpu_info(gpu)

    if queue is not None:
        print()
        draw_queue_info(queue)

    if runtime is not None:
        print()
        draw_runtime_info(runtime)

    if heartbeat.state == "ATTENTION":
        print()
        print("ComfyUI port is reachable, but API diagnostics are unavailable.")

    if heartbeat.state == "OFFLINE":
        print()
        print("Main Workstation or ComfyUI is not reachable on port 8188.")

    print()
    pause()

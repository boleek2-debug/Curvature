from core.remote import (
    RemoteGpuInfo,
    RemoteManager,
    RemoteQueueInfo,
    RemoteRuntimeInfo,
)

from .ui import clear_screen, draw_header, pause


GIBIBYTE = 1024**3


def format_gibibytes(value_bytes: int) -> str:
    return f"{value_bytes / GIBIBYTE:.2f} GB"


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

    system_stats = remote.comfyui_system_stats()
    queue_data = remote.comfyui_queue()

    if system_stats is not None:
        comfyui_state = "READY"
        gpu = remote.primary_gpu_info(system_stats)
        runtime = remote.runtime_info(system_stats)
    elif remote.comfyui_available():
        comfyui_state = "ATTENTION"
        gpu = None
        runtime = None
    else:
        comfyui_state = "OFFLINE"
        gpu = None
        runtime = None

    queue = (
        remote.queue_info(queue_data)
        if queue_data is not None
        else None
    )

    clear_screen()
    draw_header("AI RUNTIME")

    print(f"Name       {workstation.name}")
    print(f"Role       {workstation.role}")
    print(f"Endpoint   {workstation.endpoint}")
    print(f"ComfyUI    [{comfyui_state}]")

    if gpu is not None:
        print()
        draw_gpu_info(gpu)

    if queue is not None:
        print()
        draw_queue_info(queue)

    if runtime is not None:
        print()
        draw_runtime_info(runtime)

    if comfyui_state == "ATTENTION":
        print()
        print("Runtime diagnostics unavailable.")

    print()
    pause()

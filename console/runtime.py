from core.remote import RemoteManager

from .ui import clear_screen, draw_header, pause


def show_ai_runtime() -> None:
    remote = RemoteManager()
    workstation = remote.workstation
    comfyui_state = "READY" if remote.comfyui_available() else "OFFLINE"

    clear_screen()
    draw_header("AI RUNTIME")

    print(f"Name       {workstation.name}")
    print(f"Role       {workstation.role}")
    print(f"Endpoint   {workstation.endpoint}")
    print(f"ComfyUI    [{comfyui_state}]")
    print()

    pause()

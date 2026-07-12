from .workstation import Workstation


class RemoteManager:
    COMFYUI_PORT = 8188

    def __init__(self):
        self.workstation = Workstation(
            name="Main Workstation",
            role="AI Runtime",
            endpoint="100.98.198.68",
        )

    def comfyui_available(self) -> bool:
        return self.workstation.service_available(
            port=self.COMFYUI_PORT,
        )

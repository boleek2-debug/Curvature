from .workflow import Workflow


class WorkflowManager:
    def __init__(self):
        self._workflows = [
            Workflow(
                name="Image Generation",
                description="ComfyUI image generation pipeline.",
            ),
            Workflow(
                name="Video Generation",
                description="Video generation pipeline.",
            ),
            Workflow(
                name="World Builder",
                description="World production workflow.",
            ),
        ]

    def all(self) -> list[Workflow]:
        return self._workflows

    def get(self, name: str) -> Workflow | None:
        for workflow in self._workflows:
            if workflow.name == name:
                return workflow

        return None

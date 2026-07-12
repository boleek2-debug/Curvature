from dataclasses import dataclass


OFFLINE = "OFFLINE"
READY = "READY"
RUNNING = "RUNNING"
COMPLETED = "COMPLETED"
FAILED = "FAILED"


@dataclass
class Workflow:

    name: str
    state: str = OFFLINE
    description: str = ""

    def ready(self):
        self.state = READY

    def run(self):
        self.state = RUNNING

    def complete(self):
        self.state = COMPLETED

    def fail(self):
        self.state = FAILED

    def reset(self):
        self.state = OFFLINE

    def is_ready(self):
        return self.state == READY

    def is_running(self):
        return self.state == RUNNING

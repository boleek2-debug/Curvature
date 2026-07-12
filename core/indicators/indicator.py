from dataclasses import dataclass


@dataclass
class Indicator:
    name: str
    state: str
    details: str = ""

from core.indicators.indicator import Indicator


def workshop_status() -> list[Indicator]:
    return [
        Indicator(
            name="Telemetry",
            state="READY",
            details="Core telemetry operational.",
        ),
        Indicator(
            name="Diagnostics",
            state="READY",
            details="Diagnostic subsystem operational.",
        ),
        Indicator(
            name="AI Engine",
            state="OFFLINE",
            details="AI services not connected.",
        ),
        Indicator(
            name="Remote Workstation",
            state="OFFLINE",
            details="No remote workstation available.",
        ),
        Indicator(
            name="Workflow Engine",
            state="OFFLINE",
            details="Workflow engine not implemented.",
        ),
    ]

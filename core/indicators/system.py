from .indicator import Indicator


def telemetry_indicator():

    return Indicator(
        name="Telemetry",
        state="READY",
        details="Core telemetry operational."
    )

from core.telemetry import Telemetry


telemetry = Telemetry()


def test_cpu():
    value = telemetry.cpu()

    assert isinstance(value, float)
    assert 0 <= value <= 100


def test_memory():
    ram = telemetry.memory()

    assert ram["used_gb"] <= ram["total_gb"]
    assert 0 <= ram["percent"] <= 100


def test_gpu():
    gpu = telemetry.gpu()

    assert gpu["temperature_c"] > 0
    assert gpu["memory_used_mb"] <= gpu["memory_total_mb"]


def test_disk():
    disk = telemetry.disk()

    assert disk["free_gb"] >= 0
    assert disk["used_gb"] <= disk["total_gb"]

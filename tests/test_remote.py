from unittest.mock import Mock, patch

from core.remote import (
    RemoteGpuInfo,
    RemoteManager,
    RemoteQueueInfo,
    RemoteRuntimeInfo,
)
from core.remote.workstation import Workstation


def test_remote_gpu_info_calculates_vram_usage() -> None:
    gpu = RemoteGpuInfo(
        name="NVIDIA GeForce RTX 4060",
        vram_total_bytes=8 * 1024**3,
        vram_free_bytes=6 * 1024**3,
    )

    assert gpu.vram_used_bytes == 2 * 1024**3
    assert gpu.vram_usage_percent == 25.0


def test_remote_queue_info_calculates_total() -> None:
    queue = RemoteQueueInfo(
        running=1,
        pending=3,
    )

    assert queue.total == 4


def test_remote_runtime_info_calculates_ram_usage() -> None:
    runtime = RemoteRuntimeInfo(
        operating_system="win32",
        ram_total_bytes=32 * 1024**3,
        ram_free_bytes=24 * 1024**3,
        comfyui_version="0.26.2",
        python_version="3.13.12",
        pytorch_version="2.10.0+cu130",
    )

    assert runtime.ram_used_bytes == 8 * 1024**3
    assert runtime.ram_usage_percent == 25.0


def test_primary_gpu_info_reads_comfyui_system_stats() -> None:
    manager = RemoteManager()
    system_stats = {
        "devices": [
            {
                "name": "NVIDIA GeForce RTX 4060",
                "vram_total": 8_589_934_592,
                "vram_free": 6_442_450_944,
                "torch_vram_total": 8_589_934_592,
                "torch_vram_free": 6_442_450_944,
            }
        ]
    }

    gpu = manager.primary_gpu_info(system_stats)

    assert gpu is not None
    assert gpu.name == "NVIDIA GeForce RTX 4060"
    assert gpu.vram_total_bytes == 8_589_934_592
    assert gpu.vram_free_bytes == 6_442_450_944
    assert gpu.vram_used_bytes == 2_147_483_648
    assert gpu.vram_usage_percent == 25.0


def test_primary_gpu_info_rejects_missing_devices() -> None:
    manager = RemoteManager()

    assert manager.primary_gpu_info({}) is None
    assert manager.primary_gpu_info({"devices": []}) is None


def test_queue_info_reads_comfyui_queue() -> None:
    manager = RemoteManager()
    queue_data = {
        "queue_running": [["running-job"]],
        "queue_pending": [["pending-job-1"], ["pending-job-2"]],
    }

    queue = manager.queue_info(queue_data)

    assert queue is not None
    assert queue.running == 1
    assert queue.pending == 2
    assert queue.total == 3


def test_queue_info_rejects_invalid_payload() -> None:
    manager = RemoteManager()

    assert manager.queue_info({}) is None
    assert manager.queue_info(
        {
            "queue_running": [],
            "queue_pending": "invalid",
        }
    ) is None


def test_runtime_info_reads_comfyui_system_stats() -> None:
    manager = RemoteManager()
    system_stats = {
        "system": {
            "os": "win32",
            "ram_total": 34_256_003_072,
            "ram_free": 18_291_163_136,
            "comfyui_version": "0.26.2",
            "python_version": "3.13.12",
            "pytorch_version": "2.10.0+cu130",
        }
    }

    runtime = manager.runtime_info(system_stats)

    assert runtime is not None
    assert runtime.operating_system == "win32"
    assert runtime.ram_total_bytes == 34_256_003_072
    assert runtime.ram_free_bytes == 18_291_163_136
    assert runtime.comfyui_version == "0.26.2"
    assert runtime.python_version == "3.13.12"
    assert runtime.pytorch_version == "2.10.0+cu130"


def test_runtime_info_rejects_invalid_payload() -> None:
    manager = RemoteManager()

    assert manager.runtime_info({}) is None
    assert manager.runtime_info({"system": {}}) is None


def test_comfyui_system_stats_uses_verified_endpoint() -> None:
    manager = RemoteManager()
    expected = {
        "devices": [
            {
                "name": "NVIDIA GeForce RTX 4060",
                "vram_total": 8_589_934_592,
                "vram_free": 6_442_450_944,
            }
        ]
    }

    manager.workstation.get_json = Mock(return_value=expected)

    result = manager.comfyui_system_stats()

    assert result == expected
    manager.workstation.get_json.assert_called_once_with(
        port=8188,
        path="/system_stats",
    )


def test_comfyui_queue_uses_verified_endpoint() -> None:
    manager = RemoteManager()
    expected = {
        "queue_running": [],
        "queue_pending": [],
    }

    manager.workstation.get_json = Mock(return_value=expected)

    result = manager.comfyui_queue()

    assert result == expected
    manager.workstation.get_json.assert_called_once_with(
        port=8188,
        path="/queue",
    )


def test_workstation_get_json_returns_dictionary() -> None:
    workstation = Workstation(
        name="Test",
        role="AI Runtime",
        endpoint="thing",
    )
    response = Mock()
    response.__enter__ = Mock(return_value=response)
    response.__exit__ = Mock(return_value=False)

    with patch(
        "core.remote.workstation.urlopen",
        return_value=response,
    ) as mocked_urlopen:
        with patch(
            "core.remote.workstation.json.load",
            return_value={"devices": []},
        ):
            result = workstation.get_json(
                port=8188,
                path="/system_stats",
            )

    assert result == {"devices": []}
    mocked_urlopen.assert_called_once_with(
        "http://thing:8188/system_stats",
        timeout=2.0,
    )

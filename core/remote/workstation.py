import json
import socket
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.request import urlopen


class Workstation:
    def __init__(
        self,
        name: str,
        role: str,
        endpoint: str,
    ):
        self.name = name
        self.role = role
        self.endpoint = endpoint

    def service_available(
        self,
        port: int,
        timeout: float = 1.0,
    ) -> bool:
        try:
            with socket.create_connection(
                (self.endpoint, port),
                timeout=timeout,
            ):
                return True
        except (TimeoutError, ConnectionError, OSError):
            return False

    def get_json(
        self,
        port: int,
        path: str,
        timeout: float = 2.0,
    ) -> dict[str, Any] | None:
        normalized_path = path if path.startswith("/") else f"/{path}"
        url = f"http://{self.endpoint}:{port}{normalized_path}"

        try:
            with urlopen(url, timeout=timeout) as response:
                payload = json.load(response)
        except (
            HTTPError,
            URLError,
            TimeoutError,
            ConnectionError,
            OSError,
            json.JSONDecodeError,
        ):
            return None

        if not isinstance(payload, dict):
            return None

        return payload

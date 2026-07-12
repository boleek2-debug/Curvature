import socket


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

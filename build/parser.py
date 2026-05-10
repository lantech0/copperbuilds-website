from pathlib import Path


def parse_config(client_folder) -> dict:
    config_path = Path(client_folder) / "client.env"
    if not config_path.exists():
        raise FileNotFoundError(f"client.env not found in {client_folder}")
    config = {}
    with open(config_path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            if "=" in line:
                key, _, value = line.partition("=")
                config[key.strip()] = value.strip()
    return config

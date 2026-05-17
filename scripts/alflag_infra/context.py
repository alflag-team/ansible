from pathlib import Path


DEFAULT_SITE = "kanagawa01"
DEFAULT_PLAYBOOK = "site"


def repo_root() -> Path:
    return Path(__file__).resolve().parents[2]


def ansible_config_path() -> Path:
    return repo_root() / "ansible.cfg"


def inventory_path(site: str) -> Path:
    path = repo_root() / "inventories" / site / "hosts.yml"
    if not path.is_file():
        raise RuntimeError(f"Unknown site '{site}': inventory not found at {path}")
    return path


def playbook_path(playbook: str) -> Path:
    path = repo_root() / "playbooks" / f"{playbook}.yml"
    if not path.is_file():
        raise RuntimeError(f"Unknown playbook '{playbook}': playbook not found at {path}")
    return path

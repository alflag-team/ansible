import os
import shlex
import subprocess
from pathlib import Path

from .context import ansible_config_path, inventory_path, playbook_path, repo_root


class AnsibleRunner:
    def __init__(self, site: str) -> None:
        self.repo_root = repo_root()
        self.inventory = inventory_path(site)

    def playbook(
        self,
        playbook: str,
        limit: str | None = None,
        check: bool = False,
        diff: bool = False,
    ) -> None:
        cmd = [
            "ansible-playbook",
            "-i",
            self._relative(self.inventory),
            self._relative(playbook_path(playbook)),
        ]

        self._append_limit(cmd, limit)
        if check:
            cmd.append("--check")
        if diff:
            cmd.append("--diff")

        self._run(cmd)

    def adhoc(self, module: str, limit: str | None = None) -> None:
        cmd = [
            "ansible",
            "all",
            "-i",
            self._relative(self.inventory),
            "-m",
            module,
        ]

        self._append_limit(cmd, limit)
        self._run(cmd)

    def inventory_graph(self) -> None:
        cmd = [
            "ansible-inventory",
            "-i",
            self._relative(self.inventory),
            "--graph",
        ]
        self._run(cmd)

    def _run(self, cmd: list[str]) -> None:
        env = os.environ.copy()
        env["ANSIBLE_CONFIG"] = str(ansible_config_path())

        print(f"Running: {shlex.join(cmd)}", flush=True)
        subprocess.run(cmd, check=True, cwd=self.repo_root, env=env)

    def _relative(self, path: Path) -> str:
        return str(path.relative_to(self.repo_root))

    @staticmethod
    def _append_limit(cmd: list[str], limit: str | None) -> None:
        if limit and limit.strip():
            cmd.extend(["--limit", limit])

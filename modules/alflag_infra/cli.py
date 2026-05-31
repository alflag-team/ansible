import subprocess

import fire

from .ansible import AnsibleRunner
from .context import DEFAULT_PLAYBOOK, DEFAULT_SITE


class Infra:
    def ping(self, site: str = DEFAULT_SITE, limit: str | None = None) -> None:
        self._run(lambda: AnsibleRunner(site=site).adhoc(module="ping", limit=limit))

    def check(
        self,
        site: str = DEFAULT_SITE,
        playbook: str = DEFAULT_PLAYBOOK,
        limit: str | None = None,
    ) -> None:
        self._run(
            lambda: AnsibleRunner(site=site).playbook(
                playbook=playbook,
                limit=limit,
                check=True,
                diff=False,
            )
        )

    def diff(
        self,
        site: str = DEFAULT_SITE,
        playbook: str = DEFAULT_PLAYBOOK,
        limit: str | None = None,
    ) -> None:
        self._run(
            lambda: AnsibleRunner(site=site).playbook(
                playbook=playbook,
                limit=limit,
                check=True,
                diff=True,
            )
        )

    def apply(
        self,
        site: str = DEFAULT_SITE,
        playbook: str = DEFAULT_PLAYBOOK,
        limit: str | None = None,
    ) -> None:
        self._run(
            lambda: AnsibleRunner(site=site).playbook(
                playbook=playbook,
                limit=limit,
                check=False,
                diff=False,
            )
        )

    def inventory(self, site: str = DEFAULT_SITE) -> None:
        self._run(lambda: AnsibleRunner(site=site).inventory_graph())

    @staticmethod
    def _run(action) -> None:
        try:
            action()
        except RuntimeError as exc:
            raise SystemExit(f"Error: {exc}") from None
        except FileNotFoundError as exc:
            command = exc.filename or "required command"
            raise SystemExit(f"Error: {command} was not found in PATH") from None
        except subprocess.CalledProcessError as exc:
            raise SystemExit(f"Error: command failed with exit code {exc.returncode}") from None


def main() -> None:
    fire.Fire(Infra)

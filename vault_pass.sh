#!/bin/bash

set -euo pipefail

if [[ -n "${ANSIBLE_VAULT_PASSWORD:-}" ]]; then
  printf "%s" "${ANSIBLE_VAULT_PASSWORD}"
  exit 0
fi

if [[ -f ./secrets/ansible_vault.env ]]; then
  # shellcheck disable=SC1091
  source ./secrets/ansible_vault.env
fi

if [[ -z "${ANSIBLE_VAULT_PASSWORD:-}" ]]; then
  echo "ANSIBLE_VAULT_PASSWORD is not set" >&2
  exit 1
fi

printf "%s" "${ANSIBLE_VAULT_PASSWORD}"

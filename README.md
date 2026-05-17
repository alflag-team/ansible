# Ansible

サーバ構成を管理している Ansible のコードが管理されています。

## Atlas 経由の実行

この repository は Atlas の script release として扱えるようにしています。
Atlas は実行入口と run log を担当し、実際の構成適用は Ansible が担当します。

```bash
atlas scripts install git+https://github.com/alflag-team/ansible.git#feature/atlas-infra-runner --name alflag-infra
atlas scripts shims

atlas run infra inventory
atlas run infra ping
atlas run infra check
atlas run infra diff
atlas run infra apply
```

## Local Development

```bash
python -m pip install -e .
infra inventory
infra ping
infra check
```

実行例:

```bash
infra diff --site kanagawa01 --playbook baseline
infra apply --site kanagawa01 --playbook baseline --limit kng01-recursive-dns-01
```

`infra` は既定で `site=kanagawa01`、`playbook=site` を使います。
実行前には内部で呼び出す Ansible command を表示します。

Vault password は `secrets/ansible_vault.env` または `ANSIBLE_VAULT_PASSWORD`
環境変数から読み込みます。

## Ansible Vault

Ansible Vault によって、機密情報を暗号化しています。

### 暗号化

```bash
ansible-vault encrypt group_vars/all/vault
```

### 復号化

```bash
ansible-vault decrypt group_vars/all/vault
```

## プレイブックの実行

Ansible のプレイブックを実行するには、以下のコマンドを実行します。

```bash
ansible-playbook -i hosts.yml playbook.yml --ask-vault-pass
```

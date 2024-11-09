# Ansible

サーバ構成を管理している Ansible のコードが管理されています。

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

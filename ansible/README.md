# Ansible-playbook のテスト方法

## Version

- Ansible 2.9.4
- boto 2.49.0
- boto3 1.12.5
- botocore 1.15.5

boto,boto3,botocore については最新をインストールすることを推奨します。

## playbook の実行方法

### 事前準備

#### AWS の IAM ユーザー作成

Ansible 及び、CircleCI を実行する IAM ユーザーを作成します。  
作成した IAM ユーザーに対し、PowerUserAccess の IAM ポリシーを設定します。

#### 環境変数の設定

先程作成した IAM ユーザーのアクセスキーとシークレットアクセスキーを生成します。
生成したアクセスキーとシークレットアクセスキーを環境変数としてセットします。

```
% export AWS_ACCESS_KEY_ID=アクセスキー
% export AWS_SECRET_ACCESS_KEY=シークレットアクセスキー
```

#### ansible.cfg の作成

```
[defaults]
inventory = ansible/hosts/ec2.py
retry_files_enabled = False
deprecation_warnings=False
private_key_file=~/.ssh/hello_auto_key.pem

[privilege_escalation]
become = False

[ssh_connection]
ssh_args = -o StrictHostKeyChecking=no
```

### Playbook 実行

```
# cd Hello-Automation-World-Product/
# ansible-playbook ansible/playbook.yml
```

# ブランチ運用
大前提として、個別のブランチは章ごと(チケットごと)に切って作業する。  
また、事故った時のためにマージ後のブランチも残しておく。  
・ブランチの命名規則 ： feature/ + JIRAチケット番号(feature/HAW-30)  
・マージ先 ： featureブランチ -> developブランチ  

---
## Versions
 - python 3.8.0
 - Django 2.1
 - nginx 1.16.1
 - uWSGI 2.0.18
 - mysql 5.6

---
## ローカル: アプリ起動方法
```
// manage.pyのディレクトリに移動
$ cd haw/

// 必要なパッケージのインストール
$ pip install -r requirements.txt

// modelからマイグレーションファイルを作成
$ python manage.py makemigrations

// 作成したマイグレーションファイルをDBに反映
$ python manage.py migrate

// サーバーを起動
$ python manage.py runserver

// ブラウザでアクセス
http://127.0.0.1:8000/
```

---
## docker-compose: アプリ起動方法
```
// ビルドしてコンテナを作成し、起動
$ docker-compose up -d --build

// コンテナのプロセスを確認
$ docker-compose ps

// コンテナを停止し、削除
$ docker-compose down
```

---
## テスト実行方法
### 前提条件
 - アプリ起動方法の手順に記載のパッケージが、インストールされていること
```
// manage.pyのディレクトリに移動
$ cd haw

// テストを実行
$ python manage.py test
```

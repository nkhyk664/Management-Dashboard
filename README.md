Docker起動
```
docker compose up --build
```

挙動の確認（ポートフォリオ用のサンプルデータで動作します）
```
http://0.0.0.0:8501
```


停止
```
Ctrl + C
```
Docker環境をまるごと削除
```
docker compose -f docker-compose.yml down --rmi all --volumes --remove-orphans
```

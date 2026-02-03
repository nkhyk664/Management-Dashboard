Docker起動
```
docker compose up --build
```

Docker環境をまるごと削除
```
docker compose -f docker-compose.yml down --rmi all --volumes --remove-orphans
```
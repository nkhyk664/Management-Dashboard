FROM python:3.11-slim

# 作業フォルダ
WORKDIR /app

# 必要なパッケージのインストール
COPY requirements.txt .

# ライブラリをインストール
RUN pip install --no-cache-dir -r requirements.txt

# アプリ本体をコピー
COPY . .

# Streamlistが使うポート
EXPOSE 8501

# Streamlitの起動
CMD ["streamlit", "run", "home.py", "--server.port=8501", "--server.address=0.0.0.0"]
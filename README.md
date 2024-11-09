# colab2local <中文>

一個簡單的工具，用於將 Google Colab 結果同步到本地環境。

## 功能特點
- 利用 Colab 雲端 GPU 進行運算，本地接收結果
- 使用 ngrok 將結果轉發到特定的網址
- 透過 POST 方法接收結果

## Usage
1. 用 Google Colab 開啟 Colab2.local_POST.ipynb。
2. 註冊 ngrok，並將 auth token 填入 Colab 筆記本中。
3. 運行 Colab 筆記本，並記下 ngrok 網址 (https://xxxx.ngrok.app)。
4. 修改 local.py 中的 `ngrok_app` 變數，改為新生成的 ngrok 網址。
5. 運行 local.py，本地將會收到 POST 請求。

## Requirements
- Google Colab
- Python 3.6+
- requests library


# colab2local <English>

A simple tool for synchronizing Google Colab results to your local environment.

## Features
- Leverage Colab's cloud GPU for computation while receiving results locally
- Use ngrok to forward results to a specific URL
- Receive results via POST method

## Usage
1. Open Colab2local_POST.ipynb in Google Colab.
2. Register for ngrok and fill in your auth token in the Colab notebook.
3. Run the Colab notebook and note down the ngrok URL (https://xxxx.ngrok.app).
4. Modify the `ngrok_app` variable in local.py with your newly generated ngrok URL.
5. Run local.py, and your local machine will receive POST requests.

## Requirements
- Google Colab
- Python 3.6+
- requests library
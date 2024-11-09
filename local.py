import requests
import json

ngrok_app = "http://60c8-34-42-98-246.ngrok-free.app" # 更新 XXX.ngrok-free.app

demo_text = "實驗用文字，確保可以傳輸中文～"

# url = ngrok_app + '/'
url = ngrok_app + '/test'

r = requests.post(
    url=url,
    json={"text": demo_text},
)
r.encoding = "utf_8" # other encoding: utf_8 utf_16 gbk gb18030 big5hkscs
requests = r.text
print(requests)
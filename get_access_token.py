import os
from libs.jsonfile import json_to_dic,save_json
import time
from dotenv import load_dotenv
from libs.requests import request_post
import requests



def get_access_token():
  """
  freeeAPIからアクセストークン取得する関数
  """
  d = json_to_dic("json/access_token.json")
  print(d)

  #jsonからcreated_at と expires_in 取得
  #有効期限がすぎていれば refresh tokenを用いてaccess_token再発行
  if time.time() > d["created_at"] + d["expires_in"]:
    headers = {
      "Content-Type":"application/x-www-form-urlencoded"
    }
    load_dotenv()
    payload = {
      "grant_type":"refresh_token",
      "client_id":os.environ.get("CLIENT_ID"),
      "client_secret":os.environ.get("CLIENT_SECRET"),
      "refresh_token":d["refresh_token"]
    }
    print(payload)

    result =request_post(
      url="https://accounts.secure.freee.co.jp/public_api/token",headers=headers,payload=payload
      )
    print(result)

    if result[0] == requests.codes.ok:
      save_json(
        json_data=result[1],path="json/access_token.json"
      )
    else:
      print(f"エラーコード:{result[0]}\n内容:{result[1]}")









if __name__ == "__main__":
    get_access_token()
import requests


def request_get(url: str, payload={},headers={}):
  """
  リクエストGETを送る関数
  """

  result = requests.get(
    url, params=payload,headers=headers
    );
  return [result.status_code,result.json()]

def request_post(url: str, payload={},headers={}):
  """
  リクエストGETを送る関数
  """

  result = requests.post(
    url, params=payload,headers=headers
    );
  return [result.status_code,result.json()]

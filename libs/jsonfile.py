import json


def json_to_dic(path: str):
  """
  jsonファイルから辞書型配列に格納

  Parameters
  ----------
  path: str
  jsonがあるpath
  """
  d = {}
  with open(path, mode="r") as f:
    d = json.load(f)
  return d

def save_json(path: str,json_data: dict):
  """
  データをjsonファイルに保存

  Parameters
  ----------
  path: str
  格納先

  json_data: dict
  保存したい辞書型データ
  """
  with open(path, 'w') as f:
    json.dump(json_data, f, indent=2, ensure_ascii=False)
# freee のアカウントから access token を取得する

access token があること前提で考えているので、その有効期限が切れた場合に refresh token を用いて
access token を再取得する

## 必要ファイル

```
acces_token.json --- access tokenが入っているjsonファイル(jsonフォルダ内に作成)
.env --- client_id, client_secret
```

# SF Streaming Sample

Salesforce Streaming APIを利用できる `salesforce-streaming-client`を試したもの。

## 必要なもの
`requirements.txt`で必要ライブラリをインストールしてください。

また、`main.py`にある通り、先頭で以下のソースを呼び出してください。

```python
from gevent import monkey
monkey.patch_all()
```

## Environments
|Title|Version|
|---|---|
|Python|3.7.3|
|Visual Studio Code|1.46.0|
|Python Virtual Environment tool|venv|

## Reference

https://github.com/SalesforceFoundation/salesforce-streaming-client
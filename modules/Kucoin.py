import requests, time, hashlib, hmac, base64, json

class Client():
  def __init__(self, api_key, api_secret, api_passphrase) -> None:
      self.api_key = api_key
      self.api_secret = api_secret
      self.api_passphrase = api_passphrase

      self.url = 'https://api-futures.kucoin.com/api/v1/{}'

  def account_overview(self, param='', api='account-overview'):
    # pram Ex: ?currency=XBT'

    response = requests.get(
      self.url.format(api) + param,
      headers=self.header(api + param)
    )

    return (response)

  def transaction_history(self, param='', api='transaction-history'):
    # pram Ex: ?offset=1&forward=true&maxCount=50
    
    response = requests.get(
      self.url.format(api) + param,
      headers=self.header(api + param)
    )

    return (response)

  def position(self, param='?symbol=XBTUSDM', api='position'):
    response = requests.get(
      self.url.format(api) + param,
      headers=self.header(api + param)
    )

    return (response)

  def header(self, url):
    now = int(time.time() * 1000)
    str_to_sign = str(now) + 'GET/api/v1/{}'.format(url)

    signature = base64.b64encode(
      hmac.new(self.api_secret.encode('utf-8'), str_to_sign.encode('utf-8'),
      hashlib.sha256).digest()
    )

    passphrase = base64.b64encode(
      hmac.new(self.api_secret.encode('utf-8'),
      self.api_passphrase.encode('utf-8'),
      hashlib.sha256).digest()
    )

    headers = {
      "KC-API-SIGN": signature,
      "KC-API-TIMESTAMP": str(now),
      "KC-API-KEY": self.api_key,
      "KC-API-PASSPHRASE": passphrase,
      "KC-API-KEY-VERSION": "2"
    }

    return headers


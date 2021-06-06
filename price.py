import requests

BAND_ORACLE_URL = "https://asia-rpc.bandchain.org/oracle/request_prices"

def get_price(symbols):
  # assume WETH price == ETH price
  symbols = [("ETH" if symbol =="WETH" else symbol) for symbol in symbols]
  payload = {
      "symbols": symbols,
      "min_count": 10,
      "ask_count": 16
  }
  response = requests.request("POST", BAND_ORACLE_URL, json=payload).json()
  return [int(result["px"])/1e9 for result in response["result"]]



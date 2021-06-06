import json
from contracts import web3, erc20_contract_factory, uniswap_v2_pair_contract_factory


ERC20_ABI_JSON = "abis/ERC20.json"
ERC20_ABI = json.load(open(ERC20_ABI_JSON))

def get_token_info(token_address):
  token_contract = erc20_contract_factory(token_address)
  token_symbol = token_contract.functions.symbol().call()
  token_decimals = token_contract.functions.decimals().call()
  return {"address":token_address,"symbol":token_symbol,"decimals":token_decimals}

def get_lp_tokens_info(uniswap_pair_adress):
  uniswap_lp_contract = uniswap_v2_pair_contract_factory(uniswap_pair_adress)
  token0 = uniswap_lp_contract.functions.token0().call()
  token1 = uniswap_lp_contract.functions.token1().call()
  token0_data = get_token_info(token0)
  token1_data = get_token_info(token1)
  [reserve0,reserve1,_] = uniswap_lp_contract.functions.getReserves().call()
  token0_data["reserves"] = reserve0
  token1_data["reserves"] = reserve1
  return {0:token0_data, 1:token1_data}

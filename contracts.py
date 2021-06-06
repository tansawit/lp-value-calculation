import json
from web3 import Web3

UNISWAP_PAIR_ABI_JSON = "abis/UniswapV2Pair.json"
UNISWAP_ROUTER_ABI = json.load(open(UNISWAP_PAIR_ABI_JSON))

ERC20_ABI_JSON = "abis/ERC20.json"
ERC20_ABI = json.load(open(ERC20_ABI_JSON))

web3 = Web3(Web3.HTTPProvider("https://mainnet.infura.io/v3/394ff03e59644af0a007bed4cdc414d4"))

def erc20_contract_factory(token_address):
  token_contract = web3.eth.contract(address=token_address,abi=ERC20_ABI)
  return token_contract

def uniswap_v2_pair_contract_factory(pair_address):
  pair_contract= web3.eth.contract(address = pair_address, abi = UNISWAP_ROUTER_ABI)
  return pair_contract

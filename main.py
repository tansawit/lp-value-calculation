import json
from price import get_price
from lp import get_lp_tokens_info
from contracts import erc20_contract_factory

UNISWAP_PAIR_ETH_USDT_LP_TOKEN = "0x0d4a11d5EEaaC28EC3F61d100daF4d40471f1852"
TEST_ADDRESS = "0xd54D0ed024894AfF13d90f88de761DFb2E85cfe8"

def main():
  # get token info
  lp_info = get_lp_tokens_info(UNISWAP_PAIR_ETH_USDT_LP_TOKEN)
  token_prices = get_price([lp_info[0]["symbol"], lp_info[1]["symbol"]])
  for idx,lp in lp_info.items():
    print(f"printing token{idx} details:")
    print(f"symbol:{lp['symbol']}")
    print(f"address:{lp['address']}")
    print(f"decimals:{lp['decimals']}")
    print(f"reserves:{lp['reserves']}")
    print(f"latest price: {token_prices[idx]} USD per token\n")
  # get pair token info
  pair_contract = erc20_contract_factory(UNISWAP_PAIR_ETH_USDT_LP_TOKEN)
  pair_total_supply = pair_contract.functions.totalSupply().call()
  address_lp_balance = pair_contract.functions.balanceOf(TEST_ADDRESS).call()
  address_pool_ownership = address_lp_balance/pair_total_supply
  print(f"printing pair token info:")
  print(f"total supply: {pair_total_supply}")
  print(f"test address balance: {address_lp_balance}")
  print(f"test address pool ownership: {address_pool_ownership*100} %")

  # get portion of underlying tokens owned by test address
  total_position_value = 0
  for idx,lp in lp_info.items():
    address_token_balance = (lp["reserves"]/10**lp["decimals"]) * address_pool_ownership
    print(f"test address token{idx} share: {address_token_balance} tokens (@{token_prices[idx]} USD per token)")
    total_position_value += address_token_balance * token_prices[idx]

  print(f"\ntotal value of test address's LP position: {total_position_value} USD")

if __name__ == "__main__":
  main()

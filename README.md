# LP Position Value Calculation

For a given address, the value of their position in a liquidity position is calculated as follows

1) First, their pool ownership ratio is calculated. This is the balance of the pool's LP tokens they hold vs the total supply (calcualted by `lp_token.balanceOf(address)/lp_token.totalSupply()`)
2) Then we get the amount of each reserve tokens are currently in the pool (using the pool's `getReserves()` method)
     - This function call returns 3 variables, `reserve0`, `reserve1`, and `blockTimestamp`. The first two.
3) Then, for each of the reserve token (`token0` and `token1`): we query the token's decimals (using the token contract's `decimals()` method)
4) The balance of each reserve token held by the address is then calculated by `address_token_balance  = token_reserve/10**token_decimals * address_pool_ownership`
5) We then obtain the price price of each of the reserve token, either using and external oracle or the pool's built in oracle (`address_token_value = address_token_balance * token_price`)
6) The overall LP position value of the address is then calculated by `address_position_value = address_token0_value + address_token1_value`

Overall, the pseudocode are as follows:

```
token0 = lp_token.token0()
token0_decimals = token0.decimals()
token0_price  = get_price(token0)

token1 = lp_token.token1()
token1_decimals = token1.decimals()
token1_price  = get_price(token1)

address_lp_token_balance = lp_token.balanceOf(address)
lp_token_total_supply = lp_token.totalSupply()
(token0_reserves,token1_reserves,_) = lp_token.getReserves()

address_pool_ownership = (address_lp_token_balance/lp_token_total_supply)

address_token0_balance = token0_reserves/10**token0_decimals * address_pool_ownership
address_token1_balance = token1_reserves/10**token1_decimals * address_pool_ownership

address_token0_value = address_token0_balance * token0_price
address_token1_value = address_token1_balance * token1_price

address_position_value = address_token0_value + address_token1_value
```

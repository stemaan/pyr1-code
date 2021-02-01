coins = (5, 2, 1, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01)
coins_to_change = [0, 0, 0, 0, 0, 0, 0, 0, 0]
# (5, 2, 1, 0...)
# [1, 1, 1, 0, 0,0,0,0,0]

cash = 20
total_value = 8.30
change = cash - total_value # 11.70 -> 2x5, 1x1, 0.5x1, 0.2x1
idx = 0

for coin in coins:
    if change > 0 and change >= coin:
        quantity = change // coin   # 2
        value_of_coins = quantity * coin    # 2 * 5
        # bez zaokraglnie w kodzie wystepuje bug
        # change = change - value_of_coins    # 11.70 - (2 * 5)
        change = round(change - value_of_coins, 2)    # 11.70 - (2 * 5)

        coins_to_change[idx] = quantity

    idx += 1

print(coins_to_change)
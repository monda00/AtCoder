price = int(input())

coin_500 = price // 500
price -= 500 * coin_500
coin_5 = price // 5

price -= 5 * coin_5
coin_100 = price // 100
price -= 100 * coin_100
coin_50 = price // 50
price -= 50 * coin_50
coin_10 = price // 10
price -= 10 * coin_10
coin_1 = price

print(1000 * coin_500 + coin_5 * 5)

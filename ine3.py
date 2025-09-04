#dont use forloop , add 10 and divide the result with 100
prices_usd = [100, 250, 75, 300, 150]


result = list(map(lambda x: (x + 10) / 100, prices_usd))

print(result)

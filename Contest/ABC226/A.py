from decimal import Decimal, ROUND_HALF_UP

x = float(input())

ans = Decimal(str(x)).quantize(Decimal('0'), rounding=ROUND_HALF_UP)

print(ans)

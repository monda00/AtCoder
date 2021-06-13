# ビット演算
bx = 0b1101
by = 0b1010
x = 13
y = 10
xb = bin(x)
yb = bin(y)
print(bx)
print(by)
print(x)
print(y)
print(xb)
print(yb)

# AND（ビット単位）
print(x & y)
print(bin(x & y))

# OR（ビット単位）
print(x | y)
print(bin(x | y))

# XOR（ビット単位）
print(x ^ y)
print(bin(x ^ y))

# 反転（ビット単位）
print(~x)
print(bin(~x))
print(~y)
print(bin(~y))

# 右シフト
print(x >> 0)
print(bin(x >> 0))
print(x >> 1)
print(bin(x >> 1))
print(x >> 2)
print(bin(x >> 2))

# 左シフト
print(x << 0)
print(bin(x << 0))
print(x << 1)
print(bin(x << 1))
print(x << 2)
print(bin(x << 2))

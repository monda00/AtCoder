allowable_time = int(input())
takoyaki_num = int(input())
takoyaki_time_li = list(map(int, input().split()))
customer_num = int(input())
customer_time_li = list(map(int, input().split()))

# 客がきたときに最小時間で提供可能なたこ焼きを探す
for customer_time in customer_time_li:
    for tokoyaki_time in takoyaki_time_li:


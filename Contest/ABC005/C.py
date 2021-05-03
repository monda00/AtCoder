def exist_takoyaki(customer_time, takoyaki_time):
    return takoyaki_time != -1 and takoyaki_time + allowable_time >= customer_time \
        and customer_time >= takoyaki_time

allowable_time = int(input())
takoyaki_num = int(input())
takoyaki_time_li = list(map(int, input().split()))
customer_num = int(input())
customer_time_li = list(map(int, input().split()))

# 客がきたときに最小時間で提供可能なたこ焼きを探す
# 使ったたこ焼きは-1にする
for customer_time in customer_time_li:
    for i, takoyaki_time in enumerate(takoyaki_time_li):
        if exist_takoyaki(customer_time, takoyaki_time):
            takoyaki_time_li[i] = -1
            break
        if len(takoyaki_time_li) == i + 1:
            print('no')
            exit()
print('yes')


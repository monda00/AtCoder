from collections import*

char_num, changed_limit = map(int,input().split())
input_string = input()
alphabet_num = defaultdict(int)
answer = ""

# 文字をカウント
for i in input_string:alphabet_num[i]+=1

while input_string:
    print('input_string :{}'.format(input_string))
    # 小さいアルファベットから
    for c in sorted(c for c in alphabet_num):
        print('c :{}'.format(c))
        print('alphabet_num[{}] :{}'.format(c, alphabet_num[c]))
        # すでに残っていなければスキップ
        if alphabet_num[c]==0: continue
        # 残りの数を一時保存
        remain_num = alphabet_num.copy()
        remain_num[c] -= 1
        print('remain_num[{}] :{}'.format(c, remain_num[c]))
        # 残った文字列の先頭がiでなければ1
        changed_num = 1 if input_string[0]!=c else 0
        print('changed_num :{}'.format(changed_num))
        # 先頭以外の文字
        for j in input_string[1:]:
            if remain_num[j]:
                remain_num[j] -= 1
            else:
                changed_num += 1
                print('changed_num :{}'.format(changed_num))
        # 上限に達してなければ次の文字へ
        if changed_num<=changed_limit:
          alphabet_num[c] -= 1
          # 上限を下げる
          changed_limit -= 1 if input_string[0]!=i else 0
          input_string = input_string[1:]
          answer += c
          print('answer :{}'.format(answer))
          break
    print('=================================')
print(answer)


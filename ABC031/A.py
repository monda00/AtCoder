attack, defence = map(int, input().split())

add_at = (attack + 1) * defence
add_df = attack * (defence + 1)

if add_at > add_df:
    print(add_at)
else:
    print(add_df)


x = list(input())
m = int(input())
X = int(''.join(x))
max_x = int(max(x))


def change_nto10(num, b):
    n = 0
    numlist = list(str(num))
    while(numlist):
        n *= b
        n += int(numlist.pop(0))
    return n


def is_ok(mid):
    """二分探索中の判定

    Parameters
    ----------
    mid : int

    Returns
    -------
    resutl : bool
    """
    t = int(change_nto10(X, mid))
    if t <= m:
        return True
    else:
        return False


def binary_search(ok, ng):
    """二分探索

    Parameters
    ----------
    ok : int
    ng : int

    Returns
    -------
    ok : int
    """
    while ng - ok > 1:
        mid = (ok + ng) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok


if len(x) == 1:
    if X > m:
        ans = 0
    else:
        ans = 1
else:
    ans = binary_search(max_x, 10**18+1) - max_x

print(ans)

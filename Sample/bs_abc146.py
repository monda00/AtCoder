a, b, x = map(int, input().split())


def is_ok(mid):
    """二分探索中の判定

    Parameters
    ----------
    mid : int

    Returns
    -------
    resutl : bool
    """
    if (a * mid) + (b * len(str(mid))) <= x:
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


ans = binary_search(0, 10**9+1)
print(ans)

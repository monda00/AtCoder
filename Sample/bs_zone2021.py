n = int(input())
ability = [list(map(int, input().split())) for _ in range(n)]


def is_ok(mid):
    """二分探索中の判定

    Parameters
    ----------
    mid : int

    Returns
    -------
    resutl : bool
    """
    s = set()
    for a in ability:
        s.add(sum(1 << i for i in range(5) if a[i] >= mid))
    for x in s:
        for y in s:
            for z in s:
                if x | y | z == 31:
                    return True
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

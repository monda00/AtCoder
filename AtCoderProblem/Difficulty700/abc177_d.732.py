'''
[D - Friends](https://atcoder.jp/contests/abc177/tasks/abc177_d)
'''


class UnionFind():
    """
    Union Find木クラス
    Attributes
    --------------------
    n : int
        要素数
    root : list
        木の要素数
        0未満であればそのノードが根であり、添字の値が要素数
    rank : list
        木の深さ
    """

    def __init__(self, n):
        """
        Parameters
        ---------------------
        n : int
            要素数
        """
        self.n = n
        self.root = [-1]*(n+1)
        self.rank = [0]*(n+1)

    def find_root(self, x):
        """
        ノードxの根を見つける
        Parameters
        ---------------------
        x : int
            見つけるノード
        Returns
        ---------------------
        root : int
            根のノード
        """
        if(self.root[x] < 0):
            return x
        else:
            self.root[x] = self.find_root(self.root[x])
            return self.root[x]

    def unite(self, x, y):
        """
        木の併合
        Parameters
        ---------------------
        x : int
            併合したノード
        y : int
            併合したノード
        """
        # 入力ノードのrootノードを見つける
        x = self.find_root(x)
        y = self.find_root(y)
        # すでに同じ木に属していた場合
        if(x == y):
            return
        # 違う木に属していた場合rankを見てくっつける方を決める
        elif(self.rank[x] > self.rank[y]):
            self.root[x] += self.root[y]
            self.root[y] = x
        else:
            self.root[y] += self.root[x]
            self.root[x] = y
            # rankが同じ（深さに差がない場合）は1増やす
            if(self.rank[x] == self.rank[y]):
                self.rank[y] += 1

    def is_samegroup(self, x, y):
        """
        同じグループに属するか判定
        Parameters
        ---------------------
        x : int
            判定したノード
        y : int
            判定したノード
        Returns
        ---------------------
        ans : bool
            同じグループに属しているか
        """
        return self.find_root(x) == self.find_root(y)

    def count(self, x):
        """
        木のサイズを計算
        Parameters
        ---------------------
        x : int
            計算したい木のノード
        Returns
        ---------------------
        cnt : int
            木のサイズ
        """
        return -self.root[self.find_root(x)]


n, m = map(int, input().split())
A = []
B = []
for _ in range(m):
    a, b = map(int, input().split())
    A.append(a-1)
    B.append(b-1)

uf = UnionFind(n)

for i in range(m):
    uf.unite(A[i], B[i])

ans = 0
for i in range(n):
    c = uf.count(i)
    if c > ans:
        ans = c

print(ans)

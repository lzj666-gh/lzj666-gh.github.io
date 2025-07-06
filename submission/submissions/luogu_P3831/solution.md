# P3831 题解

## Description

给定一个 $n \times n\ (1 \leq n \leq 2 \times 10^4)$ 的网格图，走一条边用时 $2$，只能在特定的 $m\ (1 \leq m \leq 10^5)$ 个点转向，转向用时 $1$，求从 $(x_1,x_2)$ 到 $(y_1, y_2)$ 的最短用时。

## Solution

考虑 **分层图最短路** 。

对于样例：

### Sample Input

```
6 9
2 1
2 5
3 2
4 4
5 2
5 6
6 1
6 3
6 4
1 1 4 6
```

### Sample Output

```
27
```

题目所给的图：

![ENyre1.png](https://s2.ax1x.com/2019/05/03/ENyre1.png)

我们按照输入的顺序给这些点标上号（包括起点和终点），共 $m + 2$ 个点。

![ENyBLR.png](https://s2.ax1x.com/2019/05/03/ENyBLR.png)

设 $n = m + 2$，表示点的数量。起点为 $10$ 号节点，终点为 $11$ 号节点。

我们可以把图分成两层，其中第 $1$ 层为横向走，第 $2$ 层为纵向走。

先考虑横向走。将所有点以横坐标为第 $1$ 关键字，纵坐标为第 $2$ 关键字从小到大排序。排完序后，判断相邻两个点的横坐标是否相同，如果相同，则在它们两个点之间连一条边权为 **两点纵坐标之差的两倍** 的双向边。若可以连边 $u \leftrightarrow  v$，则说明从点 $u$ 可以横向走到点 $v$，亦可以从点 $v$ 横向走到点 $u$ 。

图中可以连的边有：

$1 \leftrightarrow 2$

$4 \leftrightarrow 11$

$5 \leftrightarrow 6$

$7 \leftrightarrow 8$

$8 \leftrightarrow 9$

边权分别为 $8,4,8,4,2$ 。

纵向走同理。因为纵向走在第 $2$ 层，节点编号不能与第 $1$ 层相同，所以给第 $2$ 层编号全部 $+n$ 。然后将所有点以纵坐标为第 $1$ 关键字，横坐标为第 $2$ 关键字从小到大排序。比较相邻两点纵坐标，连边。若可以连边 $u \leftrightarrow  v$，则说明从点 $u$ 可以纵向走到点 $v$，也可以从点 $v$ 纵向走到点 $u$ 。

图中可以连的边有：

$10+11 \leftrightarrow 1+11$

$1+11 \leftrightarrow 7+11$

$3+11 \leftrightarrow 5+11$

$4+11 \leftrightarrow 9+11$

$11+11 \leftrightarrow 6+11$

边权分别为 $2,8,4,4,2$ 。

接下来在两层 **表示同个节点的点** 之间连一条权值为 $1$ 的双向边，表示可以在该点改变方向，用时为 $1$ 。

注意起点和终点改变方向不需要 $1$ 的时间，所以在 起点 与 起点$ + n$ 之间，终点 与 终点$ + n$ 之间连一条边权为 $0$ 的双向边。

最后跑一遍起点到终点的最短路即是答案，时间复杂度为 $O(m\log m)$。

完整的图：

![EN41OS.png](https://s2.ax1x.com/2019/05/03/EN41OS.png)

## Code

```cpp
#include <bits/stdc++.h>
using namespace std;
typedef long long LL;

template <class T>
inline void read(T &x) {
    x = 0;
    char c = getchar();
    bool f = 0;
    for (; !isdigit(c); c = getchar()) f ^= c == '-';
    for (; isdigit(c); c = getchar()) x = x * 10 + (c ^ 48);
    x = f ? -x : x;
}

template <class T>
inline void write(T x) {
    if (x < 0) {
        putchar('-');
        x = -x;
    }
    T y = 1;
    int len = 1;
    for (; y <= x / 10; y *= 10) ++len;
    for (; len; --len, x %= y, y /= 10) putchar(x / y + 48);
}

const int MAXN = 3e5, MAXM = 3e6;
int n, m, s, t, tot, head[MAXN + 5], dis[MAXN + 5];
bool vis[MAXN + 5];
struct Station {
    int x, y, id;
} a[MAXN + 5];
struct Edge {
    int next, to, dis;
} e[MAXM + 5];
struct Node {
    int val, id;
    inline friend bool operator<(Node x, Node y) {
        return x.val > y.val;
    }
};

inline void addEdge(int u, int v, int w) {
    e[++tot] = (Edge) { head[u], v, w };
    head[u] = tot;
}

inline bool cmpx(Station a, Station b) {//按横坐标排序 
    return a.x == b.x ? a.y < b.y : a.x < b.x;
}

inline bool cmpy(Station a, Station b) {//按纵坐标排序
    return a.y == b.y ? a.x < b.x : a.y < b.y;
}

inline void dijkstra(int s) {//堆优化 dijkstra 
    priority_queue<Node> q;
    memset(dis, 0x3f, sizeof (dis));
    dis[s] = 0;
    q.push((Node) { 0, s });
    for (; !q.empty(); ) {
        int u = q.top().id;
        q.pop();
        if (vis[u]) continue;
        vis[u] = 1;
        for (int v, w, i = head[u]; v = e[i].to, w = e[i].dis, i; i = e[i].next)
            if (dis[v] > dis[u] + w) {
                dis[v] = dis[u] + w;
                if (!vis[v]) q.push((Node) { dis[v], v });
            }
    }
}

int main() {
    read(n), read(m);
    n = m + 2;//点的总数 
    s = n - 1, t = n;//起点 和 终点 
    for (int i = 1; i <= n; ++i) {
        read(a[i].x), read(a[i].y);
        a[i].id = i;//点的编号 
    }
    sort(a + 1, a + n + 1, cmpx);
    for (int i = 1; i < n; ++i)
        if (a[i].x == a[i + 1].x) {
            addEdge(a[i].id, a[i + 1].id, (a[i + 1].y - a[i].y) << 1);
            addEdge(a[i + 1].id, a[i].id, (a[i + 1].y - a[i].y) << 1);
        } //第一层：横向边 
    sort(a + 1, a + n + 1, cmpy);
    for (int i = 1; i < n; ++i)
        if (a[i].y == a[i + 1].y) {
            addEdge(a[i].id + n, a[i + 1].id + n, (a[i + 1].x - a[i].x) << 1);
            addEdge(a[i + 1].id + n, a[i].id + n, (a[i + 1].x - a[i].x) << 1);
        } //第二层：纵向边 
    for (int i = 1; i <= n - 2; ++i) addEdge(i, i + n, 1), addEdge(i + n, i, 1);
    //两层之间：改变方向用时 1 
    addEdge(s, s + n, 0), addEdge(s + n, s, 0);
    addEdge(t, t + n, 0), addEdge(t + n, t, 0);//起点和终点改变方向不需要时间 
    dijkstra(s);//求 s -> t 最短路 
    write(dis[t] == 0x3f3f3f3f ? -1 : dis[t]);//判断是否有解 
    putchar('\n');
    return 0;
}
```
# P3178 题解

树链剖分固然可以搞。

但还有另一种做法，可以看出，增加一个节点的权值会对以它为根的整棵子树都有影响，相当于给整棵子树增加一个值。

而给以某一节点 x 为根的子树增加一个权值也会影响当前子树，节点 y 所增加的值为 dis[y] \* z - (dis[x] - 1) \* z，每个节点都会增加 -(dis[x] - 1) \* z ，询问时只用加上 dis[y] \* y 和当前节点 y 的权值。

给整棵子树增加一个权值可以用 dfs 序 + 线段树搞， dis 数组可以预处理出来。

——代码









```cpp
#include <cstdio>
#include <cstring>
#define LL long long
#define root 1, 1, n
#define ls now << 1, l, mid
#define rs now << 1 | 1, mid + 1, r
using namespace std;
const int MAXN = 100001;
int n, m, cnt, tot;
int head[MAXN], next[MAXN << 1], to[MAXN << 1], tid[MAXN], size[MAXN];
LL a[MAXN << 2], b[MAXN << 2], val[MAXN], dis[MAXN];
inline void add(int x, int y)
{
    to[cnt] = y;
    next[cnt] = head[x];
    head[x] = cnt++;
} 
inline void dfs(int u)
{
    int i, v; 
    tid[u] = ++tot;
    size[u] = 1;
    for(i = head[u]; i != -1; i = next[i])
    {
        v = to[i];
        if(!size[v])
        {
            dis[v] = dis[u] + 1;
            dfs(v);
            size[u] += size[v];
        }
    }
}
inline void push_down(int now)
{
    a[now << 1] += a[now];
    a[now << 1 | 1] += a[now];
    b[now << 1] += b[now];
    b[now << 1 | 1] += b[now];
    a[now] = b[now] = 0;
}
inline void update(LL x, LL y, int ql, int qr, int now, int l, int r)
{
    if(ql <= l && r <= qr)
    {
        a[now] += x;
        b[now] += y;
        return;
    }
    push_down(now);
    int mid = (l + r) >> 1;
    if(ql <= mid) update(x, y, ql, qr, ls);
    if(mid < qr) update(x, y, ql, qr, rs);
}
inline LL query(int u, int x, int now, int l, int r)
{
    if(l == r) return dis[u] * a[now] + b[now];
    push_down(now);
    int mid = (l + r) >> 1;
    if(x <= mid) return query(u, x, ls);
    else return query(u, x, rs);
}
int main()
{
    int i, x, z;
    LL y;
    scanf("%d %d", &n, &m);
    for(i = 1; i <= n; i++)    scanf("%lld", &val[i]);
    memset(head, -1, sizeof(head));
    for(i = 1; i < n; i++)
    {
        scanf("%d %d", &x, &y);
        add(x, y);
        add(y, x);
    }
    dis[1] = 1;
    dfs(1);
    for(i = 1; i <= n; i++) update(0, val[i], tid[i], tid[i] + size[i] - 1, root);
    for(i = 1; i <= m; i++)
    {
        scanf("%d %d", &z, &x);
        if(z == 1)
        {
            scanf("%lld", &y);
            update(0, y, tid[x], tid[x] + size[x] - 1, root);
        }
        else if(z == 2)
        {
            scanf("%lld", &y);
            update(y, -((dis[x] - 1) * y), tid[x], tid[x] + size[x] - 1, root);
        }
        else printf("%lld\n", query(x, tid[x], root));
    }
    return 0;
}
```
# P1339 题解

### Dijkstra + 线段树解法

最近集训一位大佬给我讲了一个奇妙的Dijkstra优化方法，他告诉我线段树可以代替优先队列来优化Dijkstra。

**我第一个感觉是眼睛一亮**

于是我认真的听完了他讲的方法。

Dijkstra算法周围的大佬已经讲的十分的漂亮了，我觉得我再插一嘴就是多余。所以我就着重讲一下用线段树的优化。

首先考虑我们当时要用优先队列做什么。

是不是就是维护的dis[]数组的最小值以及它的终点？

具体操作？

不就是要我们向优先队列里放入一个dis和终点，然后每次松弛都出队一组，再进行更新？

那么这道题在这里就变成了一个简单的线段树问题。（逃

不过线段树有个性质：不能删点。那该怎么进行那个要求我们出队的操作？

我们可以考虑：如果我们把那个要出队的一组数中dis修改为INF，那么我们只要线段树里有数，就一定取不到INF，就不会用到这组数了，也就相当于出队了。如果我们在最开始初始化（建树）时就只留一个dis为0的s（起点编号），其余都变成INF，那么我们插入一组数时直接单点修改不就好啦？

如何判断队列为空？我们如果队列中只有INF，也就是没有真实要用的数据，队列就是空的了。

这里只需要一个单点修改的一个线段树就好啦。

### 代码实现
```cpp
#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <vector>
using namespace std;
#define go(i, j, n, k) for (int i = j; i <= n; i += k)
#define fo(i, j, n, k) for (int i = j; i >= n; i -= k)
#define rep(i, x) for (int i = h[x]; i; i = e[i].nxt)
#define mn 100010
#define mm 200020
#define inf 2147483647
#define ll long long
#define ld long double
#define fi first
#define se second
#define root 1, n, 1
#define lson l, m, rt << 1
#define rson m + 1, r, rt << 1 | 1
#define bson l, r, rt
inline int read(){
    int f = 1, x = 0;char ch = getchar();
    while (ch > '9' || ch < '0'){if (ch == '-')f = -f;ch = getchar();}
    while (ch >= '0' && ch <= '9'){x = x * 10 + ch - '0';ch = getchar();}
    return x * f;
}
inline void write(int x){
    if (x < 0)putchar('-'),x = -x;
    if (x > 9)write(x / 10);
    putchar(x % 10 + '0');
}
//This is AC head above...
struct node{
    int v, nxt, w;
} e[mm << 1];
int h[mn], p;
inline void add(int a,int b,int c){
    e[++p].nxt = h[a];
    h[a] = p;
    e[p].v = b;
    e[p].w = c;
}
int dis[mn];
int n, m, s, t;
struct tree{
    int minw, minv;
};
struct SegmentTree{
    tree z[mn << 2];
    inline void update(int rt){
        z[rt].minw = min(z[rt << 1].minw, z[rt << 1 | 1].minw);//维护区间最小值
        z[rt].minv = (z[rt << 1].minw < z[rt << 1 | 1].minw) ? z[rt << 1].minv : z[rt << 1 | 1].minv;//维护区间最小值位置
    }
    inline void build(int l,int r,int rt){//建树
        if(l==r){
            z[rt].minw = l == s ? 0 : inf;//我们可以直接建树时把s的点设置为0
            z[rt].minv = l;//记录最小值位置，方便修改
            return;
        }
        int m = (l + r) >> 1;
        build(lson);
        build(rson);
        update(rt);
    }
    inline void modify(int l,int r,int rt,int now,int v){//单点修改
        if(l==r){
            z[rt].minw = v;
            return;
        }
        int m = (l + r) >> 1;
        if(now<=m)
            modify(lson, now, v);
        else
            modify(rson, now, v);
        update(rt);
    }
} tr;
inline void Dij(){//Dijkstra的核心部分
    go(i,1,n,1){
        dis[i] = inf;
    }//初始化dis
    dis[s] = 0;
    while(tr.z[1].minw < inf){//这里就是判断是否为空
        int x = tr.z[1].minv;//取整个线段树中最小的点
        tr.modify(root, x, inf);//单点修改最小的点为inf
        rep(i,x){
            int v = e[i].v;
            if(dis[v] > dis[x] + e[i].w){
                dis[v] = dis[x] + e[i].w;
                tr.modify(root, v, dis[x] + e[i].w);//这里就是类似入队操作
            }
        }
    }
}
int main(){
    n = read(), m = read(), s = read(), t=read();
    go(i,1,m,1){
        int x = read(), y = read(), v = read();
        add(x, y, v);
        add(y, x, v);//这个一定记住，无向图要正反两条边QAQ
    }
    tr.build(root);//建树
    Dij();//Dijkstra
    cout << dis[t];
    return 0;
}

```

### 这样似乎要比priority_queue优化快一些

#### 第十一次写题解，希望可以给想优化Dijkstra的同学一个新思路
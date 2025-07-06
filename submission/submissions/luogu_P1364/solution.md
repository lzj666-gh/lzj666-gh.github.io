# P1364 题解

现有的题解基本是用Floyed或者其他稍优的算法跑的，其时间复杂度均在$O(n^2)$以上。

那么问题来了，

**你们经历过绝望吗**

这题作为我们图论考试的一道题，n的范围直接到了10000，此时N^2的算法也无法AC。

有句写居里夫人的话：“**别人摸瓜她寻藤，别人摘叶他问根**”

我们也要做那个“她”， 不能只满足于通过此题，而且要了解本题的$O(N)$算法正解：带权树的重心。

### 树的重心的定义：
树若以某点为根，使得该树最大子树的结点数最小，那么这个点则为该树的重心，一棵树可能有多个重心。

### 树的重心的性质：
1、树上所有的点到树的重心的距离之和是最短的，如果有多个重心，那么总距离相等。

2、插入或删除一个点，树的重心的位置最多移动一个单位。

3、若添加一条边连接2棵树，那么新树的重心一定在原来两棵树的重心的路径上。

当然，这题我们只需要用到第一条性质。

### 怎么求树的重心：
定义几个数组：$f[u]$表示以u为根的总距离，$size[u]$表示以u为根的子树的大小（结点数，**此题每个点要乘以权值**，下文结点数均指此）。

显然，$ans=min(f[i],1<=i<=n)$

首先我们任意以一个点为根dfs一遍，求出以该点为根的总距离。方便起见，我们就以1为根。

接下来就是转移，对于每个u能达到的点v，有：
$$f[v]=f[u]+size[1]-size[v]-size[v]$$
怎么来的呢？试想，当根从u变为v的时候，v的子树的所有节点原本的距离要到$u$，现在只要到$v$了，每个结点的距离都减少1，那么总距离就减少$size[v]$，同时，以v为根的子树以外的所有节点，原本只要到$u$就行了，现在要到$v$，每个节点的路程都增加了1，总路程就增加了$size[1]-size[v]$，其中$size[1]$就是我们预处理出来的整棵树的大小，减去$size[v]$就是除以v为根的子树以外的结点数。

最后取最小值，得解。时间复杂度$O(n)$

附上代码：
```cpp
#include <cstdio>
#define rep(i, m, n) for(register int i = m; i <= n; ++i)
#define INF 2147483647
#define Open(s) freopen(s".in","r",stdin);freopen(s".out","w",stdout);
#define Close fclose(stdin);fclose(stdout);
using namespace std;
inline int read(){
	int s = 0, w = 1;
	char ch = getchar();
	while(ch < '0' || ch > '9') { if(ch == '-') w = -1; ch = getchar(); }
	while(ch >= '0' && ch <= '9') { s = s * 10 + ch - '0'; ch = getchar(); }
	return s * w;
}
const int MAXN = 10010;
struct Edge{
	int next, to;
}e[MAXN << 1];
int head[MAXN], num, w[MAXN], n, size[MAXN];
long long ans = INF, f[MAXN];
inline void Add(int from, int to){
	e[++num].to = to;
	e[num].next = head[from];
	head[from] = num;
}
void dfs(int u, int fa, int dep){ //预处理f[1]和size
    size[u] = w[u];
	for(int i = head[u]; i; i = e[i].next){
	   if(e[i].to != fa)
	     dfs(e[i].to, u, dep + 1), size[u] += size[e[i].to];
	}
	f[1] += w[u] * dep;
}
void dp(int u, int fa){  //转移
    for(int i = head[u]; i; i = e[i].next)
       if(e[i].to != fa)
         f[e[i].to] = f[u] + size[1] - size[e[i].to] * 2, dp(e[i].to, u);
    ans = min(ans, f[u]); //取最小值
}
int a, b;
int main(){
    //Open("hospital");
    ans *= ans;
    n = read();
    rep(i, 1, n){
       w[i] = read();
       a = read(); b = read();
       if(a) Add(i, a), Add(a, i);
       if(b) Add(i, b), Add(b, i);
    }
    dfs(1, 0, 0);
    dp(1, 0);
    printf("%lld\n", ans);
    //Close;
    return 0;
}

```
# P5632 题解

## Stoer-Wagner 全局最小割算法

之前一篇题解没有证明，我来加上一个证明。

参考文章：[全局最小割StoerWagner算法详解 By Oyking](https://www.cnblogs.com/oyking/p/7339153.html)

设原图为 $G=(V,E)$，最小割为 $C\in E$。

算法基本思想：对于无向图上任意两点 $s,t$，割去 $C$ 后，则或者 $s,t$ 处于同一连通块，或者 $s,t$ 处于不同两连通块（显然）。

1. 对于 $s,t$ 处于同一连通块的情况，根据割的定义，割去 $C$ 后至少有一个点 $j$，与 $s$ 不在一个连通块内，则 $j,t$ 也不在一个连通块内，那么 $j$ 与 $s,t$ 都不在一个连通块内，所以凡是 $j$ 与 $s,t$ 之间的边必须全部割去，如果 $(j,s)$ 边被割去，则如果 $(j,t)$ 未被割去，$(j,s)$ 不割是一种更小的割法（与最小割矛盾），因此如果 $(j,s)\in C$，则有 $(j,t)\in C$，所以 $s,t$ 可看作是一个整体，共享所有的边。

那么，处理完一对 $s,t$ 之间的最小割后，就只有它们处于同一连通块的情况了，也就是做完一对以后就合并一对点，如是进行 $n-1$ 次即合并成一个点，算法完成。

2. 下面主要探讨 $s,t$ 不在一联通块时的答案，即 $s,t$ 之间的最小割，注意 $s,t$ 的选择是任意的。

构造过程依赖于一个集合 $A$，一开始，我们令 $A=\varnothing$，然后我们将所有点（合并了的点算一个）按照某种顺序加入 $A$ 中。

加入顺序依赖于权值函数 $w(i)$，我们令 $w(i)$ 表示 $\sum\limits_{j\in A} d(j,i)$，其中 $d(j,i)$ 表示 $j,i$ 之间的边权（因为求最小割，如果没有边可视为不用割，即 $d(j,i)=0$）。

算法流程：每次选择 $w(i)$ 最大的 $i$ 加入 $A$ 中，如是进行 $|V'|$ 次（其中 $|V'|$ 表示当前图的点数）即可确定所有点加入 $A$ 的顺序，定义 $ord(i)$ 表示第 $i$ 个加入 $A$ 的点，令 $t=ord(|V'|)$，则对于任意一点 $s$，$s$ 到 $t$ 的最小割即为 $w(t)$。

下面来证明一下以上算法的正确性（来自最上面的链接）：

若点 $v$ 满足：在割去 $C$ 的图中，存在一个点 $u$，在 $v$ 之前加入 $A$，且 $u$ 和 $v$ 不在一连通块内，则称 $v$ 是 Active 的。

下证对于任意一个 Active 结点 $v$，$C$ 中处在 $v$ 前的部分不小于 $w(v)$。如果此结论成立，则因 $t$ 最后加入 $A$，所以 $C$ 在 $t$ 前部分就是整个 $C$，于是 $C\ge w(t)$，又将 $w(t)$ 割去后 $t$ 与其他点都不连通，所以 $w(t)$ 就是 $t$ 到之前任意一点的最小割。

运用数学归纳法，对于第一个 Active 结点 $v$，结论成立：因为 $v$ 前结点都不是 Active 结点，所以都处在一连通块内，所以 $v$ 与它们都不处在一连通块内，所以想要割去 $v$ 需要断开它和之前所有点的边，即 $w(v)$。

对于 $v$ 之后的第一个 Active 结点 $u$，有 $w(u)$ 是从 $v$ 前结点和 $v$ 到 $u$ 之间结点与 $u$ 的边构成的，对于 $v$ 前面的结点，$w(u)$ 的这一部分不超过 $w(v)$（因为 $v$ 先加入 $A$）。而对于 $v$ 到 $u$ 之间结点，与 $v$ 同样道理地，与 $u$ 边权相加一定要出现在 $C$ 中，两者相加，所以完整的 $w(u)$ 必然大于等于 $C$ 在 $u$ 前部分，归纳可得证。

```cpp
#include <bits/stdc++.h>
using namespace std;
const int MAXN=610,INF=1e9;
int n,m,x,y,z,s,t,dis[MAXN][MAXN],w[MAXN],dap[MAXN],vis[MAXN],ord[MAXN];
int proc (int x) {
	memset(vis,0,sizeof(vis));
	memset(w,0,sizeof(w));
	w[0]=-1;
	for (int i=1;i<=n-x+1;i++) {
		int mx=0;
		for (int j=1;j<=n;j++) {
			if (!dap[j]&&!vis[j]&&w[j]>w[mx]) {mx=j;}
		}
		vis[mx]=1,ord[i]=mx;
		for (int j=1;j<=n;j++) {
			if (!dap[j]&&!vis[j]) {w[j]+=dis[mx][j];}
		}
	}
	s=ord[n-x],t=ord[n-x+1];
	return w[t];
}
int sw () {
	int res=INF;
	for (int i=1;i<n;i++) {
		res=min(res,proc(i));
		dap[t]=1;
		for (int j=1;j<=n;j++) {
			dis[s][j]+=dis[t][j];
			dis[j][s]+=dis[j][t];
		}
	}
	return res;
}
int main () {
	scanf("%d%d",&n,&m);
	for (int i=1;i<=m;i++) {
		scanf("%d%d%d",&x,&y,&z);
		dis[x][y]+=z,dis[y][x]+=z;
	}
	printf("%d\n",sw());
	return 0;
}
```
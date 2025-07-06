# P5787 题解

# $\text{线段树分治}$
## $\text{引入}$
一张图有 $n$ 个节点的图， 在 $k$ 时间中会出现 $m$ 条边，表示有一条连接 $x,y$ 的边在  $l$ 时刻出现 $r$ 时刻消失，求问在第 $i$ 个时间段中图是否为二分图。
### $\text{分析}$
- ### 先对于二分图来分析

如果顶点 $V$ 可分割为两个互不相交的子集 $(A,B)$ ，并且图中的每条边 $(i,j)$ 所关联的两个顶点 $i$ 和 $j$ 分别属于这两个不同的顶点集 $(i \in A,j \in B)$ ，则称图 $G$ 为一个二分图。 —— 百度百科。

- 在一般的做法中对于一个图是否为二分图，我们一般是采用染色法，如果一个图为二分图，那么一条边所连接的两个点一定是在不同集合的，也就是点的颜色不同。

- 分析到这里，我们就有了最朴素的算法，对于每个时间段，我们可以建一张图，再用 $O(n)$ 的时间遍历染色。总的复杂度就为 $O(n^2\times k)$ 。

这样的时间复杂度和空间复杂度都必须优化。回忆一下我们在 [关押罪犯](https://www.luogu.com.cn/problem/P1525) 中还学了一种判断二分图的方法 **扩展域并查集** 。如果有不了解的，用几句话介绍一下。

- 扩展域并查集：对于一个节点 $i$ ，我们将其拆分为两个节点。一个属于集合 $S$ ，另一个属于集合 $T$ 。那么一条边所连接的两个节点就必须在不同的集合中。一个点在 $S$ 中和在 $T$ 的两个点属于一个集合，那么这张图就不是二分图。

其实有了扩展域并查集，我们并没有优化时间复杂度。这只是为下文的算法铺垫。

- ### 对于时间段分析

我们如果还要优化复杂度，那么我们就不能枚举每个时间段。必须找个更靠谱的算法。

- 如果学习过线段树优化建边，那么下文将好理解一些。我们把时间轴画出来，那么对于每一条边它总是在时间轴上覆盖了一些区域。所以对于一条边我们可以将其分解。

- 我们先将时间轴构建 $\log k$ 层，然后就像插入区间一样，把每一条边插入。因为对于线段树上的一个节点，它的子节点也一定被这条边覆盖，那么我们只需要在父亲节点储存这条边。那么这样对于一条边最大也只会分解为 $\log k $ 不重复的较小的边。
![](https://cdn.luogu.com.cn/upload/image_hosting/p2fgmu5l.png)

- 这样我们把所有询问下来，最后一次性处理。但是我们发现当我们处理完这个节点的子节点时，我们必须将并查集还原到处理之前的状态才可以递归处理其他节点了。难道我们这里只能写个 $LCT$ 这种支持 $O(\log n)$ 删边的数据结构？显然不是 。~~（否则讲这么久的并查集干啥）~~

![](https://cdn.luogu.com.cn/upload/image_hosting/ceoa7omc.png)

- 这里的并查集只需要维护一个集合所属关系，那么我们对其操作其实是非常简明的，就是改变父亲的所属关系。我们可以把所有操作放在栈里，当我们退出时，撤销原操作就行了。这样我们就不可以路径压缩了，因为每个节点是要储存真正的父亲的。为了保证复杂度的正确性，必须要按秩合并。大概就是树低的合并到树高的父亲下面，这样树的高度是不会高于 $O(\log n)$ 的。

- 那么这道题就算做完了。其主要是构建一个时间轴上的线段树，再通过并查集维护答案。时间复杂度为 $O(n\log k\log n)$ 。
## $\text{代码}$

```cpp
#include<bits/stdc++.h>
using namespace std;
const int N = 10101010;
int read(){
	int x = 0,f = 0;char ch=getchar();
	while(!isdigit(ch)){if(ch=='-')f=1;ch=getchar();}
	while(isdigit(ch)){x=x*10+ch-'0';ch=getchar();}
	return f?-x:x;
}

int n,m,k,fa[N],height[N],top;
struct E{int x,y;}e[N];
struct Stack{int x,y,add;}st[N];
vector<int> t[N];

int findfa(int x)
{
	while(x != fa[x]) x = fa[x];
	return fa[x];
}
void debug()
{
	printf("\n****************\n下标");
	for(int i = 1;i <= n*2;i++) printf("%d ",i); 
	printf("\n父亲");
	for(int i = 1;i <= n*2;i++) printf("%d ",fa[i]);
	printf("\n祖先(代表元)");
	for(int i = 1;i <= n*2;i++) printf("%d ",findfa(i));
}
void merge(int x,int y)
{
	int fx = findfa(x),fy = findfa(y);
	if(height[fx] > height[fy]) swap(fx,fy);
	st[++top] = (Stack){fx,fy,height[fx] == height[fy]};
	fa[fx] = fy;
	if(height[fx] == height[fy]) height[fy]++;
}
void update(int u,int l,int r,int L,int R,int x)
{
	if(l > R || r < L) return;
	if(L <= l && r <= R) {t[u].push_back(x);return;}
	int mid = l + r >> 1;
	update(u<<1,l,mid,L,R,x);
	update(u<<1|1,mid+1,r,L,R,x);
}
void solve(int u,int l,int r)
{
//	debug();
	int ans = 1;
	int lasttop = top;
	for(int i = 0;i < t[u].size();i++)
	{
		int a = findfa(e[t[u].at(i)].x);
		int b = findfa(e[t[u].at(i)].y);
		if(a == b)
		{
			for(int k = l;k <= r;k++)
			printf("No\n");
			ans = 0;
			break;
		}
		merge(e[t[u].at(i)].x,e[t[u].at(i)].y+n);
		merge(e[t[u].at(i)].y,e[t[u].at(i)].x+n);
	}
	if(ans)
	{
		if(l==r) printf("Yes\n");
		else 
		{
			int mid = l+r>>1;
			solve(u<<1,l,mid);
			solve(u<<1|1,mid+1,r);
		}
	}
	while(top > lasttop)
	{
		height[fa[st[top].x]] -= st[top].add;
		fa[st[top].x] = st[top].x;
		top--;
	}
	return;
}
int main()
{
	n = read();m = read();k = read();
	for(int i = 1;i <= m;i++)
	{
		e[i].x = read();e[i].y = read();
		int l = read()+1,r = read();
		update(1,1,k,l,r,i);
	}
	for(int i = 1;i <= 2*n;i++) fa[i] = i,height[i] = 1;
	solve(1,1,k);
	return 0;
}
```

## $\text{应用}$
- CF1140F
- P5227
- P4585
- CF576E

# P7113 题解

如果说去掉高精度的话，还是一道非常好的 **拓扑** 排序题目。

本篇代码无高精，请自行添加（因为太复杂了qwq）。

## 拓扑排序：

拓扑排序主要思路在一个**有向无环图**中，先统计出每个点的入度个数，然后将入度为0的点入队，接着把队中每个点向它的出边做一个运算（本题中是将水分流到与其相连节点），然后断边（相连的点入度-1），最后就会得出排水节点的水量。

有不明白的同学可以看 [神经网络](https://www.luogu.com.cn/problem/P1038) [车站分级](https://www.luogu.com.cn/problem/P1983) [旅行计划](https://www.luogu.com.cn/problem/P1137) 都是很好的拓扑排序模板题。

拓扑排序函数：

```
void tp(){
	for(int i=1;i<=n;i++)//所有入度为0的点入队（1-m）
		if(!in[i]){
			book[i]=1;
			q.push(i);
			xx[i]=1,yy[i]=1;
		}
	while(!q.empty()){
		int p=q.front();
		q.pop();
		if(out[p])
			continue;
		for(int i=0;i<a[p].size();i++){
			add(a[p][i],xx[p],yy[p]*(1ll*a[p].size()));
			if(book[a[p][i]])
				continue;
			in[a[p][i]]--;
			if(in[a[p][i]]==0){
				book[a[p][i]]=1;
				q.push(a[p][i]);
			}
		}
	}
	return;
}
```

### 注意几点：
 
1. 如果是 `vector` 存边，一定不要访问排水节点的 `size()` 这样可能会炸，要事先存一下。

2.本题是前 `m` 个点是入水口，一定要注意审好题（虽然只有前 `m` 个点入度为0）。

---
## 分数处理：

我主要运用的是通分思想：

$ \frac{a}{b}+\frac{c}{d}=\frac{ad}{bd}+\frac{cb}{bd}=\frac{ad+cb}{bd} $

紧接着用 `gcd` 化简(考场差点写挂):

```
ll gcd(ll x,ll y){
	if(y==0)
		return x;
	return gcd(y,x%y);
}
```

下面是通分代码：

```
void add(int u,ll x,ll y){
	if(y==0)
		return;
	if(yy[u]==0){
		xx[u]=x;
		yy[u]=y;
		return;
	}
	ll p1=xx[u]*y+yy[u]*x;
	ll p2=yy[u]*y;
	ll p3=gcd(p1,p2);
	xx[u]=p1/p3;
	yy[u]=p2/p3;
	return;
}
```
### 注意事项：

1.一定要判出要添加的分母是否为`0`，如果为`0` 直接赋值即可。

2.最后输出保险在约分一下。

## 全部代码(考试代码)：

```
#include<iostream>
#include<cstdio>
#include<cmath>
#include<algorithm>
#include<queue>
#include<stack>
#include<vector>
#include<map>
#define ll long long
using namespace std;
inline ll read(){
	ll x=0,f=1;char ch=getchar();
	while(ch<'0'||ch>'9'){if(ch=='-')f=-1;ch=getchar();}
	while(ch>='0'&&ch<='9'){x=x*10+ch-'0';ch=getchar();}
	return x*f;
}
int n,m,in[100001],out[100001],book[100001];
ll xx[100001],yy[100001];
ll gcd(ll x,ll y){
	if(y==0)
		return x;
	return gcd(y,x%y);
}
void add(int u,ll x,ll y){
	if(y==0)
		return;
	if(yy[u]==0){
		xx[u]=x;
		yy[u]=y;
		return;
	}
	ll p1=xx[u]*y+yy[u]*x;
	ll p2=yy[u]*y;
	ll p3=gcd(p1,p2);
	xx[u]=p1/p3;
	yy[u]=p2/p3;
	return;
}
vector<int> a[500001];
queue<int> q;
void tp(){
	for(int i=1;i<=n;i++)
		if(!in[i]){
			book[i]=1;
			q.push(i);
			xx[i]=1,yy[i]=1;
		}
	while(!q.empty()){
		int p=q.front();
		q.pop();
		if(out[p])
			continue;
		for(int i=0;i<a[p].size();i++){
			add(a[p][i],xx[p],yy[p]*(1ll*a[p].size()));
			if(book[a[p][i]])
				continue;
			in[a[p][i]]--;
			if(in[a[p][i]]==0){
				book[a[p][i]]=1;
				q.push(a[p][i]);
			}
		}
	}
	return;
}
int main()
{
	//freopen("water.in","r",stdin);
	//freopen("water.out","w",stdout);
	n=read(),m=read();
	for(int i=1;i<=n;i++){
		int d=read();
		if(d==0){
			out[i]=1;
			continue;
		}
		while(d--){
			int v;
			v=read();
			a[i].push_back(v);
			in[v]++;
		}
	}
	tp();
	for(int i=1;i<=n;i++){
		if(out[i]){
			add(i,0,1);
			printf("%lld %lld\n",xx[i],yy[i]);
		}
	}
	return 0;
}
```

谢谢大家！

# P3806 题解

## 给一种~~另类~~的点分治!(非常好理解)

是一种不用桶的做法,数据范围珂以达到 $0\leq c,K \leq 10^9$ (或者更大)

---

### update 2020.2.8 修改了一些小错误

并update:代码在bzoj1316因为没有特判询问0导致WA掉的锅.(感谢 @jiaangk 指出)

### update 2021.3.3 修改了复杂度的错误

---

我看大部分题解的calc函数里都是:

```cpp
void calc(int u){
	...
	//注:tot为d数组长度
	for(int i=1;i<=tot;i++){
		for(int j=1;j<=tot;j++){
			...
		}
	}
	...
}
```
问一句: 
#### 你们不怕T么?
~~我相信回答一定是:你谷数据太菜~~ (update: 2020.2.2 管理员数据加强后确实会T)

### 双层循环?构造一个菊花图一定T!

所以,我这里给出一个复杂度是 $\mathcal{O}(n \log^{2}n+nm\log n)$ 的做法。

`calc` 函数和 `get_dis` 函数不一样，其他都差不多。

------------

记当前分治的根为 $root$。

- $a$ 数组记录从 $root$ 能到的点;

- $d$ 数组记录 $a_{i}$ 到 $root$ 的距离;

- $b$ 数组记录 $a_{i}$ 属于 $root$ 的哪一棵子树(即当 $b_{a_i}=b_{a_j}$ 时,说明 $a_{i}$ 与 $a_{j}$ 属于 $root$ 的同一棵子树)

### 注意：将 $a$ 数组排序时应按照 $d$ 值的从小到大:

cmp函数:


```cpp
bool cmp(int x,int y){
	return d[x]<d[y];
}
```

`get_dis` 函数借鉴了P4178的思想(即用两个指针 $l,r$ 遍历数组)

现在,请看 `get_dis` 与 `calc`

```cpp
void get_dis(int u,int fa,int dis,int from){
	a[++tot]=u;//加入一个新结点
	d[u]=dis;
	b[u]=from;
	for(int i=head[u];i;i=edge[i].nxt){
		int v=edge[i].to;
		if(v==fa||vis[v])continue;
		get_dis(v,u,dis+edge[i].val,from);
	}
}
void calc(int u){
	tot=0;
	a[++tot]=u;
	d[u]=0;
	b[u]=u;//别忘了加上root自己
	for(int i=head[u];i;i=edge[i].nxt){
		int v=edge[i].to;
		if(vis[v])continue;
		get_dis(v,u,edge[i].val,v);
	}
	sort(a+1,a+tot+1,cmp);
	for(int i=1;i<=m;i++){
		int l=1,r=tot;
		if(ok[i])continue;
		while(l<r){
			if(d[a[l]]+d[a[r]]>query[i]){//当和比询问的长度大时,右指针左移
				r--;
			}
			else if(d[a[l]]+d[a[r]]<query[i]){//类似上边
				l++;
			}
			else if(b[a[l]]==b[a[r]]){//和为询问的长度,但同属一棵子树,继续下一种情况
				if(d[a[r]]==d[a[r-1]])r--;
				else l++;
			}
			else{
				ok[i]=true;
				break;
			}
		}
	}
}
```
***talk is cheap,show me your code!***

## 全部代码:

```cpp
#include<iostream>
#include<cstdio>
#include<algorithm>
using namespace std;
#define N 10001
#define re register 
inline int read(){
    int x=0,f=1;
    char c=getchar();
    while(c<'0'||c>'9'){
        if(c=='-')f=-1;
        c=getchar();
    }
    while(c>='0'&&c<='9'){
        x=(x<<3)+(x<<1)+c-'0';
        c=getchar();
    }
    return x*f;
}
int n,m,query[101];
int e_cnt=0,head[N],maxp[N],siz[N],root,tot=0,d[N],b[N],a[N];
bool vis[N],ok[101];
struct Edge{
	int to,nxt,val;
}edge[N<<1];
void add(int a,int b,int c){
	e_cnt++;
	edge[e_cnt].nxt=head[a];
	edge[e_cnt].to=b;
	edge[e_cnt].val=c;
	head[a]=e_cnt;
}
void get_root(int u,int fa,int total){
	siz[u]=1;
	maxp[u]=0;
	for(re int i=head[u];i;i=edge[i].nxt){
		int v=edge[i].to;
		if(v==fa||vis[v])continue;
		get_root(v,u,total);
		siz[u]+=siz[v];
		maxp[u]=max(siz[v],maxp[u]);
	}
	maxp[u]=max(maxp[u],total-siz[u]);
	if(!root||maxp[u]<maxp[root]){
		root=u;
	}
}
bool cmp(int x,int y){
	return d[x]<d[y];
}
void get_dis(int u,int fa,int dis,int from){
	a[++tot]=u;
	d[u]=dis;
	b[u]=from;
	for(re int i=head[u];i;i=edge[i].nxt){
		int v=edge[i].to;
		if(v==fa||vis[v])continue;
		get_dis(v,u,dis+edge[i].val,from);
	}
}
void calc(int u){
	tot=0;
	a[++tot]=u;
	d[u]=0;
	b[u]=u;
	for(int i=head[u];i;i=edge[i].nxt){
		int v=edge[i].to;
		if(vis[v])continue;
		get_dis(v,u,edge[i].val,v);
	}
	sort(a+1,a+tot+1,cmp);
	for(int i=1;i<=m;i++){
		int l=1,r=tot;
		if(ok[i])continue;
		while(l<r){
			if(d[a[l]]+d[a[r]]>query[i]){
				r--;
			}
			else if(d[a[l]]+d[a[r]]<query[i]){
				l++;
			}
			else if(b[a[l]]==b[a[r]]){
				if(d[a[r]]==d[a[r-1]])r--;
				else l++;
			}
			else{
				ok[i]=true;
				break;
			}
		}
	}
}
void solve(int u){
	vis[u]=true;
	calc(u);
	for(re int i=head[u];i;i=edge[i].nxt){
		int v=edge[i].to;
		if(vis[v])continue;
		root=0;
		get_root(v,0,siz[v]);
		solve(root);
	}
}
int main(){
	n=read(),m=read();
	for(re int i=1;i<=n-1;i++){
		int u,v,w;
		u=read(),v=read(),w=read();
		add(u,v,w);
		add(v,u,w);
	}
	for(re int i=1;i<=m;i++){
		query[i]=read();
		if(!query[i])ok[i]=1;//这里,加个特判
	}
	maxp[0]=n;
	get_root(1,0,n);
	solve(root);
	for(re int i=1;i<=m;i++){
		if(ok[i]){
			cout<<"AYE"<<endl;
		}
		else{
			cout<<"NAY"<<endl;
		}
	}
	return 0;
}

```

[*Froggy's blog*](https://www.luogu.org/blog/froggy/)

#### 呱!!
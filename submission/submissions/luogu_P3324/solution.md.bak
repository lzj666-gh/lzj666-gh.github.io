# P3324 题解

# 广告

[蒟蒻のblog](http://www.cnblogs.com/dedicatus545/p/8845918.html)

# 正文

首先，有一个非常明显的模型：

将激光武器放到一边，机器人放到另一边，从每一个激光武器向它可以攻击的机器人连边，形成一个二分图

建立附加源点$ss$和附加汇点$tt$，$ss$连所有激光武器，$tt$连所有机器人，跑网络流算法

但是，问题在于这道题“武器的攻击是连续的”，也就是解是实数解

这使得我一开始想的费用流算法失效了

时间为实数，就说明我们不能把时间当成费用来看，那么该怎么办呢？

我们考虑把实数时间从费用的位置转到流量的位置去

但是流量在一开始就是确定的，最大流跑出来的结果只能用来判断是否是一个解

既然这样，我们就使用二分的方法，将最优化问题转化为判断性问题

二分时间t，每一次对于t，按照如下方式建边（以下用$\left(u,v,w\right)$表示u到v的流量为w的有向边）

对于每一个激光武器i，建边$\left(ss,i,B\left[i\right]\ast t\right)$

对于激光武器i可以攻击的机器人，建边$\left(i,j,inf\right)$

对于每一个机器人j，建边$\left(j,tt,A\left[j\right]\right)$

如果最大流流量等于所有机器人的生命之和，那么r=mid，否则l=mid+1

因为精度要求只有1e-3，所以把所有生命和时间都乘一个10000处理，要开long long 

# Code:

```cpp
#include<cstdio>
#include<cstring>
#include<iostream>
#include<algorithm>
#define inf 1e15
#define ll long long
using namespace std;
inline ll read(){
	ll re=0,flag=1;char ch=getchar();
	while(ch>'9'||ch<'0'){
		if(ch=='-') flag=-1;
		ch=getchar();
	}
	while(ch>='0'&&ch<='9') re=(re<<1)+(re<<3)+ch-'0',ch=getchar();
	return re*flag;
}
ll n,m,cnt=-1,first[210],dep[210],cur[210];
struct edge{
	ll to,next,w;
}a[100010];
void add(ll u,ll v,ll w){
	a[++cnt]=(edge){v,first[u],w};first[u]=cnt;
	a[++cnt]=(edge){u,first[v],0};first[v]=cnt;
}
bool bfs(ll s,ll t){
	ll q[210],head=0,tail=1,i,u,v;
	for(i=s;i<=t;i++) dep[i]=-1,cur[i]=first[i];
	q[0]=s;dep[s]=0;
	while(head<tail){
		u=q[head++];
		for(i=first[u];~i;i=a[i].next){
			v=a[i].to;
			if(~dep[v]||!a[i].w) continue;
			dep[v]=dep[u]+1;q[tail++]=v;
		}
	}
	return ~dep[t];
}
ll dfs(ll u,ll t,ll limit){
	if(u==t||!limit) return limit;
	ll i,v,f,flow=0;
	for(i=first[u];~i;i=a[i].next){
		v=a[i].to;
		if(dep[v]==dep[u]+1&&(f=dfs(v,t,min(limit,a[i].w)))){
			a[i].w-=f;a[i^1].w+=f;
			flow+=f;limit-=f;
			if(!limit) return flow;
		}
	}
	return flow;
}
ll dinic(ll s,ll t){
	ll re=0;
	while(bfs(s,t)) re+=dfs(s,t,inf);
	return re;
}
bool x[60][60];ll hp[60],atk[60],sum=0;
void init(){
	memset(first,-1,sizeof(first));memset(a,0,sizeof(a));cnt=-1;
}
void build(ll t){
	ll ss=0,tt=n+m+1,i,j;
	for(i=1;i<=m;i++) add(ss,i,t*atk[i]);
	for(i=1;i<=n;i++) add(i+m,tt,hp[i]);
	for(i=1;i<=m;i++){
		for(j=1;j<=n;j++){
			if(x[i][j]) add(i,j+m,inf);
		}
	}
}
int main(){
	n=read();m=read();ll i,j,le,ri,mid,ans;
	for(i=1;i<=n;i++) hp[i]=read(),hp[i]*=10000ll,sum+=hp[i];
	for(i=1;i<=m;i++) atk[i]=read();
	for(i=1;i<=m;i++){
		for(j=1;j<=n;j++) x[i][j]=read();
	}
	le=0;ri=100000000000ll;
	while(le<ri){
		mid=(le+ri)>>1ll;
		init();
		build(mid);
		ans=dinic(0,n+m+1);
		if(ans<sum) le=mid+1;
		else ri=mid;
	}
	printf("%.4lf",(double)le/10000.0);
}
```